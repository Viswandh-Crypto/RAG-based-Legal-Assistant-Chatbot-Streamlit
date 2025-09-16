# RAG-based-Legal-Assistant-Chatbot-Streamlit

⚖️ Legal Assistant Chatbot

An AI-powered Retrieval-Augmented Generation (RAG) chatbot built with LangChain, FAISS, Google Generative AI, and Streamlit.

This tool helps legal professionals and researchers analyze court orders quickly by uploading a PDF and asking natural language questions. The chatbot retrieves relevant context from the document and provides concise, legally structured answers.

🚀 Features

    📂 Upload Court Orders: Easily upload PDF court orders.

    🔍 Context-Aware Q&A: Ask detailed questions, and get answers grounded in the uploaded document.

    📝 Summarization: Generate concise 3-bullet case summaries.

    👥 Petitioners Identification: Quickly extract names of petitioners.

    📑 Liquidator Observations: Retrieve key observations from the Official Liquidator.

    ⏳ Deadline Tracking: Identify critical filing deadlines.

    💬 Custom Chat: Ask any question in plain English.

    🖥 User-Friendly UI: Clean Streamlit interface with chat history.

🛠️ Tech Stack

    LangChain
     – Framework for LLM applications

    FAISS
     – Vector database for document retrieval

    HuggingFace Sentence Transformers
     – For embeddings

    Google Generative AI (Gemini)
     – Large Language Model for responses

    Streamlit
     – Interactive web UI

    PyMuPDF
     – PDF parsing

▶️ Usage

    Run the app with:

    streamlit run Legal-Assistant-Chatbot.py


    1.Upload a court order PDF.

    2.Use quick action buttons (Summarize, Petitioners, Observations, Deadlines).

    3.Or ask your own custom legal questions.

    4.View responses and chat history directly in the UI.

📸 Screenshot
<img width="1920" height="1080" alt="Screenshot 2025-09-16 124013" src="https://github.com/user-attachments/assets/fed96fe0-ebe4-4514-99da-13b80a857f4f" />

📌 Future Improvements

    📚 Support for multiple PDFs

    🌐 Deployment on HuggingFace Spaces / Streamlit Cloud

    🧾 Case law citation extraction

    📊 Structured output (JSON / tables for deadlines, parties, etc.)

🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a PR with improvements.

⚠️ Disclaimer

This chatbot is for educational and research purposes only.
It is not a substitute for professional legal advice. Always consult a qualified lawyer for actual legal matters.
