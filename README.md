# 🚀 Prompt Optimization Toolkit

An interactive and visual Streamlit app that helps Prompt Engineers test, compare, and fine-tune prompt strategies across Large Language Models (LLMs) like LLaMA 3 and Mixtral using the **Groq API**.

---

## 🎯 Project Objective

To build a **Prompt Tuning & Evaluation Dashboard** where users can:
- Select prompt styles (e.g., instructive, creative, interrogative)
- Compare responses from two LLMs side-by-side
- Track token usage and temperature effect
- Rank and store the best-performing prompts

---

## 📸 Live Demo

> **Coming Soon** – Link to Streamlit Cloud or local app instructions

---

## 🧠 Key Features

| Feature | Description |
|--------|-------------|
| 🔄 Compare Two LLMs | View outputs from LLaMA 3 and Mixtral models side-by-side |
| ✍️ Prompt Templates | Instructive, Story-style, Question-formatted prompts built-in |
| 📊 Metrics Display | Token usage, temperature, word count, relevance |
| 🏆 Leaderboard (planned) | Save top-performing prompts based on results |
| 📁 Modular Code | Organized with `utils.py`, `prompts.json`, and clean `app.py` |

---

## 🧪 Tech Stack

- **Frontend:** Streamlit
- **Backend/API:** Groq LLMs (via OpenAI-compatible endpoint)
- **Languages:** Python
- **Libraries:** requests, json, Streamlit
- **Other Tools:** Git, VS Code

---

## ⚙️ How to Run Locally

1. **Clone this repo:**
   ```bash
   git clone https://github.com/VenkataDurgaPrasadX/prompt-optimization-toolkit.git
   cd prompt-optimization-toolkit
2. Install dependencies:
  - pip install streamlit requests


3. Start the app:
  - streamlit run app.py

4. Enter your Groq API key from the sidebar to get started.
 -    prompt-optimization-toolkit/
- ├── app.py                # Main Streamlit app
- ├── utils.py              # API call + token usage logic
- ├── prompts.json          # Predefined prompt styles
- ├── README.md             # Project description
- └── requirements.txt      # (Optional) For deployment

**💡 Use Cases**
🔬 Experimenting with prompt variations for real-world LLM performance

🧪 Training Prompt Engineers on prompt tuning workflows

📈 Evaluating token cost/performance balance in AI products


**📚 Future Enhancements**
Export chat history as .json or .txt

Save & rank prompts to leaderboard

Add timestamps and model confidence scores

Dark mode and CSS chat bubble layout


**🧑‍💻 Author**
Tattukolla Venkata Durga Prasad
📧 venkatadurgaprasad04@gmail.com
🔗 LinkedIn | GitHub


**📜 License**
This project is licensed under the MIT License.



