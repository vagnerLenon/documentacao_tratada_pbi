# Documentação Power BI - Teste
**Data:** *05/11/2022 21:47:01*

**Nome do arquivo:** *Teste.pbix*

**Caminho do arquivo .pbix:** *I:\03.DADOPAR\ADMINISTRATIVO\BI\VAGNER\POWER BI\ONLINE\GERAL TÁTICO\TESTE\Teste.pbix*

---

## Lista de páginas:

|DisplayName|Name|Ordinal|DisplayOption|Width|Height|PageIndex|
|---|---|---|---|---|---|---|
|Relatório|ReportSection0cb5c72216055c874994|0|1|1920|1080|0|
---

## Lista de visuais por relatório:

### Visuais em Relatório:

|Visual Type|Title|X|Y|Z|Width|Height|Name|tabOrder|VisualIndex|PageIndex|
|---|---|---|---|---|---|---|---|---|---|---|
|ChicletSlicer1448559807354||853|17|0|520|92|0963b4180f2751e539d3||0|0|
|ChicletSlicer1448559807354||1386|17|1000|520|92|44e7bfb3d0d179fd3e76||1|0|
|tableEx||103783783783784|126023166023166|2000|189627799227799|941467181467181|1dc597226ac5ffc560e2||2|0|
|ChicletSlicer1448559807354||103783783783784|163088803088803|3000|83027027027027|919227799227799|6256aeead0646d6e7d56||3|0|
---

## Lista de todas as Colunas/Campos/Medidas/Expressões usadas nos visuais:

