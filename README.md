📧 Spam Email Classifier

A machine learning-based web application that classifies email messages as Spam or Not Spam (Ham) using TF-IDF vectorization and Naive Bayes algorithm.

---

🚀 Live Demo

🔗 Try the app here:
https://spam-email-classifier-n4vlkxpjzke42tcujuvelg.streamlit.app/
This web app allows users to enter an email message and instantly classify it as Spam or Not Spam

---

🧠 Project Overview

This project demonstrates how machine learning and text processing techniques can be used to detect spam emails. The application processes raw text input, converts it into numerical features, and predicts whether the message is spam or legitimate.

---

⚙️ Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Streamlit

---

🔍 Key Concepts

- TF-IDF Vectorization
- Naive Bayes Classification
- Train-Test Split
- Text Classification

---

📊 Dataset

- Dataset loaded from an online URL
- Contains labeled messages:
  - Spam
  - Not Spam (Ham)

---

🏗️ Project Structure

spam-email-classifier/
│
├── spam_classifier.ipynb   # Jupyter Notebook (analysis & development)
├── spam_classifier.py      # Python script version
├── app.py                  # Streamlit web application
└── requirements.txt        # Dependencies

---

▶️ How to Run Locally

1. Install dependencies

pip install -r requirements.txt

2. Run the app

streamlit run app.py

---

🌐 Web Application

The project is deployed as an interactive web app using Streamlit.

Users can:

- Enter an email message
- Click "Predict"
- Instantly see whether it is Spam or Not Spam

---

📈 Model Details

- Text is converted into numerical features using TF-IDF
- A Naive Bayes classifier is trained on labeled data
- The model predicts spam probability based on learned patterns

---

💡 Example

Input:
Congratulations! You have won a prize

Output:
🚫 Spam

---

🎯 Conclusion

This project demonstrates a practical implementation of machine learning for spam detection and showcases how models can be deployed as interactive web applications.

---

🔮 Future Improvements

- Improve model accuracy with advanced algorithms
- Save and reuse trained model (optimize performance)
- Enhance UI design
- Deploy with custom domain

---

👤 Author

Vaidik Joshi
