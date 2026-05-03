import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

st.title("Spam Email Classifier")

# FIXED dataset loading
data = pd.read_csv(
    "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv",
    sep="\t",
    header=None
)

# ADD column names
data.columns = ["label", "message"]

# Now this works
X = data["message"]
y = data["label"].map({"ham": 0, "spam": 1})

vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vectorized, y)

st.write("Model trained successfully ✅")
# User input
email = st.text_area("Enter your email message:")

# Button
if st.button("Predict"):
    if email.strip() == "":
        st.warning("Please enter some text")
    else:
        input_data = vectorizer.transform([email])
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error("🚫 Spam Email")
        else:
            st.success("✅ Not Spam")