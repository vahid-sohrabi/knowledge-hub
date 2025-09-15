# Knowledge-Hub

**Knowledge-Hub** is a microservices-based platform designed to store and retrieve PDF files with advanced Question-Answering (QA) capabilities. The system leverages a **Qdrant Vector Database** and the **LangChain** framework to implement a **Retrieval-Augmented Generation (RAG)** pipeline, allowing users to efficiently search and query PDF documents.

---

## Features

- **Semantic PDF Storage**: Index PDF files in Qdrant for fast and accurate retrieval.  
- **Advanced Question-Answering**: Answer user queries using RAG and large language models (LLMs).  
- **Microservices Architecture**:  
  - Separate retrieval and QA processes for better scalability and performance optimization.  
  - Independent deployment of each service.  
  - Fault isolation and easy integration with other services.  
- **Enterprise Flexibility**: Suitable for enterprise applications with large volumes of documents and high-speed access requirements.  
- **Multi-Source Support**: Connect to multiple databases and external services.

---

## System Architecture

1. **Service Layer**: Independent services for information retrieval and QA.  
2. **Qdrant Vector Database**: Stores PDF content in vector format for semantic search.  
3. **RAG Pipeline**: Combines retrieval and generation using large language models.  
4. **API Gateway**: Manages user requests and routes them to appropriate services.  

**Advantages:**  
- High scalability  
- Service independence  
- Fault tolerance  
- Easy development and integration  

---

## Installation and Setup

### Prerequisites

- Python >= 3.11  
- Docker & Docker Compose  
- Qdrant Vector Database  
- LangChain and its dependencies  

### Setup Steps

```bash
# Clone the repository
git clone https://github.com/yourusername/knowledge-hub.git
cd knowledge-hub

# Install dependencies
pip install -r requirements.txt

# Start services using Docker Compose
docker-compose up -d
