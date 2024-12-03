# LLM-Powered-PDF-Chatbot 

### **Chat with Your PDF Using Streamlit and Hugging Face**
---

## **Introduction**  
LLM-Powered PDF Chatbot is an AI-driven solution that allows users to upload PDF documents and interact with them by asking questions. Powered by Hugging Face's Llama model, the chatbot extracts text from PDF files and generates intelligent, context-specific responses.  

---

## **Overview**  
This project is built using:  
- **Streamlit**: For creating an interactive web-based user interface.  
- **Transformers**: To utilize the Llama model from Hugging Face.  
- **PyPDF2**: To extract text from PDF files.  

**Key Features**:  
- Upload PDF files and extract their content.  
- Ask questions related to the PDF's content.  
- Receive AI-generated responses using a large language model.  

---

## **Installation**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/Somesh-Gowda/LLM-Powered-PDF-Chatbot.git
cd LLM-Powered-PDF-Chatbot
```  

### **2. Set Up a Virtual Environment** (Optional but recommended)  
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```  

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```  

---

## **Setting Up Hugging Face Token ID**  

1. **Sign Up on Hugging Face**:  
   Create an account at [Hugging Face](https://huggingface.co/) if you don't have one.

2. **Generate Your Token**:  
   - Navigate to **Settings** > **Access Tokens**.  
   - Click **New Token** and generate a read token.  

3. **Update the Token in Code**:  
   Replace `"YOUR_HUGGINGFACE_TOKEN"` with your token:  
   ```python
   HUGGINGFACE_TOKEN = "your_generated_token"
   ```

---

## **Running the Model**  

### **1. Start the Streamlit App**  
```bash
streamlit run app.py
```  

### **2. Upload a PDF & Interact**  
- Use the file uploader to select a PDF.  
- Extracted PDF content will be displayed.  
- Ask questions, and the chatbot will generate responses based on the content.

---

## **Sample Output**  

### **Extracted PDF Content (Example)**  
```
The PDF discusses the evolution of artificial intelligence and its applications in various industries...
```

### **User Query**  
```
What are the main applications of AI in healthcare?
```

### **AI-Generated Response**  
```
AI is being used in healthcare for predictive analytics, diagnostics, personalized medicine, and automated image analysis...
```
