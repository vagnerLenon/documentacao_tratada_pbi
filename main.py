import re
import sys
import time
from datetime import datetime
from os import listdir, path

import pandas as pd


def get_section_table(lista, title_key, title, table_key) -> pd.DataFrame:

    temp = (
        None
        if [p for p in lista if p.get(title_key) == title] is None
        else [p for p in lista if p.get(title_key) == title][0]
    )

    if temp is None:
        return None

    return temp.get(table_key)


def get_multiple_tables_in(list, title_key, table_key, prefix, new_prefix) -> list:

    new_list = [c for c in list if c.get(title_key).startswith(prefix)]

    if len(new_list) > 0:
        return [
            {
                title_key: f"{new_prefix}{c.get(title_key).replace(prefix, '')[:-1]}",
                table_key: c.get(table_key),
            }
            for c in new_list
        ]

    return None


def convert_to_md_table(df: pd.DataFrame) -> str:
    colunas = df.columns.tolist()

    texto = f"|{'|'.join(colunas)}|\n"
    texto += f"|{'|'.join(['---' for _ in range(len(colunas))])}|\n"

    for col in colunas:
        df[col] = df[col].fillna("")

    for _, l in df.iterrows():

        texto += f"|{'|'.join([str(l[c]) for c in colunas])}|\n"

    return texto


