
import os
import streamlit as st

from agents.code_analyzer import analyze_project
from agents.doc_generator import generate_doc
from utils.uml import generate_uml

st.set_page_config(page_title="Enterprise Auto Doc Agent", layout="wide")

st.title("🚀 Enterprise AI Doc Agent")

uploaded = st.file_uploader("Upload Python file or project zip", type=["py","zip"])

if st.button("Run Agent Pipeline"):

    if not uploaded:
        st.warning("upload file first")
        st.stop()

    path = os.path.join("demo_project", uploaded.name)
    with open(path, "wb") as f:
        f.write(uploaded.read())

    analysis = analyze_project(path)
    doc = generate_doc(analysis)

    st.subheader("📊 Analysis")
    st.text_area("", analysis, height=200)

    st.subheader("📄 Documentation")
    st.text_area("", doc, height=300)

    st.subheader("🧠 UML (Mermaid)")
    st.code(generate_uml(analysis), language="markdown")
