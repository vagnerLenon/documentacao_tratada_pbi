import re
import sys
from datetime import datetime
from os import listdir, path
from time import sleep


class DataFrame:
    def __init__(self, columns: list = None, rows: list = None):
        self.columns = columns
        self.rows = rows

    columns = None
    rows = None

    def to_md(self, nl="") -> str:

        md_text = ""
        if self.columns in [None, []]:
            return md_text

        # Titulos
        md_text += f"|{'|'.join(self.columns)}|\n"
        md_text += f"|{'|'.join(['---' for _ in self.columns])}|\n"

        if self.rows not in [None, []]:
            lines = [[DataFrame.__remove_tags(c) for c in l] for l in self.rows]
            md_text += "\n".join([f"|{'|'.join(r)}|" for r in lines])

        return md_text + nl

    def to_html(self) -> str:

        md_text = "<table>\n"
        if self.columns in [None, []]:
            return md_text

        # Titulos
        md_text += (
            f"<thead>\n<tr><th>{'</th><th>'.join(self.columns)}</th></tr>\n</thead>\n"
        )

        if self.rows not in [None, []]:
            md_text += "<tbody>\n"

            md_text += "\n".join(
                [f"<tr><td>{'</td><td>'.join(r)}</td></tr>" for r in self.rows]
            )
            md_text += "\n</tbody>\n"

        md_text += "</table>"

        return md_text

    @staticmethod
    def from_html(html_table: str):
        tabelas = DataFrame.__get_tables(html_table)
        if tabelas is None:
            return DataFrame()
        else:
            if len(tabelas) == 1:
                tabela = tabelas[0]
                columns, rows = DataFrame.__get_one_table(tabela)
                return DataFrame(columns=columns, rows=rows)
            else:

                dfs = []

                for t in tabelas:
                    columns, rows = DataFrame.__get_one_table(t)
                    df = DataFrame(columns, rows)
                    dfs.append(df)

                return dfs

    @staticmethod
    def __get_tables(html: str):
        html = DataFrame.__remove_tabs_ans_newlines(html)
        tables = [
            (t[t.find("<table") :] + "</table>")
            .replace("<tr >", "<tr>")
            .replace("<th >", "<th>")
            .replace("<td >", "<td>")
            .replace("th>", "td>")
            for t in html.split("</table>")
        ]
        if tables:
            return tables[:-1]
        return None

    @staticmethod
    def __get_one_table(html_table):
        linhas = [
            l[l.find("<tr>") + 4 :].replace("\n", "") for l in html_table.split("</tr>")
        ][:-1]
        columns = None
        rows = None

        if len(linhas) > 0:
            columns = [
                t.replace("<td>", "").replace("</td>", "")
                for t in linhas[0].split("</td><td>")
            ]

        if len(linhas) > 1:
            rows = [
                [
                    DataFrame.__remove_tags(l.replace("<td>", "").replace("</td>", ""))
                    for l in t.split("</td><td>")
                ]
                for t in linhas[1:]
            ]

        return columns, rows

    @staticmethod
    def __remove_tags(text: str) -> str:
        return re.sub(r'<(?:"[^"]*"[\'"]*|\'[^\']*\'[\'"]*|[^\'">])+>', "", text)

    @staticmethod
    def __remove_tabs_ans_newlines(text: str) -> str:
        return text.replace("\n", "").replace("\t", "")


def create_base_etl_doc(df) -> str:

    columns = ["Name", "Description"]
    indexes = [0, 1]
    tabelas = [
        dict(zip(columns, [c for i, c in enumerate(l) if i in indexes]))
        for l in df.rows
    ]

    texto = ""

    texto = "\n\n".join(
        [
            f"**[`{t.get('Name')}`](dummy_link):** {t.get('Description')}"
            for t in tabelas
        ]
    )
    return texto + "\n\n"


def md_title(text: str, level: int = 1, nl=""):
    if not str(level).isnumeric():
        level = 1
    level = 1 if level < 1 else level
    level = 7 if level > 7 else level

    return "".join(["#" for _ in range(level)]) + " " + text + nl


