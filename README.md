📧 Spam Email Classifier

A machine learning project that classifies emails as Spam or Not Spam (Ham) using TF-IDF vectorization and Naive Bayes algorithm.

---

🚀 Overview

This project demonstrates how machine learning can be applied to detect spam emails.
It processes text data, converts it into numerical form, and trains a classification model to make predictions.

---

🧠 Technologies & Libraries Used

- Python
- NumPy
- Pandas
- Scikit-learn

🔍 Key Concepts

- TF-IDF Vectorization
- Naive Bayes Classifier
- Train-Test Split
- Model Evaluation Metrics

---

📂 Project Structure

spam-email-classifier/
│
├── spam_classifier.ipynb   # Jupyter Notebook (with explanation & output)
├── spam_classifier.py      # Python script version
└── README.md

---

📊 Dataset

The dataset is loaded using an online URL.

It contains labeled email messages categorized as:

- Spam
- Not Spam (Ham)

---

⚙️ How It Works

1. Load dataset using Pandas
2. Preprocess text data
3. Convert text into numerical features using TF-IDF
4. Split data using train_test_split
5. Train model using Naive Bayes
6. Evaluate using:
   - Accuracy Score
   - Confusion Matrix
   - Classification Report

---

▶️ How to Run

🔹 Option 1: Jupyter Notebook

Open and run:

spam_classifier.ipynb

🔹 Option 2: Python Script

Install dependencies:

pip install numpy pandas scikit-learn

Run the file:

python spam_classifier.py

---

📈 Model Evaluation

The model performance is evaluated using:

- Accuracy Score
- Confusion Matrix
- Classification Report

These metrics help measure how well the model classifies spam and non-spam emails.

---

💡 Example

Input:
"Congratulations! You have won a prize"

Output:
Spam

---

🎯 Conclusion

This project shows how TF-IDF and Naive Bayes can be effectively used for spam detection tasks using text data.

---

🔮 Future Improvements

- Improve accuracy with advanced models
- Use larger datasets
- Deploy as a web application
- Add GUI interface

---

👤 Author

Vaidik Joshi
