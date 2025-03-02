# ChatDoc - RAG (Retrieval-Augmented Generation)

O **ChatDoc** é uma aplicação interativa que permite a análise de documentos PDF, integrando-se com modelos de linguagem da OpenAI. Utilizando a abordagem de **Retrieval-Augmented Generation (RAG)**, o sistema permite que o modelo acesse informações extraídas dos documentos carregados e forneça respostas detalhadas com base no conteúdo desses documentos. Os PDFs enviados são processados e armazenados em um banco de dados vetorial (Vector Database), o que facilita a extração e consulta das informações. O sistema também oferece uma interface intuitiva para melhorar a experiência do usuário.

> **⚠️ Aviso:** Para usar o ChatDoc, você precisará informar uma API Key válida.

![imagem](https://github.com/user-attachments/assets/b5866fce-30cd-4d4f-8097-84509e6ce29e)

## Funcionalidades

- **Interação com Documentos PDF**: Realize o upload de arquivos PDF para processamento e análise.
- **Pesquisa Inteligente**: Pergunte sobre o conteúdo dos documentos carregados e obtenha respostas detalhadas.
- **Suporte a Modelos da OpenAI**: Escolha entre modelos como `gpt-3.5-turbo`, `gpt-4`, `gpt-4-turbo` e variantes do `gpt-4`.
- **Validação de API Key**: O sistema verifica automaticamente a validade da chave de API, sem armazená-la, garantindo a segurança.
- **Persistência de Dados**: Os dados extraídos dos PDFs são armazenados em um banco de dados vetorial, permitindo consultas rápidas e eficientes.

## Tecnologias Utilizadas

- **Streamlit**: Framework utilizado para criar a interface do usuário.
- **OpenAI API**: Para integrar os modelos de linguagem da OpenAI.
- **Python**: Linguagem principal do projeto.
- **Pandas**: Biblioteca para manipulação de dados.
- **Decouple**: Utilizada para gerenciar variáveis de ambiente.
- **Vector Databases**: Usado para persistir e buscar dados extraídos dos PDFs.

## Pré-requisitos

Antes de executar o projeto, você precisará de:

- **Python 3.x** instalado em sua máquina.
- **Uma chave da API da OpenAI válida**. Você pode obter uma chave [aqui](https://platform.openai.com/signup).
- Instalar as dependências do projeto.

## Instalação

### 1. Clonando o repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu_usuario/chatdoc-rag.git
cd chatdoc-rag
