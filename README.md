<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=00494c&height=120&section=header"/>

# Processamento da Lei nº 14.133/2021 e Geração de Índice Unitário

## ❯ Descrição

Este projeto realiza a extração, processamento e estruturação da **Lei nº 14.133 de 1º de abril de 2021** (a nova Lei de Licitações e Contratos Administrativos do Brasil) a partir de um arquivo PDF.

O fluxo de trabalho consiste em extrair o texto completo da lei, segmentá-lo de forma inteligente em artigos e, por fim, salvar esses artigos em um arquivo JSON estruturado. O resultado é um índice de fácil consumo para futuras aplicações, como sistemas de busca, análise de dados ou alimentação de modelos de linguagem (LLMs).

O projeto foi desenvolvido como parte do desafio da empresa Ágape.

## ❯ Estrutura do Projeto

```
agape-desafio/
│
│
├── function/
│   ├── chuckDiv.py       # Contém a função para segmentar o texto
│   ├── CreateJson.py     # Contém a função para criar o arquivo JSON
│   └── extractFile.py    # Contém a função para extrair texto do PDF
│
├── pdf/
│   └── LEI Nº 14.133, DE 1º DE ABRIL DE 2021 - ... .pdf   
│
├── main.py               # Orquestra a execução do processo
├── requirements.txt      # Lista de dependências do projeto
└── README.md
```

## ❯ Tecnologias

| Módulo/Biblioteca                                      | Função | Propósito                                                                                                                               |
| ------------------------------------------------------ | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| `pdfminer.six`                                         | `extractPdfFile`   | Utilizada no módulo `extractFile` para a extração de texto de alta performance diretamente do arquivo `.pdf` da lei.               |
| `langchain`                                            | `chunkLoad`        | Usada no módulo `chuckDiv`, emprega `RecursiveCharacterTextSplitter` para dividir o texto da lei em artigos (chunks) de forma coesa. |
| `json`                                                 | `createJSONArt`    | Usada no módulo `createJSONArt`, é responsável por serializar a lista de artigos em um arquivo `JSON` bem formatado.              |

## ❯ Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/RaphaelSimoesGomes/agape-desafio.git](https://github.com/RaphaelSimoesGomes/agape-desafio.git)
    cd agape-desafio
    ```

2. **Instale as dependências a partir do arquivo `requirements.txt`:**
    ```bash
    pip install -r requirements.txt
    ```

## ❯ Como Usar

1.  **Verifique o PDF**: Certifique-se de que o arquivo `LEI Nº 14.133, DE 1º DE ABRIL DE 2021 - Lei de Licitações e Contratos Administrativos.pdf` está dentro da pasta `pdf/`.

2.  **Execute o script principal**: Na pasta raiz do projeto, execute o seguinte comando no seu terminal:
    ```bash
    python main.py
    ```

3.  **Verifique a Saída**: Após a execução, um novo arquivo chamado `Artigos extraidos.json` será criado na raiz do projeto. O terminal exibirá uma mensagem de sucesso ou informará sobre qualquer erro que possa ter ocorrido.

## ❯ Estrutura do JSON de Saída

O arquivo JSON gerado conterá uma lista de objetos, onde cada objeto representa uma unidade da lei, facilitando sua manipulação:

```json
    "Art. 2º": {
        "caput": [
            "..................................................................................................................\n\n........................................................................................................................................."
        ],
        "II": [
            "concessão de serviço público: a delegação de sua prestação, feita pelo poder concedente,\n\nmediante licitação, na modalidade concorrência ou diálogo competitivo, a pessoa jurídica ou consórcio de\n\nempresas  que  demonstre  capacidade  para  seu  desempenho,  por  sua  conta  e  risco  e  por  prazo\n\ndeterminado;"
        ],
        "III": [
            "concessão de serviço público precedida da execução de obra pública: a construção, total ou\n\nparcial,  conservação,  reforma,  ampliação  ou  melhoramento  de  quaisquer  obras  de  interesse  público,\n\ndelegados  pelo  poder  concedente,  mediante  licitação,  na  modalidade  concorrência  ou  diálogo\n\ncompetitivo, a pessoa jurídica ou consórcio de empresas que demonstre capacidade para a sua realização,",
            "por  sua  conta  e  risco,  de  forma  que  o  investimento  da  concessionária  seja  remunerado  e  amortizado\n\nmediante a exploração do serviço ou da obra por prazo determinado;\n\n..............................................................................................................................\" (NR)"
        ]
    },
    "Art. 3º": {
        "caput": [
            "Não se subordinam ao regime desta Lei:"
        ],
        "I": [
            "contratos que tenham por objeto operação de crédito, interno ou externo, e gestão de dívida\n\npública,  incluídas  as  contratações  de  agente  ﬁnanceiro  e  a  concessão  de  garantia  relacionadas  a  esses\ncontratos;"
        ],
        "II": [
            "contratações sujeitas a normas previstas em legislação própria."
        ]
    },
    "Art. 4º": {
        "caput": [
            "Aplicam-se às licitações e contratos disciplinados por esta Lei as disposições constantes\n\ndos arts. 42 a 49 da Lei Complementar nº 123, de 14 de dezembro de 2006."
        ],
        "§ 1º": [
            "e 2º deste artigo.\n\nCAPÍTULO II\n\nDOS PRINCÍPIOS"
        ],
        "I": [
            "no  caso  de  licitação  para  aquisição  de  bens  ou  contratação  de  serviços  em  geral,  ao  item\ncujo  valor  estimado  for  superior  à  receita  bruta  máxima  admitida  para  ﬁns  de  enquadramento  como\nempresa de pequeno porte;"
        ],
        "II": [
            "no caso de contratação de obras e serviços de engenharia, às licitações cujo valor estimado\nfor  superior  à  receita  bruta  máxima  admitida  para  ﬁns  de  enquadramento  como  empresa  de  pequeno\n\nporte."
        ],
        "§  2º": [
            "A  obtenção  de  benefícios  a  que  se  refere  ocaputdeste  artigo  ﬁca  limitada  às\n\nmicroempresas e às empresas de pequeno porte que, no ano-calendário de realização da licitação, ainda\nnão tenham celebrado contratos com a Administração Pública cujos valores somados extrapolem a receita\nbruta máxima admitida para ﬁns de enquadramento como empresa de pequeno porte, devendo o órgão\nou entidade exigir do licitante declaração de observância desse limite na licitação."
        ],
        "§  3º": [
            "Nas  contratações  com  prazo  de  vigência  superior  a  1  (um)  ano,  será  considerado  o  valor\n\nanual do contrato na aplicação dos limites previstos nos §"
        ]
    }
```
<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=00494c&height=120&section=footer"/>
