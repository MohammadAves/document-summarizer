import streamlit as st
from summarizer import summarize_text

st.title("Document Summarization Service 📝")


text_input = st.text_area("Enter text to summarize:", height=200)
summary_style = st.selectbox("Select summarization style:", ["brief", "detailed", "bullet"])

if st.button("Summarize"):
    if not text_input.strip():
        st.warning("Please enter some text to summarize.")
    else:
        summary = summarize_text(text_input, style=summary_style)
        st.subheader("Summary:")
        st.write(summary)




