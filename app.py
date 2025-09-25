import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from streamlit_lottie import st_lottie
import requests

# --- NLTK Data Download ---
# This is a simpler and more reliable way to ensure the data is present.
# If the data is already downloaded, NLTK will skip the download.
nltk.download('punkt')
nltk.download('stopwords')


# --- LOTTIE ANIMATION ---
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url = "https://assets5.lottiefiles.com/packages/lf20_t24jcswl.json"
lottie_json = load_lottieurl(lottie_url)

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Spam Shield",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- STYLING ---
st.markdown("""
<style>
    /* Main app background */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    /* Text area styling */
    .stTextArea textarea {
        background-color: #262730;
        color: #FAFAFA;
        border-radius: 10px;
        border: 1px solid #4A4A4A;
    }
    /* Button styling */
    .stButton>button {
        background-color: #4CAF50; /* Green */
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049; /* Darker Green */
    }
    /* Custom headers */
    .spam-header {
        color: #FF4B4B; /* Red for Spam */
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
    }
    .not-spam-header {
        color: #28A745; /* Green for Not Spam */
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# --- TEXT TRANSFORMATION FUNCTION ---
ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = [i for i in text if i.isalnum()]
    text = [i for i in y if i not in stopwords.words('english') and i not in string.punctuation]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)


# --- LOAD MODEL AND VECTORIZER ---
try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except FileNotFoundError:
    st.error(
        "Model or vectorizer files not found. Please ensure 'vectorizer.pkl' and 'model.pkl' are in the root directory.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the model files: {e}")
    st.stop()

# --- APP LAYOUT ---
st.markdown("<h1 style='text-align: center;'>📧 Spam Shield: Email/SMS Classifier</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter a message below to check if it's spam or not.</p>",
            unsafe_allow_html=True)

# Display Lottie Animation
if lottie_json:
    st_lottie(lottie_json, speed=1, height=200, key="initial")

input_sms = st.text_area("Enter your message here...", height=150)

if st.button('Analyze Message'):
    if not input_sms.strip():
        st.warning("Please enter a message to analyze.")
    else:
        with st.spinner('Analyzing...'):
            # 1. Preprocess
            transformed_sms = transform_text(input_sms)
            # 2. Vectorize
            vector_input = tfidf.transform([transformed_sms])
            # 3. Predict
            result = model.predict(vector_input)[0]

            # 4. Display Result
            if result == 1:
                st.markdown("<h2 class='spam-header'>🚨 Spam Detected!</h2>", unsafe_allow_html=True)
            else:
                st.markdown("<h2 class='not-spam-header'>✅ Not Spam (Safe)</h2>", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.header("About Spam Shield")
    st.write("""
    This application uses a Machine Learning model to classify messages as either 'Spam' or 'Not Spam'.

    **How it works:**
    1. You enter a message.
    2. The message is preprocessed (cleaned and stemmed).
    3. The cleaned text is converted into numerical vectors.
    4. The model predicts the classification based on these vectors.
    """)
    st.header("Libraries Used")
    st.write("- Streamlit\n- Scikit-learn\n- NLTK\n- Pickle")