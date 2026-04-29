#  Tradeoffs – System Design Decisions

##  1. Hybrid System vs Pure LLM
- Chose hybrid (rules + embeddings) instead of LLM-only system
- Reason:
  - faster inference in CLI environment
  - deterministic outputs for customer support
  - lower cost and easier debugging
- Tradeoff: less generative flexibility than GPT-style models

---

##  2. No Fine-Tuning Approach
- Did NOT fine-tune transformer model
- Reason:
  - 5-hour constraint
  - dataset too small for meaningful fine-tuning
- Instead used:
  - SentenceTransformers embeddings
  - semantic similarity matching

---

##  3. No Vector Database (FAISS/Pinecone)
- Used in-memory similarity search instead
- Reason:
  - simplicity and portability
  - no infra dependency
- Tradeoff:
  - not scalable to millions of FAQs

---

##  4. Structured Output over Free Text
- Forced JSON schema validation (Pydantic-style)
- Reason:
  - production-grade reliability
  - avoids hallucinated formats
- Tradeoff:
  - reduced natural language flexibility

---

##  5. Multilingual Design Choice
- Used static bilingual response mapping (EN + AR)
- Reason:
  - ensures controlled Arabic output quality
- Tradeoff:
  - not fully dynamic translation system

---

##  Final Design Philosophy
Prioritized:
✔ reliability  
✔ interpretability  
✔ structured outputs  
✔ deterministic behavior  

Over:
✖ pure generative creativity  
✖ large model dependency  
✖ production scaling complexity