|Name|Table Name|Aggregation|Expression|VisualIndex|PageIndex|
|---|---|---|---|---|---|
|Year|||MOVIMENTOS.DATA_MOVIMENTO.Variation.Date Hierarchy.Year|0|0|
|MES_RED|Meses||Meses.MES_RED|1|0|
|MOVIMENTO|MOVIMENTOS|Sum|Sum(MOVIMENTOS.MOVIMENTO)|2|0|
|CFOP|MOVIMENTOS||MOVIMENTOS.CFOP|2|0|
|CD_TP_OPERACAO|MOVIMENTOS||MOVIMENTOS.CD_TP_OPERACAO|2|0|
|TIPO_OPERACAO|MOVIMENTOS||MOVIMENTOS.TIPO_OPERACAO|2|0|
|CONFIG_LABEL|MOVIMENTOS||MOVIMENTOS.CONFIG_LABEL|2|0|
|CONFIG_LOCAL|MOVIMENTOS||MOVIMENTOS.CONFIG_LOCAL|2|0|
|DATA_MOVIMENTO|MOVIMENTOS||MOVIMENTOS.DATA_MOVIMENTO|2|0|
|DATA_ORIGINAL|MOVIMENTOS||MOVIMENTOS.DATA_ORIGINAL|2|0|
|SERIE|MOVIMENTOS||MOVIMENTOS.SERIE|2|0|
|NF|MOVIMENTOS|Sum|Sum(MOVIMENTOS.NF)|2|0|
|SEQ_NOTA|MOVIMENTOS|Sum|Sum(MOVIMENTOS.SEQ_NOTA)|2|0|
|NF_REFERENCIA|MOVIMENTOS|Sum|Sum(MOVIMENTOS.NF_REFERENCIA)|2|0|
|CD_VENDEDOR_NF|MOVIMENTOS||MOVIMENTOS.CD_VENDEDOR_NF|2|0|
|VENDEDOR|MOVIMENTOS||MOVIMENTOS.VENDEDOR|2|0|
|NOME_COMPLETO_VENDEDOR|MOVIMENTOS||MOVIMENTOS.NOME_COMPLETO_VENDEDOR|2|0|
|CD_MATERIAL|MOVIMENTOS||MOVIMENTOS.CD_MATERIAL|2|0|
|NOME_MATERIAL|MOVIMENTOS||MOVIMENTOS.NOME_MATERIAL|2|0|
|UNI_MED|MOVIMENTOS||MOVIMENTOS.UNI_MED|2|0|
|LINHA|MOVIMENTOS||MOVIMENTOS.LINHA|2|0|
|CD_GRUPO|MOVIMENTOS||MOVIMENTOS.CD_GRUPO|2|0|
|DESC_GRUPO|MOVIMENTOS||MOVIMENTOS.DESC_GRUPO|2|0|
|CD_SUB_GRUPO|MOVIMENTOS||MOVIMENTOS.CD_SUB_GRUPO|2|0|
|DESC_SUB_GRUPO|MOVIMENTOS||MOVIMENTOS.DESC_SUB_GRUPO|2|0|
|VOLUME_UNITARIO|MOVIMENTOS|Sum|Sum(MOVIMENTOS.VOLUME_UNITARIO)|2|0|
|PESO_EMBALAGEM_UNIT|MOVIMENTOS|Sum|Sum(MOVIMENTOS.PESO_EMBALAGEM_UNIT)|2|0|
|PESO_TOTAL|MOVIMENTOS|Sum|Sum(MOVIMENTOS.PESO_TOTAL)|2|0|
|CD_CLIENTE|MOVIMENTOS||MOVIMENTOS.CD_CLIENTE|2|0|
|FANTASIA_CLIENTE|MOVIMENTOS||MOVIMENTOS.FANTASIA_CLIENTE|2|0|
|NOME_COMPLETO_CLIENTE|MOVIMENTOS||MOVIMENTOS.NOME_COMPLETO_CLIENTE|2|0|
|UF_CLIENTE|MOVIMENTOS||MOVIMENTOS.UF_CLIENTE|2|0|
|MUNICIPIO_CLIENTE|MOVIMENTOS||MOVIMENTOS.MUNICIPIO_CLIENTE|2|0|
|CD_ROTA|MOVIMENTOS||MOVIMENTOS.CD_ROTA|2|0|
|ROTA|MOVIMENTOS||MOVIMENTOS.ROTA|2|0|
|VOLUME|MOVIMENTOS|Sum|Sum(MOVIMENTOS.VOLUME)|2|0|
|QUANTIDADE|MOVIMENTOS|Sum|Sum(MOVIMENTOS.QUANTIDADE)|2|0|
|PR_TOTAL_ITEM|MOVIMENTOS|Sum|Sum(MOVIMENTOS.PR_TOTAL_ITEM)|2|0|
|RECEITA_BRUTA|MOVIMENTOS|Sum|Sum(MOVIMENTOS.RECEITA_BRUTA)|2|0|
|VL_ICMS|MOVIMENTOS|Sum|Sum(MOVIMENTOS.VL_ICMS)|2|0|
|VL_SUBSTITUICAO|MOVIMENTOS|Sum|Sum(MOVIMENTOS.VL_SUBSTITUICAO)|2|0|
|FCP|MOVIMENTOS|Sum|Sum(MOVIMENTOS.FCP)|2|0|
|VL_IPI|MOVIMENTOS|Sum|Sum(MOVIMENTOS.VL_IPI)|2|0|
|PIS|MOVIMENTOS|Sum|Sum(MOVIMENTOS.PIS)|2|0|
|COFINS|MOVIMENTOS|Sum|Sum(MOVIMENTOS.COFINS)|2|0|
|RECEITA_LIQUIDA|MOVIMENTOS|Sum|Sum(MOVIMENTOS.RECEITA_LIQUIDA)|2|0|
|CD_CONDICAO_PAG|MOVIMENTOS||MOVIMENTOS.CD_CONDICAO_PAG|2|0|
|NOME_COND_PAGTO|MOVIMENTOS||MOVIMENTOS.NOME_COND_PAGTO|2|0|
|CD_TIPO_DE_PAGA|MOVIMENTOS||MOVIMENTOS.CD_TIPO_DE_PAGA|2|0|
|NOME_TIPO_PAGAMENTO|MOVIMENTOS||MOVIMENTOS.NOME_TIPO_PAGAMENTO|2|0|
|PARCELAS|MOVIMENTOS||MOVIMENTOS.PARCELAS|2|0|
|NUMERO_DE_VEZES|MOVIMENTOS|Sum|Sum(MOVIMENTOS.NUMERO_DE_VEZES)|2|0|
|GGF_LITRO|MOVIMENTOS|Sum|Sum(MOVIMENTOS.GGF_LITRO)|2|0|
|PR_TOTAL_CUSTO|MOVIMENTOS|Sum|Sum(MOVIMENTOS.PR_TOTAL_CUSTO)|2|0|
|TOTAL_GGF|MOVIMENTOS|Sum|Sum(MOVIMENTOS.TOTAL_GGF)|2|0|
|CPV|MOVIMENTOS|Sum|Sum(MOVIMENTOS.CPV)|2|0|
|CONFIG_LABEL|MOVIMENTOS||MOVIMENTOS.CONFIG_LABEL|3|0|
---

