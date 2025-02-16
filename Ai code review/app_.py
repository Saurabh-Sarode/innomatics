import google.generativeai as genai
import streamlit as st

genai.configure(api_key="AIzaSyDyrbMxCVdUS7whn2MxrcbZ7etwgiOX6ps")  

def review_code(user_code):
    """Send user code to Gemini AI and return only the corrected version."""
    prompt = f"Fix any errors or improve this Python code. Return only the corrected code without any explanations:\n```python\n{user_code}\n```"
    
    response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
    return response.text  
st.set_page_config(page_title="AI Code Reviewer", layout="wide")

st.title("🔍 AI-Powered Python Code Reviewer")
st.write("Enter your Python code below and get an improved version with fixes.")
user_code = st.text_area("Write your Python code here:", height=250)

if st.button("Review Code"):
    if user_code.strip():
        with st.spinner("Analyzing and fixing code... Please wait..."):
            corrected_code = review_code(user_code)
        
        st.subheader("Corrected Code:")
        st.code(corrected_code, language="python")
    else:
        st.warning(" Please enter some code before submitting!")
