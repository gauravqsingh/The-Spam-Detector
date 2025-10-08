import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="GuardianAI Pro",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- STYLING ---
# This CSS creates the animated gradient background, glassmorphism card, and custom widget styles.
st.markdown("""
<style>
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: #FFFFFF;
    }
    header, footer { visibility: hidden; }
    .main-container {
        background: rgba(0, 0, 0, 0.2);
        border-radius: 20px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.18);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    .title {
        font-family: 'Arial Black', sans-serif;
        text-align: center;
        font-size: 3.5em;
        color: #FFFFFF;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.6);
    }
    div[data-baseweb="select"] > div {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        color: #FFFFFF;
    }
    div[data-baseweb="select"] > div > div { color: #FFFFFF; }
    .stTextArea textarea {
        background-color: rgba(0, 0, 0, 0.3);
        color: #FFFFFF;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        font-size: 16px;
    }
    .stButton>button {
        background-color: #FFFFFF;
        color: #23a6d5;
        border: none;
        padding: 15px 30px;
        font-size: 1.2em;
        font-weight: bold;
        border-radius: 10px;
        transition: all 0.3s;
        width: 100%;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background-color: #e0e0e0;
    }
    .result-header {
        font-size: 2.2em; font-weight: bold; text-align: center;
        padding: 20px; border-radius: 10px; margin-top: 20px;
        color: white;
    }
    .negative-result { background-color: rgba(255, 75, 75, 0.7); }
    .positive-result { background-color: rgba(40, 167, 69, 0.7); }
    .footer {
        text-align: center;
        padding-top: 2rem;
        color: rgba(255, 255, 255, 0.7);
    }
</style>
""", unsafe_allow_html=True)


# --- TEXT PREPROCESSING FUNCTION ---
stemmer = SnowballStemmer('english')
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = [i for i in text if i.isalnum()]
    text = [i for i in y if i not in stopwords.words('english') and i not in string.punctuation]
    y.clear()
    for i in text:
        y.append(stemmer.stem(i))
    return " ".join(y)


# --- DICTIONARY TO HOLD MODEL INFO ---
MODELS = {
    "Spam Classifier": {
        "icon": "📧",
        "description": "Analyze an Email or SMS message to determine if it is spam.",
        "vectorizer_path": "vectorizer.pkl",
        "model_path": "model.pkl",
        "result_negative": "🚨 Spam Detected!",
        "result_positive": "✅ Not Spam (Safe)",
        "button_text": "Analyze Message"
    },
    "Fake News Detector": {
        "icon": "📰",
        "description": "Verify a news article's authenticity by pasting its content below.",
        "vectorizer_path": "fakenews_vectorizer.pkl",
        "model_path": "fakenews_model.pkl",
        "result_negative": "❌ Unreliable (Likely Fake News)",
        "result_positive": "✔️ Authentic (Likely Real News)",
        "button_text": "Verify News"
    },
    "Toxic Comment Detector": {
        "icon": "🤬",
        "description": "Analyze a comment (e.g., from social media) for toxic or harmful language.",
        "vectorizer_path": "toxic_vectorizer.pkl",
        "model_path": "toxic_model.pkl",
        "result_negative": "🤬 Toxic Comment Detected!",
        "result_positive": "👍 Non-Toxic Comment",
        "button_text": "Analyze Comment"
    }
}


# --- MAIN APP LAYOUT ---
st.markdown("<h1 class='title'>GuardianAI Pro ✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #FFFFFF;'>Your intelligent shield against digital deception.</h3>", unsafe_allow_html=True)

options = [f"{info['icon']} {name}" for name, info in MODELS.items()]
selection_str = st.selectbox(
    "Choose a tool from the dropdown menu:",
    options
)
app_mode = selection_str.split(" ", 1)[1]

with st.container():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)

    selected_model = MODELS[app_mode]
    st.header(f"{selected_model['icon']} {app_mode}")
    st.write(selected_model['description'])

    try:
        tfidf = pickle.load(open(selected_model['vectorizer_path'], 'rb'))
        model = pickle.load(open(selected_model['model_path'], 'rb'))
    except FileNotFoundError:
        st.error(f"Model files for '{app_mode}' not found! Please ensure they are uploaded.")
        st.stop()

    input_text = st.text_area("Enter the text to analyze:", height=200, key=f"{app_mode}_input")

    if st.button(selected_model['button_text'], key=f"{app_mode}_analyze"):
        if input_text.strip():
            with st.spinner('GuardianAI is analyzing...'):
                transformed = transform_text(input_text)
                vectorized = tfidf.transform([transformed])
                result = model.predict(vectorized)[0]

                if result == 1:
                    st.markdown(f"<div class='result-header negative-result'>{selected_model['result_negative']}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='result-header positive-result'>{selected_model['result_positive']}</div>", unsafe_allow_html=True)
        else:
            st.warning("Please enter some text to analyze.")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Developed with ❤️ for GuardianAI</div>", unsafe_allow_html=True)