def create_doc(base_file, dest_file_path):
    documentation = {}

    # HTML
    html = ""
    with open(base_file, "r", encoding="utf-8") as f:
        html = f.read()

    # primeiramente pegamos só o que está dentro de body
    find = re.findall(r"<body[^>]*>((.|[\n\r])*)<\/body>", html)
    body = ""

    if len(find) > 0:
        body = re.findall(r"<body[^>]*>((.|[\n\r])*)<\/body>", html)[0][0]

    # removida a tag de scripts
    body = re.sub(pattern=r"<script>+((.|[\n\r])*)+<\/script>", string=body, repl="")

    body = body.replace("<th>", "<td>").replace("</th>", "</td>")

    # Informações Básicas
    temp = body.split("</h2>")[1]
    temp = temp[temp.find("File: ") + 6 :]
    full_file_name = temp[: temp.find("</")]
    file_name = full_file_name[: full_file_name.find(".pbix")]

    documentation["full_file_name"] = full_file_name
    documentation["file_name"] = file_name

    temp = body.split("</h2>")[2]
    temp = temp[temp.find("Path: ") + 6 :]
    file_path = temp[: temp.find("</")]

    documentation["file_path"] = file_path

    # # Partes
    # parts = body.split("<hr>")

    # Tabelas

    partes_iniciais = body[: body.find("******   Model    ******")]

    parts_table = [p for p in partes_iniciais.split("<hr>") if "<table" in p]

    initial = []

    for p in parts_table:

        # Pego todos os títulos encontrados para poder agrupar algum caso necessario
        find_title = re.findall(
            r"(<h1>|<h2>|<h3>)+<div>(.*?)<\/div>+(<\/h1>|<\/h2>|<\/h3>)", p
        )

        if find_title is not None:

            if str(find_title[0][1]).startswith("Visuals in "):

                title = "Visuals"

                visuals_in = {}

                for subtab in [f"{t}</table>" for t in p.split("</table>")]:
                    subtitle = re.findall(
                        r"(<h1>|<h2>|<h3>)+<div>(.*?)<\/div>+(<\/h1>|<\/h2>|<\/h3>)",
                        subtab,
                    )

                    if subtitle:
                        title = subtitle[0][1]
                        table = DataFrame.from_html(subtab)
                        initial.append({"title": title, "table": table})
            else:
                title = find_title[0][1]
                table = DataFrame.from_html(p)
                initial.append({"title": title, "table": table})

    # Separar as partes:
    # List of pages (tabela única)
    nome = "List of Pages:"

    temp = (
        None
        if [p for p in initial if p.get("title") == nome] is None
        else [p for p in initial if p.get("title") == nome][0]
    )

    tables = {t.get("title"): t.get("table") for t in initial}

    documentation["page_list"] = tables.get("List of Pages:")

    # Visuals in <Page> (uma tabela por página)
    documentation["visuals_per_page"] = [
        t for t in initial if str(t.get("title")).startswith("Visuals in")
    ]

    # List of all Columns/Fields/Measures/Expressions Used in Visuals: (única)
    documentation["columns_fields_measures_expressions"] = tables.get(
        "List of all Columns/Fields/Measures/Expressions Used in Visuals:"
    )

    # List of Tables Used in Visuals: (única)
    documentation["tables_used"] = tables.get("List of Tables Used in Visuals:")

    # List of Columns Not Used in Visuals: Única
    documentation["columns_not_used"] = tables.get(
        "List of Columns Not Used in Visuals:"
    )

    # partes Finais
    partes_finais = body[body.find("******   Model    ******") :].split("<hr>")
    model_name = partes_finais[0]
    model_name = model_name[model_name.find("Model: ") + 7 :]
    model_name = model_name[: model_name.find("</div>")]

    documentation["model_name"] = model_name

    parts_table = [p for p in partes_finais if "<table" in p]

    final_tables = []

    for p in parts_table:

        # Pego todos os títulos encontrados para poder agrupar algum caso necessario
        find_title = re.findall(
            r"(<h1>|<h2>|<h3>)+<div>(.*?)<\/div>+(<\/h1>|<\/h2>|<\/h3>)", p
        )

        if find_title is not None:
            title = find_title[0][1]
            table = DataFrame.from_html(p)
            final_tables.append({"title": title, "table": table})

    # Scripts

    scripts = [c for c in partes_finais if "M (Power Query) Script" in c][0]
    scripts = scripts.split("----------------------")
    scripts[0] = scripts[0][
        scripts[0].find("M (Power Query) Script:</div></h2>") + 34 :
    ]

    power_query = []

    for c in scripts:

        base = [
            re.sub(r'<(?:"[^"]*"[\'"]*|\'[^\']*\'[\'"]*|[^\'">])+>', "", c).strip()
            for c in c.split("<br></br>")
            if c != ""
        ]

        if len(base) < 2:
            continue

        title = base[0]

        code = base[1]
        if code == "let":
            code = "\n".join(base[1:])

        power_query.append({"title": title, "code": code})

    tabelas = {
        t.get("title"): t.get("table")
        for t in final_tables
        if not t.get("title", "").startswith("List of Columns for Table ")
    }

    list_of_table_columns = [
        t
        for t in [
            t
            for t in final_tables
            if t.get("title", "").startswith("List of Columns for Table ")
        ]
    ]

    # List of Tables: - única
    documentation["tables_list"] = tabelas.get("List of Tables:")

    # List of Measures: - única
    documentation["measures_list"] = tabelas.get("List of Measures:")

    # List of Columns for Table <table>: - Uma por tabela
    documentation["columns_in_tables"] = list_of_table_columns

    # List of Roles:única
    documentation["roles"] = tabelas.get("List of Roles:")

    # Relationships: única
    documentation["relashionship"] = tabelas.get("Relationships:")

    documentation["partitions"] = tabelas.get("Partitions:")

    documentation["power_queries"] = power_query

    file = f"{filePath}\\{documentation.get('file_name')}.md"

    with open(file, "w", encoding="utf-8") as f:
        f.write(
            md_title(
                f"Documentação Power BI - {documentation.get('file_name')}", nl="\n"
            )
        )

        f.write(f"**Data:** *{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*\n\n")

        f.write(f"**Nome do arquivo:** *{documentation.get('full_file_name')}*\n\n")

        f.write(f"**Caminho do arquivo .pbix:** *{documentation.get('file_path')}*\n\n")

        f.write(f"---\n\n")

        f.write(md_title("Lista de páginas:", 2, "\n\n"))

        f.write(documentation.get("page_list").to_md("\n\n"))

        f.write(f"---\n\n")

        f.write(md_title("Lista de visuais por relatório:", 2, "\n\n"))

        for v in documentation.get("visuals_per_page"):
            f.write(md_title(v.get("title"), 3, "\n\n"))
            f.write(v.get("table").to_md("\n\n"))
            f.write("\n\n")

        f.write(f"---\n\n")

        f.write(
            md_title(
                "Lista de todas as Colunas/Campos/Medidas/Expressões usadas nos visuais:",
                2,
                "\n\n",
            )
        )

        f.write(documentation.get("columns_fields_measures_expressions").to_md("\n\n"))

        f.write(f"---\n\n")

        f.write(md_title("Lista das Tabelas usadas nos visuais:", 2, "\n\n"))

        f.write(documentation.get("tables_used").to_md("\n\n"))

        f.write(f"---\n\n")

        f.write(md_title("Lista das Colunas NÃO usadas nos visuais:", 2, "\n\n"))

        f.write(documentation.get("columns_not_used").to_md("\n\n"))

        f.write(f"---\n\n")

        f.write(md_title("Modelo:", 2, "\n\n"))

        f.write(md_title(f"Modelo: {documentation.get('model_name')}", 2, "\n\n"))

        f.write(f"---\n\n")

        f.write(md_title("Lista de Tabelas:", 2, "\n\n"))

        f.write(documentation.get("tables_list").to_md("\n\n"))

        f.write(f"---\n\n")

        f.write(md_title("Arquivos de ETL:", 2, "\n\n"))

        f.write(create_base_etl_doc(documentation.get("tables_list")))

        f.write(f"---\n\n")

        f.write(md_title("Lista de Medidas:", 2, "\n\n"))

        f.write(documentation.get("measures_list").to_md("\n\n"))

        f.write(f"---\n\n")

        f.write(md_title("Lista de Colunas por Tabela:", 2, "\n\n"))

        for v in documentation.get("columns_in_tables"):
            f.write(md_title(v.get("title"), 3, ":\n\n"))
            f.write(v.get("table").to_md("\n\n"))

        f.write(f"---\n\n")

        f.write(md_title("Lista de Funções (Segurança):", 2, "\n\n"))

        f.write(documentation.get("roles").to_md("\n\n"))

        f.write(f"---\n\n")

        f.write(md_title("Lista de Relacionamentos:", 2, "\n\n"))

        f.write(documentation.get("relashionship").to_md("\n\n"))

        f.write(f"---\n\n")

        f.write(md_title("Lista de Partições:", 2, "\n\n"))

        f.write(documentation.get("partitions").to_md("\n\n"))

        f.write(f"---\n\n")

        f.write(f"## Power Query:\n\n")

        for v in documentation.get("power_queries"):
            f.write(f"### {v.get('title')}:\n\n")
            code = v.get("code").replace("\n", "\n>\n>")
            f.write(f">{code}\n\n")


path = " ".join(sys.argv[1:])
filePath = "\\".join(path.split("\\")[:-1])


arquivos = [f for f in listdir(filePath) if f.endswith(".htm") or f.endswith(".html")]

if len(arquivos) == 0:
    print("Sem arquivos")
    exit()

for f in arquivos:
    arquivo = arquivos[0]
    arquivo = f"{filePath}\\{arquivo}"

    try:
        create_doc(f, filePath)
    except Exception as ex:
        print(ex)
        sleep(5)
        with open(filePath, "w") as f:
            f.write(f"# Erro ao criar Documentação.\n\n## Erro Python: {ex}")
