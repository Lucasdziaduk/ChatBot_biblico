# ✝️ Chatbot Bíblico Inteligente (RAG + IA)

Um chatbot inteligente capaz de responder perguntas bíblicas utilizando técnicas modernas de **Recuperação de Informação (RAG)**, **Embeddings Semânticos** e **Modelos de Linguagem (LLMs)**.

---

## 🚀 Visão Geral

Este projeto implementa um sistema de perguntas e respostas sobre a Bíblia que combina:

* 📖 Base textual estruturada (Bíblia em JSON)
* 🧠 Busca semântica com embeddings
* 🔎 Busca textual (keyword-based)
* ⚖️ Ranking híbrido (semântico + textual)
* 🤖 Geração de resposta com LLM

O objetivo é fornecer respostas **contextualizadas, relevantes e coerentes** com base nas Escrituras.

---

## 🧠 Arquitetura do Sistema

```text
Pergunta do usuário
        ↓
Embedding (Sentence Transformers)
        ↓
Busca Semântica (cosine similarity)
        ↓
Busca Textual (BM25)
        ↓
Ranking Híbrido (combinação de scores)
        ↓
Top-K resultados relevantes
        ↓
Chunking (contexto expandido)
        ↓
LLM (geração da resposta final)
```

---

## ⚙️ Tecnologias Utilizadas

* **Python**
* **FastAPI** – API backend
* **SentenceTransformers** – geração de embeddings
* **BM25** – busca textual
* **OpenAI API** – geração de respostas
* **Gradio** – interface de usuário
* **Pytest** – testes automatizados

---

## 📁 Estrutura do Projeto

```bash
biblia_chatbot/
│
├── app/
│   ├── api/                # Rotas da API
│   ├── core/               # Configurações e prompts
│   ├── models/             # Schemas
│   ├── services/           # Lógica principal (RAG, embeddings, etc)
│   ├── data/               # Base bíblica (JSON)
│   └── main.py             # Inicialização da aplicação
│
├── tests/                  # Testes automatizados
├── ui/                     # Interface Gradio
├── requirements.txt
└── README.md
```

---

## 🔍 Funcionalidades

* ✅ Perguntas em linguagem natural sobre a Bíblia
* ✅ Busca semântica por similaridade
* ✅ Busca textual por palavras-chave
* ✅ Ranking híbrido (melhor relevância)
* ✅ Geração de respostas com contexto bíblico
* ✅ Interface interativa com Gradio

---

## 📊 Diferenciais Técnicos

Este projeto não é um chatbot simples. Ele implementa conceitos modernos de IA:

### 🔹 RAG (Retrieval-Augmented Generation)

Combina recuperação de informação com geração por LLM.

### 🔹 Embeddings Semânticos

Permite entender o significado da pergunta, não apenas palavras.

### 🔹 Ranking Híbrido

Melhora a precisão combinando:

* Similaridade semântica
* Correspondência textual

### 🔹 Separação em Camadas

Arquitetura modular:

* API
* Serviços
* Modelos
* Dados

---

## 🛠️ Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/Lucasdziaduk/ChatBot_biblico.git
cd ChatBot_biblico
```

---

### 2. Criar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz:

```env
OPENAI_API_KEY=sua_chave_aqui
```

---

### 5. Executar a API

```bash
uvicorn app.main:app --reload
```

---

### 6. Executar interface (opcional)

```bash
python ui/gradio_app.py
```

---

## 🧪 Testes

```bash
pytest
```

---

## 🔐 Segurança

* ❌ Nenhuma chave de API é versionada
* ✅ Uso de variáveis de ambiente (`.env`)
* ✅ `.gitignore` configurado corretamente

---

## 📈 Possíveis Melhorias

* 🔄 Cache de embeddings para performance
* 📊 Avaliação automática de respostas (metrics)
* 🌍 Suporte a múltiplas traduções bíblicas
* 🧠 Fine-tuning ou uso de modelos locais
* ⚡ Deploy em nuvem (AWS, GCP, Vercel)

---

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com foco em:

* Aprendizado de **IA aplicada**
* Implementação prática de **RAG**
* Construção de **sistemas escaláveis**
* Portfólio técnico para área de tecnologia

---

## 👨‍💻 Autor

**Lucas Dziaduk**

---

## 📄 Licença

Este projeto está sob a licença MIT.
