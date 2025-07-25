import streamlit as st
import requests

st.set_page_config(page_title="Document Summarizer", page_icon="📄", layout="centered")
st.title("📄 Document Summarizer")
st.markdown("""
Upload a PDF or image (JPEG/PNG) and get a concise summary using state-of-the-art AI models (T5 or BART).
""")

backend_url = "http://localhost:8000/upload/"

with st.form("upload_form", clear_on_submit=True):
    uploaded_file = st.file_uploader("Choose a PDF or image file", type=["pdf", "png", "jpg", "jpeg"], help="Supported: PDF, PNG, JPG, JPEG")
    model = st.selectbox("Select summarization model", ["t5", "bart"], index=0)
    submit = st.form_submit_button("Summarize", use_container_width=True)

if submit and uploaded_file:
    with st.spinner("Uploading and summarizing..."):
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        data = {"model": model}
        try:
            response = requests.post(backend_url, files=files, data=data)
            if response.status_code == 200:
                summary = response.json().get("summary", "No summary returned.")
                st.success("Summary:")
                st.markdown(f"<div style='background:#f6f8fa;padding:1em;border-radius:8px;font-size:1.1em'>{summary}</div>", unsafe_allow_html=True)
            else:
                st.error(f"Error: {response.json().get('error', 'Unknown error')}")
        except Exception as e:
            st.error(f"Failed to connect to backend: {e}")
else:
    st.markdown("<br><sub>Powered by T5 & BART transformers. Developed with ❤️ using FastAPI & Streamlit.</sub>", unsafe_allow_html=True) 