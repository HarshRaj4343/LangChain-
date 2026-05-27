# 🦜🔗 LangChain — Learning Repository

> Personal notes and code while following the **[Generative AI using LangChain](https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0)** playlist by [CampusX](https://www.youtube.com/@campusx-official).  
> 19 videos · hands-on Python · multi-provider LLMs (OpenAI, Anthropic, Google, HuggingFace)

---

## 📁 Repository Structure

```
LangChain-/
├── LLMs/                        # Video 03 — LLM models (OpenAI, HuggingFace, etc.)
├── ChatModels/                  # Video 03 — Chat models (GPT-4, Claude, Gemini)
├── EmbeddedModels/              # Video 03 — Embedding models
├── Messages/                    # Video 04 — LangChain message types
├── Prompts/                     # Video 04 — Prompt templates & chatbot UI
├── Structured Outputs/
│   └── with structured outputs/ # Video 05 — Pydantic / TypedDict / JSON schemas
├── Chains/                      # Video 07 — Simple, sequential, parallel, conditional chains
├── Document Similarity Search/  # Video 12–13 — Vector stores & retrievers
├── MyChatBot/                   # Video 15 — RAG-based YouTube chatbot
├── requirements.txt
├── template.json
└── test.py
```

---

## 🎬 Playlist Curriculum

All 19 videos from the CampusX LangChain series, with official code links where available.

| # | Video | Duration | Topics Covered | Code |
|---|-------|----------|----------------|------|
| 00 | [Generative AI using LangChain — Intro](https://www.youtube.com/watch?v=pSVk-5WemQ0) | 15 min | What is LangChain, why use it, course overview | — |
| 01 | [Introduction to LangChain](https://www.youtube.com/watch?v=nlz9j-r0U9U) | 38 min | LangChain architecture, installation, first program | — |
| 02 | [LangChain Components](https://www.youtube.com/watch?v=pSVk-5WemQ0&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) | 53 min | Models, Prompts, Chains, Retrievers, Agents overview | — |
| 03 | [LangChain Models — In-depth](https://www.youtube.com/watch?v=HdcLE8JuMrA) | 102 min | LLMs, Chat Models, Embedding Models across providers | [📂 langchain-models](https://github.com/campusx-official/langchain-models) |
| 04 | [Prompts in LangChain](https://www.youtube.com/watch?v=pSVk-5WemQ0&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) | 79 min | PromptTemplate, ChatPromptTemplate, MessagePlaceholder, Chatbot UI | [📂 langchain-prompts](https://github.com/campusx-official/langchain-prompts) |
| 05 | [Structured Output in LangChain](https://www.youtube.com/watch?v=pSVk-5WemQ0&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) | 68 min | `with_structured_output`, Pydantic, TypedDict, JSON Schema | [📂 langchain-structured-output](https://github.com/campusx-official/langchain-structured-output) |
| 06 | [Output Parsers in LangChain](https://www.youtube.com/watch?v=pSVk-5WemQ0&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) | 53 min | StrOutputParser, PydanticOutputParser, JSONOutputParser, StructuredOutputParser | [📂 langchain-output-parsers](https://github.com/campusx-official/langchain-output-parsers) |
| 07 | [Chains in LangChain](https://www.youtube.com/watch?v=pSVk-5WemQ0&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) | 54 min | Simple chain, sequential chain, parallel chain, conditional chain | [📂 langchain-chains](https://github.com/campusx-official/langchain-chains) |
| 08 | [What are Runnables in LangChain](https://www.youtube.com/watch?v=pSVk-5WemQ0&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) | 76 min | RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda | [📂 langchain-runnables](https://github.com/campusx-official/langchain-runnables) |
| 09 | [LangChain Runnables — Part 2](https://www.youtube.com/watch?v=pSVk-5WemQ0&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) | 54 min | RunnableBranch, advanced composition patterns | [📂 langchain-runnables](https://github.com/campusx-official/langchain-runnables) |
| 10 | [Document Loaders in LangChain](https://www.youtube.com/watch?v=pSVk-5WemQ0&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) | 57 min | PDF, CSV, Web, YouTube loaders; `Document` objects | [📂 langchain-document-loaders](https://github.com/campusx-official/langchain-document-loaders) |
| 11 | [Text Splitters in LangChain](https://www.youtube.com/watch?v=pSVk-5WemQ0&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) | 59 min | Length-based, text-structure, markdown, code, semantic splitting | [📂 langchain-text-splitters](https://github.com/campusx-official/langchain-text-splitters) |
| 12 | [Vector Stores in LangChain](https://www.youtube.com/watch?v=pSVk-5WemQ0&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) | 51 min | FAISS, Chroma; embedding + indexing; similarity search | — |
| 13 | [Retrievers in LangChain](https://www.youtube.com/watch?v=pSVk-5WemQ0&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) | 51 min | VectorStoreRetriever, MMR, similarity score threshold | — |
| 14 | [Retrieval Augmented Generation — What is RAG?](https://www.youtube.com/watch?v=pSVk-5WemQ0&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) | 59 min | RAG architecture, ingest → retrieve → generate pipeline | — |
| 15 | [YouTube Chatbot using LangChain — Building a RAG System](https://www.youtube.com/watch?v=pSVk-5WemQ0&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) | 46 min | End-to-end RAG chatbot over YouTube transcripts | — |
| 16 | [Tools in LangChain](https://www.youtube.com/watch?v=pSVk-5WemQ0&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) | 45 min | Built-in tools, custom tools, `@tool` decorator | — |
| 17 | [Tool Calling in LangChain](https://www.youtube.com/watch?v=pSVk-5WemQ0&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) | 59 min | `bind_tools`, tool execution loop, function calling | — |
| 18 | [Building an End-to-End AI Agent in LangChain](https://www.youtube.com/watch?v=pSVk-5WemQ0&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) | 73 min | ReAct agent, AgentExecutor, full autonomous agent build | — |

> **Full playlist →** https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0  
> **Official CampusX code repos →** https://github.com/campusx-official

---

## 🗂️ Folder → Video Mapping

| Folder | Video(s) | What's inside |
|--------|----------|---------------|
| `LLMs/` | #03 | OpenAI, HuggingFace LLM wrappers |
| `ChatModels/` | #03 | ChatOpenAI, ChatAnthropic, ChatGoogleGenerativeAI |
| `EmbeddedModels/` | #03 | OpenAI & HuggingFace embedding models |
| `Messages/` | #04 | HumanMessage, AIMessage, SystemMessage types |
| `Prompts/` | #04 | PromptTemplate, ChatPromptTemplate, chatbot UI (Streamlit) |
| `Structured Outputs/` | #05 | `with_structured_output` via Pydantic / TypedDict / JSON |
| `Chains/` | #07 | Simple → sequential → parallel → conditional chains |
| `Document Similarity Search/` | #12–13 | FAISS vector store + retriever for semantic search |
| `MyChatBot/` | #15 | RAG chatbot over YouTube video transcripts |

---

## ⚙️ Setup

### 1. Clone

```bash
git clone https://github.com/HarshRaj4343/LangChain-.git
cd LangChain-
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt` includes:**

```
langchain
langchain-core
langchain-openai
openai
langchain-anthropic
langchain-google-genai
google-generativeai
langchain-huggingface
transformers
huggingface-hub
python-dotenv
numpy
scikit-learn
pandas
```

### 4. Set up API keys

Create a `.env` file in the root:

```env
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=...
HUGGINGFACEHUB_API_TOKEN=...
```

> The `.gitignore` already excludes `.env`. Never commit your keys.

---

## 🔑 Providers Used

| Provider | Model(s) | Used In |
|----------|----------|---------|
| OpenAI | `gpt-4o`, `text-embedding-3-small` | LLMs, ChatModels, Embeddings |
| Anthropic | `claude-3-5-sonnet` | ChatModels |
| Google | `gemini-1.5-flash` | ChatModels |
| HuggingFace | various open-source | LLMs, Embeddings |

---

## 📚 Resources

- [LangChain Docs](https://python.langchain.com/docs/introduction/)
- [CampusX YouTube Channel](https://www.youtube.com/@campusx-official)
- [CampusX Official GitHub](https://github.com/campusx-official)
- [Full Playlist](https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0)

---

*Following along with the CampusX LangChain series — Generative AI using LangChain (2025).*
