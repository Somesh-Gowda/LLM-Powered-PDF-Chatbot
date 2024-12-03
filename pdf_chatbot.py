import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
from PyPDF2 import PdfReader

HUGGINGFACE_TOKEN = "YOUR_HUGGINGFACE_TOKEN"

MODEL_NAME = "meta-llama/Llama-3.2-1B"

@st.cache_resource
def load_model_and_tokenizer(model_name):
    tokenizer = AutoTokenizer.from_pretrained(
        model_name, use_auth_token=HUGGINGFACE_TOKEN
    )
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        use_auth_token=HUGGINGFACE_TOKEN,
        device_map="auto",
        torch_dtype="auto"
    )
    return tokenizer, model

tokenizer, model = load_model_and_tokenizer(MODEL_NAME)

def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_new_tokens=150, temperature=0.7)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response


st.title("Chat with Your PDF")
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with st.spinner("Extracting text from PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)
    
    st.text_area("Extracted PDF Content", pdf_text, height=300)
    
    user_query = st.text_input("Ask something about the PDF content:")
    if user_query:
        with st.spinner("Generating response..."):
            prompt = f"Based on the following PDF content, answer the question:\n\n{pdf_text}\n\nQuestion: {user_query}\nAnswer:"
            response = generate_response(prompt)
            st.text_area("Response", response, height=200)
