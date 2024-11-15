import os
import streamlit as st
import pickle
import time
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Check if API key is loaded
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.error("OpenAI API key not found. Please ensure it is in the .env file.")
else:
    st.success("OpenAI API key successfully loaded!")

st.title("RockyBot: News Research Tool 📈")
st.sidebar.title("News Article URLs")

# Input fields for URLs
urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store_openai.pkl"

main_placeholder = st.empty()

# Initialize the OpenAI LLM with the loaded API key
llm = OpenAI(api_key=openai_api_key, temperature=0.9, max_tokens=500)

# If the "Process URLs" button is clicked
if process_url_clicked:
    if not all(urls):  # Check if all URLs are provided
        st.error("Please enter all URLs.")
    else:
        try:
            # Load data from URLs
            loader = UnstructuredURLLoader(urls=urls)
            main_placeholder.text("Data Loading...Started...✅✅✅")
            data = loader.load()

            if not data:
                st.error("No data found. Please check the provided URLs.")
            else:
                # Split the data into chunks
                text_splitter = RecursiveCharacterTextSplitter(
                    separators=['\n\n', '\n', '.', ','],
                    chunk_size=1000
                )
                main_placeholder.text("Text Splitter...Started...✅✅✅")
                docs = text_splitter.split_documents(data)

                if not docs:
                    st.error("No text found to split. Please check the content of the URLs.")
                else:
                    # Create embeddings and save it to FAISS index
                    embeddings = OpenAIEmbeddings(api_key=openai_api_key)
                    try:
                        vectorstore_openai = FAISS.from_documents(docs, embeddings)
                        main_placeholder.text("Embedding Vector Started Building...✅✅✅")
                        time.sleep(2)

                        # Save the FAISS index to a pickle file
                        with open(file_path, "wb") as f:
                            pickle.dump(vectorstore_openai, f)
                        st.success("FAISS index created and saved successfully!")

                    except Exception as e:
                        st.error(f"Error creating FAISS index: {str(e)}")

        except Exception as e:
            st.error(f"Error loading data from URLs: {str(e)}")

# Query input
query = main_placeholder.text_input("Question: ")
if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
            result = chain({"question": query}, return_only_outputs=True)
            
            # Display result
            st.header("Answer")
            st.write(result["answer"])

            # Display sources, if available
            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                sources_list = sources.split("\n")  # Split the sources by newline
                for source in sources_list:
                    st.write(source)
