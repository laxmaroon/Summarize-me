import os
import streamlit as st
from dotenv import load_dotenv, find_dotenv
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain, OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import YoutubeLoader, NewsURLLoader
from pypdf import PdfReader
from langchain.schema import Document
from langchain.chains import AnalyzeDocumentChain
from htmlTemplates import css, bot_template
import textwrap

load_dotenv(find_dotenv())
HUGGINGFACEHUB_API_TOKEN = os.environ["HUGGINGFACEHUB_API_TOKEN"]

repo_id = "tiiuae/falcon-7b-instruct"  # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options
falcon_llm = HuggingFaceHub(
    repo_id=repo_id, model_kwargs={"temperature": 0.1, "max_new_tokens": 500}
)

def handle_userinputYT(user_url):
    # video_url = "https://www.youtube.com/watch?v=riXpu1tHzl0"
    loader = YoutubeLoader.from_youtube_url(user_url)
    transcript = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000)
    docs = text_splitter.split_documents(transcript)

    return docs

def handle_userinputNA(user_url):
    loader = NewsURLLoader(
        urls = [user_url]
    )
    transcript = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000)
    docs = text_splitter.split_documents(transcript)

    return docs

def handle_userinputPDF(pdf_docs):
    # docs = []  # List to store individual documents

    # for pdf in pdf_docs:
    #     pdf_reader = PdfReader(pdf)
    #     for page in pdf_reader.pages:
    #         # Create a document for each page and append it to the list
    #         page_text = page.extract_text()
    #         doc = Document(page_content=page_text)
    #         docs.append(doc)
    docs = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            docs += page.extract_text()
    return docs

def summarize(docs):
    chain = load_summarize_chain(falcon_llm, chain_type="map_reduce", verbose=True)
    output_summary = chain.run(docs)
    wrapped_text = textwrap.fill(
        output_summary, width=100, break_long_words=False, replace_whitespace=False
    )
    st.write(bot_template.replace("{{MSG}}", wrapped_text), unsafe_allow_html = True)
    return wrapped_text

def summarizePDFs(docs):
    chain = load_summarize_chain(falcon_llm, chain_type="map_reduce", verbose=True)
    summarize_document_chain = AnalyzeDocumentChain(combine_docs_chain=chain)
    output_summary = summarize_document_chain.run(docs)
    wrapped_text = textwrap.fill(
        output_summary, width=100, break_long_words=False, replace_whitespace=False
    )
    st.write(bot_template.replace("{{MSG}}", wrapped_text), unsafe_allow_html = True)
    return wrapped_text

def main():
    load_dotenv()
    st.set_page_config(page_title = "Summarize me", page_icon = ":sparkles:")
 
    st.write(css, unsafe_allow_html = True)
    st.header("Summarize me :sparkles:")
    st.markdown("### Youtube Videos :tv:")
    user_url = st.text_input("Enter the url here:", key = "1")
    if user_url:
        docs = handle_userinputYT(user_url)
        summ = summarize(docs)
    
    st.markdown("### News Articles :newspaper:")
    user_url = st.text_input("Enter the url here:", key = "2")
    if user_url:
        docs = handle_userinputNA(user_url)
        summ = summarize(docs)

    st.markdown("### PDF Documents 	:closed_book:")
    pdf_docs = st.file_uploader("Upload your PDFs here and clich on 'Process'", accept_multiple_files = True)
    if st.button("Process"):
        with st.spinner("Processing"):
            docs = handle_userinputPDF(pdf_docs)      
            summ = summarizePDFs(docs)

if __name__ == '__main__':
    main()