## Lista das Tabelas usadas nos visuais:

|Name|
|---|
|MOVIMENTOS|
|LocalDateTable_4517c509-c3e1-42ae-9c3b-7646609659c3|
|Meses|
---

## Lista das Colunas NÃO usadas nos visuais:

|Name|Table Name|State|Data Category|Data Type|Description|Display Folder|Error Message|Format String|Is Hidden|Modified Time|Structure Modified Time|Sort by Column|Summarize By|Type|Expression|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|SERIE_REFERENCIA|MOVIMENTOS|||||||||||||COLUMN||
|MATERIAL|MOVIMENTOS|||||||||||||COLUMN||
|MODALIDADE|MOVIMENTOS|||||||||||||COLUMN||
|CONFIG_NOME_GRUPO|MOVIMENTOS|||||||||||||COLUMN||
|VOLUME_ABS|MOVIMENTOS|||||||||||||COLUMN||
|RECEITA_BRUTA_ABS|MOVIMENTOS|||||||||||||COLUMN||
|PRAZO_MEDIO|MOVIMENTOS|||||||||||||COLUMN||
|UNI_NEG|MOVIMENTOS|||||||||||||COLUMN||
|Mês|MOVIMENTOS|||||||||||||COLUMN||
|MES|Meses|||||||||||||COLUMN||
|NOME_MES|Meses|||||||||||||COLUMN||
---

## Modelo:

## Modelo: Teste

---

## Lista de Tabelas:

