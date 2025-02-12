# 📄 Chat with PDFs using AI

This Streamlit app allows you to chat with your PDF documents using AI-powered retrieval and generation models. 📚✨

## 🚀 Features
✅ Upload and process multiple PDF files 📂
✅ Uses **FAISS** for vector database storage ⚡
✅ Google Generative AI for vector embeddings 🧠
✅ **GROQ LLM** for accurate and contextual responses 🤖
✅ Document similarity search to find relevant excerpts 🔍

---

## 📦 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/chat-with-pdfs.git
cd chat-with-pdfs
```

### 2️⃣ Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv chat
source venv/bin/activate  # On Windows use: chat\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file and add the following:
```ini
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
```
👉 Get your API keys from [GROQ](https://groq.com/) and [Google AI](https://ai.google.dev/)

---

## 🚀 Usage
Run the application with:
```bash
streamlit run app.py
```

### 🎨 How to Use
1️⃣ Upload one or multiple PDF files 📜
2️⃣ Click **Process Documents** to extract and store embeddings 📊
3️⃣ Enter your question based on the uploaded PDFs ✍️
4️⃣ View AI-generated responses with document context 🖥️

---

## 🔧 Troubleshooting
🔹 Ensure your API keys are correctly set in the `.env` file.
🔹 If vector storage isn't working, try deleting cached files and restarting the app.
🔹 Make sure all dependencies are installed properly.

---

## 🤝 Contributing
Want to enhance this project? Fork it, make improvements, and submit a PR! 🚀

---

## 📜 License
This project is licensed under the MIT License. 📄

---

### 💡 Credits
Built with ❤️ by **Your Name**

🔗 Follow me on [GitHub](https://github.com/Pradhyumnasg) | [Linkedin](https://www.linkedin.com/in/pradhyumn-sg-a0629918b/) 🌍

