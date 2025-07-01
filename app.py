# app.py
import streamlit as st
import json
from utils import call_model_api, calculate_token_usage

# Load prompt styles
with open("prompts.json") as f:
    prompt_templates = json.load(f)

st.set_page_config(page_title="Prompt Optimization Toolkit", layout="wide")
st.title("📊 Prompt Optimization Toolkit")
st.markdown("Compare different prompt styles and LLM responses side-by-side using Groq API.")

# Sidebar settings
st.sidebar.header("🔧 Settings")
api_key = st.sidebar.text_input("🔑 Groq API Key", type="password")
model_1 = st.sidebar.selectbox("Model A", ["llama3-70b-8192", "mixtral-8x7b-32768"])
model_2 = st.sidebar.selectbox("Model B", ["mixtral-8x7b-32768", "llama3-70b-8192"])
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("Max Tokens", 100, 2048, 512)

# Main input
col1, col2 = st.columns(2)

with col1:
    st.subheader("🧾 Choose Prompt Style")
    style = st.selectbox("Prompt Template", list(prompt_templates.keys()))
    prompt = st.text_area("🔤 Prompt Text", prompt_templates[style], height=200)

with col2:
    st.subheader("📌 Prompt Summary")
    st.markdown(f"**Template Style:** `{style}`")
    st.markdown(f"**Characters:** `{len(prompt)}` | **Words:** `{len(prompt.split())}`")

# Generate button
if st.button("🚀 Compare Models"):
    if not api_key:
        st.error("❌ API key is missing.")
    else:
        with st.spinner("⏳ Fetching responses from models..."):
            result_1 = call_model_api(api_key, model_1, prompt, temperature, max_tokens)
            result_2 = call_model_api(api_key, model_2, prompt, temperature, max_tokens)

        col1, col2 = st.columns(2)
        with col1:
            st.success(f"Model A: {model_1}")
            st.write(result_1['response'])
            st.caption(f"Tokens used: {result_1['tokens']}")
        with col2:
            st.success(f"Model B: {model_2}")
            st.write(result_2['response'])
            st.caption(f"Tokens used: {result_2['tokens']}")
