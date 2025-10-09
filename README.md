The Filter: An Intelligent Shield Against Digital Deception ✨
<p align="center">
A multi-feature web application built with Python and Streamlit that leverages Natural Language Processing (NLP) and Machine Learning to detect various forms of misleading and harmful online content.
</p>

Developed By

Radhika Agarwal

Gaurav Singh

Lakshya Nigam

Dhruv Raj Kaushik

🚀 Live Application

The application is deployed and can be accessed here:

<!-- IMPORTANT: Replace the link above with the live URL of your deployed Streamlit app! -->

📸 Application Demo

<p align="center">
<img src="https://YOUR_GIF_LINK_HERE.gif" alt="App Demo GIF" width="800"/>
</p>

<!-- Add a GIF of your app in action here. Use a tool like Giphy Capture or ScreenToGif, upload the GIF to your repository, and replace the link above. -->

🎯 Project Vision

The vision behind The Filter is to empower everyday internet users with a simple, accessible, and intelligent tool to navigate the digital world safely. By hiding the complexity of machine learning behind a beautiful and intuitive interface, the app aims to foster digital literacy and build resilience against the growing threat of online deception.

✨ Key Features
The Filter integrates three distinct, high-accuracy machine learning models into one seamless user experience, allowing users to select a tool from a central dropdown menu.

📧 Spam Classifier: Analyzes an email or SMS message to determine if it is unwanted spam.

📰 Fake News Detector: Verifies a news article's content to check for signs of misinformation and fake news.

🤬 Toxic Comment Detector: Scans online comments for toxic or harmful language, helping to identify abusive content.

🛠️ Technology Stack
This project was built using a modern, open-source technology stack, focusing on Python for its powerful data science and machine learning libraries.

<p align="center">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Python-3.9%252B-blue%3Fstyle%3Dfor-the-badge%26logo%3Dpython" alt="Python Badge">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/scikit--learn-%2523F7931E.svg%3Fstyle%3Dfor-the-badge%26logo%3Dscikit-learn%26logoColor%3Dwhite" alt="Scikit-learn Badge">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Streamlit-FF4B4B%3Fstyle%3Dfor-the-badge%26logo%3DStreamlit%26logoColor%3Dwhite" alt="Streamlit Badge">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/NLTK-3.8-yellowgreen%3Fstyle%3Dfor-the-badge" alt="NLTK Badge">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Pandas-1.5-blueviolet%3Fstyle%3Dfor-the-badge%26logo%3Dpandas" alt="Pandas Badge">
</p>

Backend & Machine Learning:

Python: The core programming language.

Scikit-learn: For building, training, and evaluating all classification models.

Pandas: For high-performance data loading, manipulation, and analysis.

NLTK (Natural Language Toolkit): For all core NLP tasks, including tokenization, stopword removal, and stemming.

Frontend Web Application:

Streamlit: Used to rapidly build and serve the interactive, user-friendly web interface with custom styling.

Development & Deployment:

Jupyter Notebook: For initial data exploration and model experimentation.

PyCharm: As the primary IDE for application development.

GitHub: For version control and as the central code repository.

Streamlit Cloud / Hugging Face Spaces: For free, continuous deployment and global hosting.

⚙️ System Workflow
The application follows a standard and efficient machine learning workflow from user input to final prediction:

User Input: The user selects a tool (e.g., "Fake News Detector") from the dropdown menu and pastes their desired text into the text area.

Text Preprocessing: The raw text is passed to a unified transform_text function. This function performs a series of cleaning steps:

Converts text to lowercase.

Tokenizes the text into individual words.

Removes all punctuation and non-alphanumeric characters.

Filters out common English "stopwords."

Performs stemming using SnowballStemmer to reduce words to their root form (e.g., "running" -> "run").

Vectorization: The cleaned text is then fed into the appropriate pre-trained TfidfVectorizer model (.pkl file), which converts the processed text into a numerical vector.

Prediction: The resulting vector is passed to the corresponding trained classification model (.pkl file), which outputs a prediction (e.g., 1 for "Fake" or 0 for "Real").

Display Result: The application's front-end interprets this prediction and displays a clear, color-coded, and easy-to-understand result to the user.