def create_base_etl_doc(df: pd.DataFrame) -> str:

    dados = df[["Name", "Description"]].to_dict("records")
    texto = "\n\n".join(
        [f"**[`{t.get('Name')}`](dummy_link):** {t.get('Description')}" for t in dados]
    )
    texto = texto + "\n\n"
    return texto


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
        find_title = re.findall(
            r"(<h1>|<h2>|<h3>)+<div>(.*?)<\/div>+(<\/h1>|<\/h2>|<\/h3>)", p
        )
        find_table = re.search(r"<table[\s\S]*<\/table>", p)

        if find_title:

            if str(find_title[0][1]).startswith("Visuals in "):
                for tab in [f"{t}</table>" for t in p.split("</table>")]:
                    find_title = re.findall(
                        r"(<h1>|<h2>|<h3>)+<div>(.*?)<\/div>+(<\/h1>|<\/h2>|<\/h3>)",
                        tab,
                    )
                    find_table = re.search(r"<table[\s\S]*<\/table>", tab)

                    if find_table:
                        title = find_title[0][1]
                        table = find_table[0] if find_table else None

                        table_df = pd.read_html(table)[0] if table else None

                        if len(table_df) > 0:

                            table_df.columns = table_df.iloc[0]
                            table_df = table_df.iloc[1:].copy().reset_index(drop=True)

                        initial.append({"title": title, "table": table_df})
            else:

                title = find_title[0][1]
                table = find_table[0] if find_table else None

                table_df = pd.read_html(table)[0] if table else None

                if len(table_df) > 0:

                    table_df.columns = table_df.iloc[0]
                    table_df = table_df.iloc[1:].copy().reset_index(drop=True)

                initial.append({"title": title, "table": table_df})

    # Separar as partes:
    # List of pages (tabela única)
    nome = "List of Pages:"

    temp = (
        None
        if [p for p in initial if p.get("title") == nome] is None
        else [p for p in initial if p.get("title") == nome][0]
    )

    documentation["page_list"] = get_section_table(
        initial, "title", "List of Pages:", "table"
    )

    # Visuals in <Page> (uma tabela por página)
    documentation["visuals_per_page"] = get_multiple_tables_in(
        initial, "title", "table", "Visuals in ", "Visuais em "
    )

    # List of all Columns/Fields/Measures/Expressions Used in Visuals: (única)
    documentation["columns_fields_measures_expressions"] = get_section_table(
        initial,
        "title",
        "List of all Columns/Fields/Measures/Expressions Used in Visuals:",
        "table",
    )

    # List of Tables Used in Visuals: (única)
    documentation["tables_used"] = get_section_table(
        initial, "title", "List of Tables Used in Visuals:", "table"
    )

    # List of Columns Not Used in Visuals: Única
    documentation["columns_not_used"] = get_section_table(
        initial, "title", "List of Columns Not Used in Visuals:", "table"
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
        find_title = re.findall(
            r"(<h1>|<h2>|<h3>)+<div>(.*?)<\/div>+(<\/h1>|<\/h2>|<\/h3>)", p
        )
        find_table = re.search(r"<table[\s\S]*<\/table>", p)

        if find_title:
            title = find_title[0][1]
            table = find_table[0] if find_table else None

            table_df = pd.read_html(table)[0] if table else None

            if table_df is not None:
                if len(table_df) > 0:
                    table_df.columns = table_df.iloc[0]
                    table_df = table_df.iloc[1:].copy().reset_index(drop=True)

            final_tables.append({"title": title, "table": table_df})

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

        # List of Tables: - única
    documentation["tables_list"] = get_section_table(
        final_tables, "title", "List of Tables:", "table"
    )

    # List of Measures: - única
    documentation["measures_list"] = get_section_table(
        final_tables, "title", "List of Measures:", "table"
    )

    # List of Columns for Table <table>: - Uma por tabela
    documentation["columns_in_tables"] = get_multiple_tables_in(
        final_tables,
        "title",
        "table",
        "List of Columns for Table ",
        "Lista de colunas na tabela ",
    )

    # List of Roles:única
    documentation["roles"] = get_section_table(
        final_tables, "title", "List of Roles:", "table"
    )

    # Relationships: única
    documentation["relashionship"] = get_section_table(
        final_tables, "title", "Relationships:", "table"
    )

    documentation["power_queries"] = power_query

    # Criar Documento
    file = f"{dest_file_path}\\{documentation.get('file_name')}.md"

    with open(file, "w", encoding="utf-8") as f:
        f.write(f"# Documentação Power BI - {documentation.get('file_name')}\n")
        f.write(f"**Data:** *{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*\n\n")

        f.write(f"**Nome do arquivo:** *{documentation.get('full_file_name')}*\n\n")
        f.write(f"**Caminho do arquivo .pbix:** *{documentation.get('file_path')}*\n\n")

        f.write(f"---\n\n")

        f.write(f"## Lista de páginas:\n\n")

        f.write(convert_to_md_table(documentation.get("page_list")))

        f.write(f"---\n\n")

        f.write(f"## Lista de visuais por relatório:\n\n")

        for v in documentation.get("visuals_per_page"):
            f.write(f"### {v.get('title')}:\n\n")
            f.write(convert_to_md_table(v.get("table")))

        f.write(f"---\n\n")

        f.write(
            f"## Lista de todas as Colunas/Campos/Medidas/Expressões usadas nos visuais:\n\n"
        )

        f.write(
            convert_to_md_table(
                documentation.get("columns_fields_measures_expressions")
            )
        )

        f.write(f"---\n\n")

        f.write(f"## Lista das Tabelas usadas nos visuais:\n\n")

        f.write(convert_to_md_table(documentation.get("tables_used")))

        f.write(f"---\n\n")

        f.write(f"## Lista das Colunas NÃO usadas nos visuais:\n\n")

        f.write(convert_to_md_table(documentation.get("columns_not_used")))

        f.write(f"---\n\n")

        f.write(f"## Modelo:\n\n")

        f.write(f"## Modelo: {documentation.get('model_name')}\n\n")

        f.write(f"---\n\n")

        f.write(f"## Lista de Tabelas:\n\n")

        f.write(convert_to_md_table(documentation.get("tables_list")))

        f.write(f"---\n\n")

        f.write(f"## Arquivos de ETL:\n\n")

        f.write(create_base_etl_doc(documentation.get("tables_list")))

        f.write(f"---\n\n")

        f.write(f"## Lista de Medidas:\n\n")

        f.write(convert_to_md_table(documentation.get("measures_list")))

        f.write(f"---\n\n")

        f.write(f"## Lista de Colunas por tabela:\n\n")

        for v in documentation.get("columns_in_tables"):
            f.write(f"### {v.get('title')}:\n\n")
            f.write(convert_to_md_table(v.get("table")))

        f.write(f"---\n\n")

        f.write(f"## Lista de Funções (Roles):\n\n")

        f.write(convert_to_md_table(documentation.get("roles")))

        f.write(f"---\n\n")

        f.write(f"## Lista de Relacionamentos:\n\n")

        f.write(convert_to_md_table(documentation.get("relashionship")))

        f.write(f"---\n\n")

        f.write(f"## Power Query:\n\n")

        for v in documentation.get("power_queries"):
            f.write(f"### {v.get('title')}:\n\n")
            code = v.get("code").replace("\n", "\n>\n>")
            f.write(f">{code}\n\n")


# print("\\".join(" ".join(sys.argv[1:])).split("\\")[:-1])
path = " ".join(sys.argv[1:])
filePath = "\\".join(path.split("\\")[:-1])


arquivos = [f for f in listdir(filePath) if f.endswith(".htm") or f.endswith(".html")]

if len(arquivos) == 0:
    print("Sem arquivos")
    exit()

for f in arquivos:
    arquivo = arquivos[0]
    arquivo = f"{filePath}\\{arquivo}"

    create_doc(f, filePath)
