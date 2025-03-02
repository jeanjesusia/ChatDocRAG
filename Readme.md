# ChatDoc - RAG (Retrieval-Augmented Generation)

O ChatDoc é uma aplicação interativa que permite a análise de documentos PDF com base em uma integração com modelos de linguagem da OpenAI. Ele usa uma abordagem de **Retrieval-Augmented Generation (RAG)** para permitir que o modelo acesse informações dos documentos enviados e forneça respostas detalhadas com base no conteúdo desses documentos. Os documentos enviados são processados e armazenados em um banco de dados de vetores (Vector Database) que facilita a extração das informações. O sistema conta também com uma interface bem simples para facilitar o entendimento das funcionalidades. Para utilizá-lo você deve informar uma API Key válida.<br/><br/>
![image](https://github.com/user-attachments/assets/b5866fce-30cd-4d4f-8097-84509e6ce29e)


## Funcionalidades

- **Interação com Documentos PDF**: Permite o upload de arquivos PDF para processamento.
- **Pesquisa Inteligente**: Permite ao usuário fazer perguntas sobre o conteúdo dos documentos carregados.
- **Suporte a Vários Modelos da OpenAI**: Suporte para escolher entre vários modelos da OpenAI, como `gpt-3.5-turbo`, `gpt-4`, `gpt-4-turbo` e variantes de `gpt-4`.
- **Validação de API Key**: Verificação automática de validade da chave da API para garantir a integração correta com os modelos da OpenAI. (A Chave não é armazenada para sua segurança, sendo utilizada apenas em tempo de execução.)
- **Persistência de Dados**: Armazena dados vetoriais dos PDFs processados para consultas futuras.

## Tecnologias Utilizadas

- **Streamlit**: Framework para criação da interface do usuário.
- **OpenAI API**: Para interação com modelos de linguagem de IA.
- **Python**: Linguagem principal usada no projeto.
- **Pandas**: Para manipulação de dados.
- **decouple**: Para gerenciamento de variáveis de ambiente.
- **Vector Databases**: Usado para persistir e buscar dados extraídos dos PDFs.

## Pré-requisitos

Antes de rodar o projeto, você precisará de:

- Python 3.x instalado em sua máquina.
- Uma chave da API da OpenAI válida. Você pode obter uma chave [aqui](https://platform.openai.com/signup).
- Instalar as dependências do projeto.

## Instalação

### 1. Clonando o repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu_usuario/chatdoc-rag.git
cd chatdoc-rag
