# 🏥 Medical Prediction System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red?style=for-the-badge&logo=streamlit&logoColor=white)
![Gemini AI](https://img.shields.io/badge/Gemini_AI-2.0_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**An AI-powered heart disease prediction and medical chat assistant built with Streamlit and Google Gemini.**

[🚀 Live Demo](#-demo) · [📦 Installation](#-installation) · [🐛 Report Bug](https://github.com/sohail189/Medical-prediction-system/issues) · [💡 Request Feature](https://github.com/sohail189/Medical-prediction-system/issues)

</div>

---

## 📝 Description

The **Medical Prediction System** is an intelligent health assistant that combines machine learning and generative AI to help users:

1. **Predict heart disease risk** — Enter patient data and get an instant risk assessment using a trained ML model.
2. **Ask medical questions** — Chat with a Google Gemini-powered AI assistant specialised in heart disease and general health.

> ⚠️ **Disclaimer:** This tool is for educational purposes only. It is **not** a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider.

---

## ✨ Features

- 💬 **AI Medical Chatbot** — Conversational assistant powered by Google Gemini 2.0 Flash, specialised in heart disease knowledge
- 🔬 **Heart Disease Prediction** — Real-time risk prediction using a pre-trained scikit-learn ML model
- 📊 **CSV Dataset Support** — Includes the Heart Disease UCI dataset for model training and exploration
- 🧠 **Conversation Memory** — Maintains full chat history within the session
- 🎨 **Clean Streamlit UI** — Simple, responsive web interface — no frontend skills needed
- 🔐 **Secure API Key Handling** — API keys managed via `.env` file, never hardcoded
- ⚡ **Fast Responses** — Lightweight Gemini Flash model for quick, accurate replies

---

## 🛠️ Technologies Used

| Category | Technology |
|---|---|
| **Frontend / UI** | Streamlit |
| **AI / LLM** | Google Gemini 2.0 Flash (`google-genai`) |
| **Machine Learning** | scikit-learn, joblib |
| **Data Processing** | pandas |
| **Environment Config** | python-dotenv |
| **Language** | Python 3.12 |
| **Dataset** | Heart Disease UCI Dataset (CSV) |

---

## 📋 Prerequisites

Before running this project, make sure you have:

- ✅ Python **3.10 or higher** installed
- ✅ A **Google Gemini API key** (free at [aistudio.google.com](https://aistudio.google.com/app/apikey))
- ✅ `pip` package manager
- ✅ Git (to clone the repository)

---

## 📦 Installation

Follow these steps exactly to get the project running on your machine:

### Step 1 — Clone the Repository

```bash
git clone https://github.com/sohail189/Medical-prediction-system.git
cd Medical-prediction-system
```

### Step 2 — Create a Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Set Up Your API Key

Create a `.env` file in the project root folder:

```bash
# Windows PowerShell
New-Item .env

# Mac / Linux
touch .env
```

Open `.env` and add your Gemini API key:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

> 🔑 Get your free API key at: https://aistudio.google.com/app/apikey

### Step 5 — Run the App

```bash
streamlit run healthapp.py
```

Your browser will open automatically at **http://localhost:8501** 🎉

---

## 🚀 Usage

### 💬 Chat Mode — Ask Medical Questions

Simply type any health-related question in the chat box:

```
What are the symptoms of heart disease?
What is the difference between angina and a heart attack?
How can I reduce my cholesterol naturally?
```

### 🔬 Prediction Mode — Get Heart Disease Risk Assessment

Type `predict:` followed by your patient data as `key=value` pairs separated by commas:

```
predict: age=55, sex=1, cp=3, trestbps=130, chol=240, fbs=0, restecg=1, thalach=150, exang=0, oldpeak=2.3, slope=2, ca=0, thal=2
```

**Response example:**
```
⚠️ High risk of heart disease detected. Please consult a doctor.
```
or
```
✅ Low risk of heart disease. Keep maintaining a healthy lifestyle!
```

### 📊 Dataset Features (Input Parameters)

| Feature | Description | Type |
|---|---|---|
| `age` | Age in years | Integer |
| `sex` | Sex (1=male, 0=female) | Binary |
| `cp` | Chest pain type (0–3) | Integer |
| `trestbps` | Resting blood pressure (mm Hg) | Integer |
| `chol` | Serum cholesterol (mg/dl) | Integer |
| `fbs` | Fasting blood sugar > 120 mg/dl (1=true) | Binary |
| `restecg` | Resting ECG results (0–2) | Integer |
| `thalach` | Maximum heart rate achieved | Integer |
| `exang` | Exercise-induced angina (1=yes) | Binary |
| `oldpeak` | ST depression induced by exercise | Float |
| `slope` | Slope of peak exercise ST segment (0–2) | Integer |
| `ca` | Number of major vessels (0–3) | Integer |
| `thal` | Thalassemia type (1–3) | Integer |

---

## ⚙️ Configuration

### Environment Variables

| Variable | Required | Description |
|---|---|---|
| `GEMINI_API_KEY` | ✅ Yes | Your Google Gemini API key |

### `.env` File Example

```env
GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

> ⚠️ **Never commit your `.env` file to GitHub!** It is already listed in `.gitignore`.

---

## 📁 Project Structure

```
Medical-prediction-system/
│
├── healthapp.py          ← Main Streamlit application
├── Questions.py          ← Helper questions / data input module
├── my_model.pkl          ← Pre-trained ML model (scikit-learn)
├── heart (1).csv         ← Heart disease dataset (UCI)
├── requirements.txt      ← Python dependencies
├── .env                  ← API keys (NOT committed to git)
├── .gitignore            ← Files excluded from git
├── README.md             ← Project documentation
└── README                ← Plain text readme
```

---

## 🖥️ Demo

### Chat Interface
> 💡 *Add a screenshot of your app here*

```
![App Screenshot](screenshots/chat_demo.png)
```

### Prediction Output
> 💡 *Add a screenshot of prediction result here*

```
![Prediction Screenshot](screenshots/prediction_demo.png)
```

---

## 📄 Requirements

Full list of dependencies (`requirements.txt`):

```txt
streamlit
google-genai
scikit-learn
pandas
joblib
python-dotenv
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 🔧 Troubleshooting

| Problem | Solution |
|---|---|
| `File does not exist: healthapp.py` | Make sure you `cd` into the project folder first |
| `Gemini API key missing` | Create `.env` file and add `GEMINI_API_KEY=your_key` |
| `FutureWarning: google.generativeai` | Run `pip install google-genai` and update imports |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| App not opening in browser | Manually go to `http://localhost:8501` |

---

## 🤝 Contributing

Contributions are welcome and appreciated! Here's how to get started:

1. **Fork** the repository
2. **Clone** your fork:
   ```bash
   git clone https://github.com/your-username/Medical-prediction-system.git
   ```
3. **Create** a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make** your changes and commit:
   ```bash
   git commit -m "Add: your feature description"
   ```
5. **Push** to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open** a Pull Request on GitHub

### 💡 Ideas for Contribution

- [ ] Add more disease prediction models (diabetes, cancer, etc.)
- [ ] Add patient history saving with a database
- [ ] Add data visualisation charts for prediction confidence
- [ ] Add multi-language support
- [ ] Improve UI with custom CSS styling
- [ ] Add user authentication

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

```
MIT License — free to use, modify, and distribute with attribution.
```

---

## 📬 Contact

**Sohail** — [@sohail189](https://github.com/sohail189)

🔗 Project Link: [https://github.com/sohail189/Medical-prediction-system](https://github.com/sohail189/Medical-prediction-system)

---

<div align="center">

Made with ❤️ and Python

⭐ **Star this repo if you found it helpful!** ⭐

</div>
