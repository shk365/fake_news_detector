import streamlit as st
import joblib
import os

# Load model and vectorizer
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, '..', 'model', 'fake_news_model.pkl')
tfidf_path = os.path.join(BASE_DIR, '..', 'model', 'tfidf.pkl')

model = joblib.load(model_path)
vectorizer = joblib.load(tfidf_path)

# Streamlit UI
st.title("Fake News Detector")
st.write("Paste any news article below and check if it's **Real** or **Fake**.")

# Input text
user_input = st.text_area("Enter News Text", height=200)

if st.button("Check News"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Transform text and predict
        transformed = vectorizer.transform([user_input])
        prediction = model.predict(transformed)[0]

        if prediction == "FAKE":
            st.error("This news is likely **FAKE**.")
        else:
            st.success("This news appears to be **REAL**.")
 