|Name|Description|Storage Mode|Source|Is Hidden|
|---|---|---|---|---|
|DateTableTemplate_5711c55f-3f3b-4291-a7b7-5c3b6577416b||Import|Calendar(Date(2015,1,1), Date(2015,1,1))|True|
|MOVIMENTOS||Import|let  Fonte = Sql.Database("192.168.1.249\DADOBIER_BI", "DADOBIER_ETL", [Query="SELECT#(lf)#(tab)DISTINCT #(lf)#(tab)V.MOVIMENTO,#(lf)#(tab)V.CFOP,#(lf)#(tab)V.CD_TP_OPERACAO,#(lf)#(tab)TPOP.DESCRICAO AS TIPO_OPERACAO,#(lf)#(tab)V.DATA_MOVIMENTO,#(lf)#(tab)V.DATA_ORIGINAL,#(lf)#(tab)V.SERIE,#(lf)#(tab)V.NF,#(lf)#(tab)V.SEQ_NOTA,#(lf)#(tab)V.SERIE_REFERENCIA,#(lf)#(tab)V.NF_REFERENCIA,#(lf)#(tab)V.CD_VENDEDOR_NF,#(lf)#(tab)VEND.FANTASIA AS VENDEDOR,#(lf)#(tab)VEND.NOME_COMPLETO AS NOME_COMPLETO_VENDEDOR,#(lf)#(tab)V.CD_MATERIAL,#(lf)#(tab)MAT.DESCRICAO AS NOME_MATERIAL,#(lf)#(tab)MAT.APELIDO AS MATERIAL,#(lf)#(tab)MAT.CD_UNIDADE_MEDI AS UNI_MED,#(lf)#(tab)MAT.LINHA_CERVEJA AS LINHA,#(lf)#(tab)MAT.CD_GRUPO,#(lf)#(tab)MAT.DESC_GRUPO,#(lf)#(tab)MAT.CD_SUB_GRUPO,#(lf)#(tab)MAT.DESC_SUB_GRUPO,#(lf)#(tab)MAT.PESO AS VOLUME_UNITARIO,#(lf)#(tab)MAT.PESO_EMBALAGEM AS PESO_EMBALAGEM_UNIT,#(lf)#(tab)V.QUANTIDADE * MAT.PESO_EMBALAGEM + V.QUANTIDADE * MAT.PESO AS PESO_TOTAL,#(lf)#(tab)V.VOLUME,#(lf)#(tab)V.CD_CLIENTE,#(lf)#(tab)EMP.FANTASIA AS FANTASIA_CLIENTE,#(lf)#(tab)EMP.NOME_COMPLETO AS NOME_COMPLETO_CLIENTE,#(lf)#(tab)EMP.UF AS UF_CLIENTE,#(lf)#(tab)EMP.MUNICIPIO AS MUNICIPIO_CLIENTE,#(lf)#(tab)EMP.TIPO_DE_EMPRESA AS CD_ROTA,#(lf)#(tab)ROTA.DESCRICAO AS ROTA,#(lf)#(tab)V.QUANTIDADE,#(lf)#(tab)V.PR_TOTAL_ITEM,#(lf)#(tab)V.RECEITA_BRUTA,#(lf)#(tab)V.VL_ICMS,#(lf)#(tab)V.VL_SUBSTITUICAO,#(lf)#(tab)V.FCP,#(lf)#(tab)V.VL_IPI,#(lf)#(tab)V.PIS,#(lf)#(tab)V.COFINS,#(lf)#(tab)V.RECEITA_LIQUIDA,#(lf)#(tab)V.CD_CONDICAO_PAG,#(lf)#(tab)V.NOME_COND_PAGTO,#(lf)#(tab)V.CD_TIPO_DE_PAGA,#(lf)#(tab)V.NOME_TIPO_PAGAMENTO,#(lf)#(tab)V.NUMERO_DE_VEZES,#(lf)#(tab)V.MODALIDADE,#(lf)#(tab)V.GGF_LITRO,#(lf)#(tab)V.CONFIG_LABEL,#(lf)#(tab)V.CONFIG_NOME_GRUPO,#(lf)#(tab)V.CONFIG_LOCAL,#(lf)#(tab)V.VOLUME_ABS,#(lf)#(tab)V.RECEITA_BRUTA_ABS,#(lf)#(tab)V.PR_TOTAL_CUSTO,#(lf)#(tab)V.TOTAL_GGF,#(lf)#(tab)V.CPV,#(lf)#(tab)V.PARCELAS,#(lf)#(tab)V.PRAZO_MEDIO,#(lf)#(tab)V.UNI_NEG#(lf)FROM#(lf)#(tab)COMERCIAL.DBO.TB_VENDAS V#(lf)#(tab)LEFT JOIN CIGAM_AUX.DBO.GETOPERA TPOP ON TPOP.CD_TIPO_OPERACA = V.CD_TP_OPERACAO#(lf)#(tab)LEFT JOIN CIGAM_AUX.DBO.GEEMPRES VEND ON VEND.CD_EMPRESA = V.CD_VENDEDOR_NF#(lf)#(tab)LEFT JOIN CIGAM_AUX.DBO.VW_MATERIAIS MAT ON MAT.CD_MATERIAL = V.CD_MATERIAL#(lf)#(tab)LEFT JOIN CIGAM_AUX.DBO.GEEMPRES EMP ON EMP.CD_EMPRESA = V.CD_CLIENTE#(lf)#(tab)LEFT JOIN CIGAM_AUX.DBO.VETIPOEM ROTA ON ROTA.TIPO_DE_EMPRESA = EMP.TIPO_DE_EMPRESA#(lf)#(tab)WHERE V.DATA_MOVIMENTO >= '2014-01-01'", CommandTimeout=#duration(0, 0, 5, 0)]),  #"Tipo Alterado" = Table.TransformColumnTypes(Fonte,{{"DATA_MOVIMENTO", type date}, {"DATA_ORIGINAL", type date}}),  #"Duplicatas Removidas" = Table.Distinct(#"Tipo Alterado", {"MOVIMENTO"}),  #"Mês Inserido" = Table.AddColumn(#"Duplicatas Removidas", "Mês", each Date.Month([DATA_MOVIMENTO]), Int64.Type) in  #"Mês Inserido"|False|
|LocalDateTable_4517c509-c3e1-42ae-9c3b-7646609659c3||Import|Calendar(Date(Year(MIN('MOVIMENTOS'[DATA_MOVIMENTO])), 1, 1), Date(Year(MAX('MOVIMENTOS'[DATA_MOVIMENTO])), 12, 31))|True|
|LocalDateTable_594b5b4a-0dc1-4056-8188-4e6467427da5||Import|Calendar(Date(Year(MIN('MOVIMENTOS'[DATA_ORIGINAL])), 1, 1), Date(Year(MAX('MOVIMENTOS'[DATA_ORIGINAL])), 12, 31))|True|
|Meses||Import|let  Fonte = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("Nc+/CsIwEMfxd7m5g/W/oyAOBXVwDBlaODQQexCbDr6QD+KLefldO+WbT0LIOUc1VdS0PYckVuQrR0vtM4+cJteGr7Qvbfp9xQK41j52KURbYRucB7sWQNvyfu6fYitsh46TRdi+PPOQ9yAWwIP2nQd+dfiPJrhe6OaWh2ysZVymuso4X9c0L3Od+DO7Jnn/Bw==", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [MES = _t, NOME_MES = _t, MES_RED = _t]),  #"Tipo Alterado" = Table.TransformColumnTypes(Fonte,{{"MES", Int64.Type}, {"NOME_MES", type text}, {"MES_RED", type text}}) in  #"Tipo Alterado"|False|
---

## Lista de Medidas:

|Measure Name|Table Name|Description|Expression|Dependency|Reverse Dependency|
|---|---|---|---|---|---|
---

## Lista de Colunas por tabela:

### Lista de colunas na tabela MOVIMENTOS:

|Column Name|Description|Calculated Column|Expression|
|---|---|---|---|
|MOVIMENTO||||
|CFOP||||
|CD_TP_OPERACAO||||
|TIPO_OPERACAO||||
|DATA_MOVIMENTO||||
|DATA_ORIGINAL||||
|SERIE||||
|NF||||
|SEQ_NOTA||||
|SERIE_REFERENCIA||||
|NF_REFERENCIA||||
|CD_VENDEDOR_NF||||
|VENDEDOR||||
|NOME_COMPLETO_VENDEDOR||||
|CD_MATERIAL||||
|NOME_MATERIAL||||
|MATERIAL||||
|UNI_MED||||
|LINHA||||
|CD_GRUPO||||
|DESC_GRUPO||||
|CD_SUB_GRUPO||||
|DESC_SUB_GRUPO||||
|VOLUME_UNITARIO||||
|PESO_EMBALAGEM_UNIT||||
|PESO_TOTAL||||
|VOLUME||||
|CD_CLIENTE||||
|FANTASIA_CLIENTE||||
|NOME_COMPLETO_CLIENTE||||
|UF_CLIENTE||||
|MUNICIPIO_CLIENTE||||
|CD_ROTA||||
|ROTA||||
|QUANTIDADE||||
|PR_TOTAL_ITEM||||
|RECEITA_BRUTA||||
|VL_ICMS||||
|VL_SUBSTITUICAO||||
|FCP||||
|VL_IPI||||
|PIS||||
|COFINS||||
|RECEITA_LIQUIDA||||
|CD_CONDICAO_PAG||||
|NOME_COND_PAGTO||||
|CD_TIPO_DE_PAGA||||
|NOME_TIPO_PAGAMENTO||||
|NUMERO_DE_VEZES||||
|MODALIDADE||||
|GGF_LITRO||||
|CONFIG_LABEL||||
|CONFIG_NOME_GRUPO||||
|CONFIG_LOCAL||||
|VOLUME_ABS||||
|RECEITA_BRUTA_ABS||||
|PR_TOTAL_CUSTO||||
|TOTAL_GGF||||
|CPV||||
|PARCELAS||||
|PRAZO_MEDIO||||
|UNI_NEG||||
|Mês||||
### Lista de colunas na tabela Meses:

|Column Name|Description|Calculated Column|Expression|
|---|---|---|---|
|MES||||
|NOME_MES||||
|MES_RED||||
---

## Lista de Funções (Roles):

|Role Name|Table Name|Description|Expression|
|---|---|---|---|
|Vendedor|MOVIMENTOS||[CONFIG_LABEL] = "VENDA"|
---

## Lista de Relacionamentos:

|Name|CrossFilteringBehavior|FromCardinality|FromColumn|FromTable|IsActive|IsRemoved|JoinOnDateBehavior|RelyOnReferentialIntegrity|SecurityFilteringBehavior|State|ToCardinality|ToColumn|ToTable|Type|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|994749f0-08a7-4538-b7d6-197fd7249760|OneDirection|Many|DATA_MOVIMENTO|MOVIMENTOS|True|False|DatePartOnly|False|OneDirection|Ready|One|Date|LocalDateTable_4517c509-c3e1-42ae-9c3b-7646609659c3|SingleColumn|
|2424fcd0-0435-4378-89b3-7008c1f99867|OneDirection|Many|DATA_ORIGINAL|MOVIMENTOS|True|False|DatePartOnly|False|OneDirection|Ready|One|Date|LocalDateTable_594b5b4a-0dc1-4056-8188-4e6467427da5|SingleColumn|
|f2744543-33dc-4e0e-bf5a-9c8e7cced8d7|BothDirections|Many|Mês|MOVIMENTOS|True|False|DateAndTime|False|OneDirection|Ready|One|MES|Meses|SingleColumn|
---

## Power Query:

### DateTableTemplate_5711c55f-3f3b-4291-a7b7-5c3b6577416b-beddb651-157e-4cf6-ac11-83e077582cf0:

>Calendar(Date(2015,1,1), Date(2015,1,1))

### MOVIMENTOS-62c0b944-23b8-4302-ad04-36b710242104:

>let
>
>Fonte = Sql.Database("192.168.1.249\DADOBIER_BI", "DADOBIER_ETL", [Query="SELECT#(lf)#(tab)DISTINCT #(lf)#(tab)V.MOVIMENTO,#(lf)#(tab)V.CFOP,#(lf)#(tab)V.CD_TP_OPERACAO,#(lf)#(tab)TPOP.DESCRICAO AS TIPO_OPERACAO,#(lf)#(tab)V.DATA_MOVIMENTO,#(lf)#(tab)V.DATA_ORIGINAL,#(lf)#(tab)V.SERIE,#(lf)#(tab)V.NF,#(lf)#(tab)V.SEQ_NOTA,#(lf)#(tab)V.SERIE_REFERENCIA,#(lf)#(tab)V.NF_REFERENCIA,#(lf)#(tab)V.CD_VENDEDOR_NF,#(lf)#(tab)VEND.FANTASIA AS VENDEDOR,#(lf)#(tab)VEND.NOME_COMPLETO AS NOME_COMPLETO_VENDEDOR,#(lf)#(tab)V.CD_MATERIAL,#(lf)#(tab)MAT.DESCRICAO AS NOME_MATERIAL,#(lf)#(tab)MAT.APELIDO AS MATERIAL,#(lf)#(tab)MAT.CD_UNIDADE_MEDI AS UNI_MED,#(lf)#(tab)MAT.LINHA_CERVEJA AS LINHA,#(lf)#(tab)MAT.CD_GRUPO,#(lf)#(tab)MAT.DESC_GRUPO,#(lf)#(tab)MAT.CD_SUB_GRUPO,#(lf)#(tab)MAT.DESC_SUB_GRUPO,#(lf)#(tab)MAT.PESO AS VOLUME_UNITARIO,#(lf)#(tab)MAT.PESO_EMBALAGEM AS PESO_EMBALAGEM_UNIT,#(lf)#(tab)V.QUANTIDADE * MAT.PESO_EMBALAGEM + V.QUANTIDADE * MAT.PESO AS PESO_TOTAL,#(lf)#(tab)V.VOLUME,#(lf)#(tab)V.CD_CLIENTE,#(lf)#(tab)EMP.FANTASIA AS FANTASIA_CLIENTE,#(lf)#(tab)EMP.NOME_COMPLETO AS NOME_COMPLETO_CLIENTE,#(lf)#(tab)EMP.UF AS UF_CLIENTE,#(lf)#(tab)EMP.MUNICIPIO AS MUNICIPIO_CLIENTE,#(lf)#(tab)EMP.TIPO_DE_EMPRESA AS CD_ROTA,#(lf)#(tab)ROTA.DESCRICAO AS ROTA,#(lf)#(tab)V.QUANTIDADE,#(lf)#(tab)V.PR_TOTAL_ITEM,#(lf)#(tab)V.RECEITA_BRUTA,#(lf)#(tab)V.VL_ICMS,#(lf)#(tab)V.VL_SUBSTITUICAO,#(lf)#(tab)V.FCP,#(lf)#(tab)V.VL_IPI,#(lf)#(tab)V.PIS,#(lf)#(tab)V.COFINS,#(lf)#(tab)V.RECEITA_LIQUIDA,#(lf)#(tab)V.CD_CONDICAO_PAG,#(lf)#(tab)V.NOME_COND_PAGTO,#(lf)#(tab)V.CD_TIPO_DE_PAGA,#(lf)#(tab)V.NOME_TIPO_PAGAMENTO,#(lf)#(tab)V.NUMERO_DE_VEZES,#(lf)#(tab)V.MODALIDADE,#(lf)#(tab)V.GGF_LITRO,#(lf)#(tab)V.CONFIG_LABEL,#(lf)#(tab)V.CONFIG_NOME_GRUPO,#(lf)#(tab)V.CONFIG_LOCAL,#(lf)#(tab)V.VOLUME_ABS,#(lf)#(tab)V.RECEITA_BRUTA_ABS,#(lf)#(tab)V.PR_TOTAL_CUSTO,#(lf)#(tab)V.TOTAL_GGF,#(lf)#(tab)V.CPV,#(lf)#(tab)V.PARCELAS,#(lf)#(tab)V.PRAZO_MEDIO,#(lf)#(tab)V.UNI_NEG#(lf)FROM#(lf)#(tab)COMERCIAL.DBO.TB_VENDAS V#(lf)#(tab)LEFT JOIN CIGAM_AUX.DBO.GETOPERA TPOP ON TPOP.CD_TIPO_OPERACA = V.CD_TP_OPERACAO#(lf)#(tab)LEFT JOIN CIGAM_AUX.DBO.GEEMPRES VEND ON VEND.CD_EMPRESA = V.CD_VENDEDOR_NF#(lf)#(tab)LEFT JOIN CIGAM_AUX.DBO.VW_MATERIAIS MAT ON MAT.CD_MATERIAL = V.CD_MATERIAL#(lf)#(tab)LEFT JOIN CIGAM_AUX.DBO.GEEMPRES EMP ON EMP.CD_EMPRESA = V.CD_CLIENTE#(lf)#(tab)LEFT JOIN CIGAM_AUX.DBO.VETIPOEM ROTA ON ROTA.TIPO_DE_EMPRESA = EMP.TIPO_DE_EMPRESA#(lf)#(tab)WHERE V.DATA_MOVIMENTO >= '2014-01-01'", CommandTimeout=#duration(0, 0, 5, 0)]),
>
>#"Tipo Alterado" = Table.TransformColumnTypes(Fonte,{{"DATA_MOVIMENTO", type date}, {"DATA_ORIGINAL", type date}}),
>
>#"Duplicatas Removidas" = Table.Distinct(#"Tipo Alterado", {"MOVIMENTO"}),
>
>#"Mês Inserido" = Table.AddColumn(#"Duplicatas Removidas", "Mês", each Date.Month([DATA_MOVIMENTO]), Int64.Type)
>
>in
>
>#"Mês Inserido"

### LocalDateTable_4517c509-c3e1-42ae-9c3b-7646609659c3-669d3392-c075-4dd7-8faf-f621b8dcf544:

>Calendar(Date(Year(MIN('MOVIMENTOS'[DATA_MOVIMENTO])), 1, 1), Date(Year(MAX('MOVIMENTOS'[DATA_MOVIMENTO])), 12, 31))

### LocalDateTable_594b5b4a-0dc1-4056-8188-4e6467427da5-ed821328-6204-4821-b7ef-2d294ba273ca:

>Calendar(Date(Year(MIN('MOVIMENTOS'[DATA_ORIGINAL])), 1, 1), Date(Year(MAX('MOVIMENTOS'[DATA_ORIGINAL])), 12, 31))

### Meses-8b306c3a-41a8-42b1-b6e2-349ba078fe48:

>let
>
>Fonte = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("Nc+/CsIwEMfxd7m5g/W/oyAOBXVwDBlaODQQexCbDr6QD+KLefldO+WbT0LIOUc1VdS0PYckVuQrR0vtM4+cJteGr7Qvbfp9xQK41j52KURbYRucB7sWQNvyfu6fYitsh46TRdi+PPOQ9yAWwIP2nQd+dfiPJrhe6OaWh2ysZVymuso4X9c0L3Od+DO7Jnn/Bw==", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [MES = _t, NOME_MES = _t, MES_RED = _t]),
>
>#"Tipo Alterado" = Table.TransformColumnTypes(Fonte,{{"MES", Int64.Type}, {"NOME_MES", type text}, {"MES_RED", type text}})
>
>in
>
>#"Tipo Alterado"

