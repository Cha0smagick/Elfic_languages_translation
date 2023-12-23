import streamlit as st
import re
import google.generativeai as genai
from IPython.display import display, Markdown

# Set up the Google GEMINI API
genai.configure(api_key='google_api_key')  # Replace with your Gemini API key

# Define a function to clean text
def clean_text(text):
    # Clean punctuation and special characters using regular expressions
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return cleaned_text

# Define a function to translate text to Elvish languages
def translate_to_elvish(text, target_language):
    try:
        # Generate translation using the GEMINI model
        response = model.generate_content(f"Translate '{text}' to {target_language}", stream=True)

        # Extract the translated response
        translated_text = ""
        for chunk in response:
            translated_text += chunk.text

        return translated_text

    except Exception as e:
        return f"Translation Error: {str(e)}"

# Streamlit UI
st.title("Elvish Language Translator")

# User input
user_input = st.text_input("Enter the text to translate:")
target_language = st.selectbox("Select Elvish Language:", ["Quenya", "Quenya Exilic", "Telerin", "Nandorin", "Avarin", "Common Telerin", "Common Eldarin", "Primitive Quendian"])

if st.button("Translate"):
    # Clean the user input
    cleaned_input = clean_text(user_input)

    if not cleaned_input:
        st.warning("Invalid input. Please enter some text to translate.")
    else:
        # Define the GEMINI model for translation
        model = genai.GenerativeModel('gemini-pro')

        # Translate the input to the selected Elvish language
        translated_text = translate_to_elvish(cleaned_input, target_language)

        if "Translation Error" in translated_text:
            st.error(translated_text)
        else:
            st.success(f"Translated text in {target_language}: {translated_text}")

# Additional information about the app
st.markdown("This app uses the Google GEMINI API to translate text into various Elvish languages, including Quenya, Quenya Exilic, Telerin, Nandorin, Avarin, Common Telerin, Common Eldarin, and Primitive Quendian, as inspired by J.R.R. Tolkien's works.")
st.markdown("Powered by Google GEMINI")

# Add any other information or links here
