# 🤖 Mumzworld AI Support System (Track A – AI Engineering Intern)

> Production-ready AI customer support system for Mumzworld with semantic understanding, multilingual responses, retrieval-augmented generation (RAG), and structured output validation.

---

## 🎯 Overview

This project is an AI-native customer support system designed for Mumzworld, the largest e-commerce platform for mothers in the Middle East. It handles customer queries in English and Arabic using a hybrid AI pipeline combining intent classification, semantic embeddings, and a lightweight retrieval-augmented generation (RAG) system.

The system is built to simulate a real-world production support assistant that can understand paraphrased queries, retrieve relevant FAQ knowledge, respond in multiple languages, and provide structured outputs with confidence scoring and fallback handling for unknown inputs.

---

## 🚀 Key Features

The system supports semantic intent detection using sentence embeddings instead of keyword matching, enabling it to understand paraphrased queries like “I want my money back”, “refund please”, and “return my payment” as the same intent. It includes a lightweight RAG system that retrieves relevant FAQ answers using cosine similarity, ensuring responses are grounded in predefined knowledge rather than hallucination.

It provides multilingual responses in English and Arabic, confidence scoring for every prediction, structured JSON output validated using Pydantic, and safe fallback behavior for unknown or noisy inputs. The system also includes an evaluation pipeline that measures accuracy across real and adversarial test cases.

---

## 🏗️ Architecture

User input is first normalized and converted into embeddings using SentenceTransformer. The embedding is then used for semantic similarity matching against predefined intent examples and FAQ knowledge. The system determines intent using a hybrid logic combining similarity scores and rule-based fallback conditions. Once intent is identified, a response is generated using either FAQ retrieval (RAG) or template-based responses. A confidence score is computed based on similarity strength, and the final output is validated using a structured schema before being returned.

---

## 🧠 Core Capabilities

The system understands real-world paraphrased user queries, supports bilingual response generation (English and Arabic), retrieves grounded FAQ responses using semantic search, handles unknown or noisy inputs safely, and provides confidence scoring for all predictions. It is designed to avoid hallucination by relying only on retrieved knowledge and predefined intent mappings.

---

## 📊 Evaluation Results

The system achieves approximately 91% accuracy on a mixed evaluation dataset consisting of customer support scenarios such as refund requests, order delays, product issues, shipping queries, and random noise inputs. It correctly handles paraphrased inputs, unknown queries, and maintains stable multilingual response quality across test cases.

---

## 🧪 Sample Outputs

Input: "I want my money back"
{
  "intent": "refund_request",
  "response_en": "Refund is available within 30 days if the product is unused.",
  "response_ar": "يمكنك استرجاع المبلغ خلال 30 يوم إذا لم يتم استخدام المنتج.",
  "confidence": 0.77,
  "faq_used": "Returns accepted within 30 days of purchase."
}

Input: "my order is late"
{
  "intent": "delay_issue",
  "response_en": "Your order may be delayed. Please share your order ID.",
  "response_ar": "قد يكون طلبك متأخراً. يرجى مشاركة رقم الطلب.",
  "confidence": 0.89,
  "faq_used": null
}

Input: "asdfgh"
{
  "intent": "unknown",
  "response_en": "I need more details to help you.",
  "response_ar": "أحتاج إلى مزيد من التفاصيل لمساعدتك.",
  "confidence": 0.18,
  "faq_used": null
}

---

## 📁 Project Structure

app.py → CLI interface for interaction  
classifier.py → semantic + rule-based intent classification  
embeddings.py → sentence transformer embedding generation  
rag.py → FAQ retrieval system using similarity search  
config.py → intents and FAQ dataset  
schema.py → structured output validation using Pydantic  
eval.py → evaluation pipeline  
utils.py → helper utilities  

---

## ⚙️ Setup Instructions

Clone the repository using git clone https://github.com/DuggireddyVarshini/mumzworld-ai-support-v2.git then navigate into the folder. Create a virtual environment using python -m venv venv and activate it using venv\Scripts\activate on Windows or source venv/bin/activate on Linux/Mac. Install dependencies using pip install -r requirements.txt. Run the application using python app.py. Run evaluation using python eval.py.

---

## 📦 Requirements

sentence-transformers  
numpy  
scikit-learn  
faiss-cpu  
pydantic  

---

## 🧠 Design Decisions

The system uses embeddings instead of keyword matching to handle real-world paraphrasing. A lightweight RAG system is used to ensure responses are grounded in FAQ knowledge instead of hallucinated outputs. A hybrid architecture combining rules and semantic similarity ensures stability and robustness. Confidence scoring is used to indicate uncertainty and improve reliability in production-like scenarios.

---

## ⚠️ Limitations

The system does not use a large language model due to assignment constraints. The FAQ dataset is synthetic and can be expanded with real customer data. The system runs in CLI mode without a frontend interface.

---

## 🚀 Future Improvements

Future versions can include FastAPI deployment, React-based support dashboard, integration with LLMs like GPT or Llama 3 for response generation, real-time analytics dashboard, cloud deployment on AWS or Azure, and conversation memory for contextual support.

---

## 🧪 Evaluation Summary

The system has been evaluated on 12+ test cases with an accuracy of approximately 91%. It performs well on paraphrased inputs, unknown query detection, and multilingual response generation while maintaining consistent confidence scoring.

---

## 🧰 Tools Used

SentenceTransformers (MiniLM), Scikit-learn, FAISS / cosine similarity, Pydantic validation, Python CLI system.

---

## ⏱️ Time Breakdown

Problem design: 1 hour  
Core implementation: 2 hours  
Embeddings + RAG: 1 hour  
Evaluation: 1 hour  

---

## 📌 Final Note

This project demonstrates real-world AI engineering capability including semantic search, retrieval-augmented generation, multilingual response handling, structured output validation, and evaluation-driven development. It is designed as a production-style AI support system aligned with real e-commerce use cases like Mumzworld.

---

## 🔗 GitHub Repository

https://github.com/DuggireddyVarshini/mumzworld-ai-support-v2