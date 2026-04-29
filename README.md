# 🤖 Mumzworld AI Support System (Track A - AI Engineering Intern)

> Production-grade AI-native multilingual customer support system for e-commerce (Mumzworld use case) built with intent classification, retrieval-augmented responses, embeddings, structured outputs, and evaluation framework in English + Arabic.

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![AI](https://img.shields.io/badge/AI-Native-green.svg)]()
[![NLP](https://img.shields.io/badge/NLP-Embeddings-orange.svg)]()
[![Status](https://img.shields.io/badge/Status-Prototype-brightgreen.svg)]()

---

## 🎯 Overview

This project is an AI-native customer support system designed for Mumzworld, the largest e-commerce platform for mothers in the Middle East. It handles customer queries in English and Arabic using a hybrid AI pipeline combining intent classification, semantic embeddings, and a lightweight retrieval-augmented generation (RAG) system.

The system is built to simulate a real-world production support assistant that can understand paraphrased queries, retrieve relevant FAQ knowledge, respond in multiple languages, and provide structured outputs with confidence scoring and fallback handling for unknown inputs.

It is not a simple chatbot. It is an AI pipeline combining:
- Intent classification (rule + semantic)
- Embedding-based similarity matching
- Retrieval-Augmented Generation (FAQ grounding)
- Structured JSON output validation
- Confidence scoring + uncertainty handling
- Evaluation framework with measurable accuracy

---

## 🧠 Problem It Solves

Customer support teams face:
- Repeated queries (refunds, delays, returns)
- Mixed English + Arabic messages
- Unstructured user inputs
- Slow manual response handling
- Inconsistent responses across agents

This system solves it by automatically:
- Understanding intent
- Retrieving relevant policy context
- Generating structured bilingual responses
- Handling uncertainty safely

---

## ⚙️ Key Features

### 🧩 AI Capabilities
- Intent classification (refund, delay, product issue, order status, policy, shipping, unknown)
- Semantic understanding using sentence embeddings
- FAQ retrieval using similarity search (RAG-style)
- Confidence scoring per prediction
- Safe fallback for unknown queries

### 🌍 Multilingual Output
- Native English responses
- Native Arabic responses (not literal translation style)

### 🧠 Structured Output
Every response follows strict schema:
- intent
- response_en
- response_ar
- confidence
- faq_used (optional)

### 📊 Evaluation System
- 12+ test cases (normal + adversarial inputs)
- Accuracy measurement (~91.6%)
- Robustness testing on noise inputs
- Unknown intent detection validation

---

## 🏗️ Architecture

User Input → Classifier (Rule + Embedding) → Retriever (FAQ similarity) → RAG Context Injection → Response Generator → Pydantic Validator → Final Structured JSON Output

---

## 📁 Project Structure

app.py → CLI interface  
classifier.py → intent classification engine  
embeddings.py → sentence transformer embeddings  
rag.py → FAQ retrieval system  
response.py → response generation (EN + AR)  
validator.py → structured schema validation (Pydantic)  
eval.py → evaluation pipeline (accuracy testing)  
config.py → intents + FAQ dataset  
data.py → sample training/FAQ data  
tools.py → utility functions  
utils.py → helper functions  
policies.txt → business rules  

---

## 🚀 How to Run

1. Create virtual environment:
python -m venv venv  
venv\Scripts\activate  

2. Install dependencies:
pip install -r requirements.txt  

3. Run system:
python app.py  

4. Run evaluation:
python eval.py  

---

## 💬 Example Outputs

User: I want my money back  
{
  "intent": "refund_request",
  "response_en": "Refund is available within 30 days if the product is unused.",
  "response_ar": "يمكنك استرجاع المبلغ خلال 30 يوم إذا لم يتم استخدام المنتج.",
  "confidence": 0.77,
  "faq_used": "Returns accepted within 30 days of purchase."
}

User: my order is late  
{
  "intent": "delay_issue",
  "response_en": "Your order may be delayed. Please share your order ID.",
  "response_ar": "قد يكون طلبك متأخراً. يرجى مشاركة رقم الطلب.",
  "confidence": 0.66
}

User: asdfgh random text  
{
  "intent": "unknown",
  "response_en": "I need more details to help you.",
  "response_ar": "أحتاج إلى مزيد من التفاصيل لمساعدتك.",
  "confidence": 0.18
}

---

## 📊 Evaluation Results

- Test cases: 12  
- Accuracy: 91.6%  
- Robustness: Handles noisy + adversarial inputs  
- Unknown detection: Working correctly  
- Confidence calibration: Stable across intents  

---

## 🧠 Why This Is AI Engineering (Not Just ML)

This system includes:
- Agent-like pipeline (classifier → retriever → generator)
- Embedding-based semantic retrieval (RAG)
- Structured output enforcement (Pydantic validation)
- Uncertainty-aware responses (confidence scoring + fallback)
- Multilingual generation (English + Arabic)

---

## ⚠️ Limitations

- No external LLM API used (lightweight local model design)
- Dataset is synthetic (expandable with real data)
- CLI-based interface (no frontend UI yet)
- No persistent memory layer

---

## 🔥 Future Improvements

- Fine-tuned transformer classifier
- Vector database (FAISS / Pinecone)
- Real-time dashboard for support analytics
- WhatsApp / chat UI integration
- Human escalation workflow
- Production API deployment (FastAPI)

---

## 🧪 Tools Used

- SentenceTransformers
- Scikit-learn
- Embedding similarity search
- Pydantic validation
- Python CLI system
- Custom evaluation pipeline

---

## ⏱ Time Log

- Design: 1 hour  
- AI pipeline: 2 hours  
- Implementation: 1.5 hours  
- Evaluation: 0.5 hour  

---

## 📌 Key Insight

This project demonstrates how real-world AI support systems are built using:
- Semantic understanding (embeddings)
- Retrieval augmentation (RAG)
- Structured outputs (validation)
- Evaluation-driven development
- Multilingual response generation

Designed specifically for real e-commerce AI workflows like Mumzworld (English + Arabic support).