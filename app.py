import streamlit as st
from utils.parser import extract_text
from utils.generator import generate_summary, generate_goals, generate_mcqs

st.title("🧠 Personal Productivity AI Coach")

uploaded_file = st.file_uploader("📄 Upload your work journal (.pdf or .md)", type=["pdf", "md"])

if uploaded_file:
    content = extract_text(uploaded_file)

    st.subheader("📝 Document Summary")
    summary = generate_summary(content)
    st.write(summary)

    st.subheader("🎯 Suggested Daily Goals")
    for goal in generate_goals(content):
        st.markdown(f"- {goal}")

    st.subheader("❓ Recall Quiz (MCQs)")
    for mcq in generate_mcqs(content):
        st.markdown(mcq)
