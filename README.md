# Document Summarization Service 📝

A simple web-based document summarization app using **Groq API**. Users can input text and get summarized output in multiple styles: brief, detailed, or bullet points.

---

## Features
- Input text through a clean web interface using **Streamlit**
- Multiple summarization styles: brief, detailed, bullet points
- Handles API errors gracefully
- Basic input validation
- Easy to extend for other APIs or local models

---



document-summarizer/
│
├── app/
│ ├── main.py # Streamlit front-end
│ ├── summarizer.py # Summarization logic using Groq API
│ ├── .env # Environment variables (API key)
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation
