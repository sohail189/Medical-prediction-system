# Medical Prediction System

A web-based health assistant that combines a machine learning model with an AI chatbot to help users understand their heart disease risk. Built with Python and Streamlit.

> **Important:** This tool is for educational purposes only and is not a substitute for professional medical advice. Always consult a qualified doctor for health concerns.

---

## What It Does

This project has two main features:

**1. Heart Disease Risk Prediction**
Enter basic patient information and the system will instantly tell you whether you are at low or high risk of heart disease. The prediction is powered by a pre-trained scikit-learn model trained on the Heart Disease UCI dataset.

**2. AI Medical Chatbot**
Ask any heart-health related question in plain English and get a clear, conversational response. The chatbot is powered by Google Gemini 2.0 Flash and remembers your conversation throughout the session.

---

## Technologies Used

- **Python 3.12**
- **Streamlit** — for the web interface
- **Google Gemini 2.0 Flash** — for the AI chatbot
- **scikit-learn** — for the prediction model
- **pandas** — for data handling
- **python-dotenv** — for secure API key management

---

## Getting Started

### What You Need Before Starting

- Python 3.10 or higher installed on your machine
- A free Google Gemini API key — get one at [aistudio.google.com](https://aistudio.google.com/app/apikey)
- Git installed

### Installation Steps

**1. Clone the repository**

```bash
git clone https://github.com/sohail189/Medical-prediction-system.git
cd Medical-prediction-system
```

**2. Create a virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac / Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Add your API key**

Create a `.env` file in the project root and add the following line:

```
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

Never share or commit this file to GitHub.

**5. Run the app**

```bash
streamlit run healthapp.py
```

The app will open in your browser at `http://localhost:8501`.

---

## How to Use It

### Chatbot Mode

Just type any medical question into the chat box:

```
What are the early symptoms of heart disease?
How does high cholesterol affect the heart?
What lifestyle changes reduce heart attack risk?
```

### Prediction Mode

Type `predict:` followed by patient data as key-value pairs:

```
predict: age=55, sex=1, cp=3, trestbps=130, chol=240, fbs=0, restecg=1, thalach=150, exang=0, oldpeak=2.3, slope=2, ca=0, thal=2
```

The system will respond with either a low-risk or high-risk assessment.

### Input Parameters Explained

| Parameter | What It Means |
|-----------|--------------|
| age | Patient age in years |
| sex | 1 = Male, 0 = Female |
| cp | Chest pain type (0 to 3) |
| trestbps | Resting blood pressure (mm Hg) |
| chol | Cholesterol level (mg/dl) |
| fbs | Fasting blood sugar above 120 mg/dl (1 = yes) |
| restecg | Resting ECG result (0 to 2) |
| thalach | Maximum heart rate achieved |
| exang | Exercise-induced angina (1 = yes) |
| oldpeak | ST depression from exercise |
| slope | Slope of ST segment (0 to 2) |
| ca | Number of major vessels (0 to 3) |
| thal | Thalassemia type (1 to 3) |

---

## Project Structure

```
Medical-prediction-system/
│
├── healthapp.py          # Main application file
├── Questions.py          # Data input helper module
├── my_model.pkl          # Trained ML model
├── heart (1).csv         # Heart disease dataset
├── requirements.txt      # Project dependencies
├── .env                  # Your API key (not committed to git)
├── .gitignore            # Files excluded from version control
└── README.md             # Project documentation
```

---

## Common Issues

| Problem | Fix |
|---------|-----|
| App says healthapp.py not found | Make sure you are inside the project folder before running |
| Gemini API key error | Check that your .env file exists and the key is correct |
| Module not found error | Run `pip install -r requirements.txt` again |
| Browser does not open | Manually visit `http://localhost:8501` |

---

## Future Plans

- Add prediction models for diabetes and other conditions
- Save patient history to a database
- Add charts showing prediction confidence
- Support multiple languages
- Add user login and authentication

---

## License

This project is open source under the MIT License. You are free to use, modify, and share it with attribution.

---

## Contact

**Sohail** — [github.com/sohail189](https://github.com/sohail189)

Project Repository: [github.com/sohail189/Medical-prediction-system](https://github.com/sohail189/Medical-prediction-system)
