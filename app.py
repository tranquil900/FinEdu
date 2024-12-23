"""
Main Streamlit application file
"""

import streamlit as st
import pandas as pd
from config import *
from utils.document_processor import DocumentProcessor
from utils.financial_analyzer import FinancialAnalyzer
from utils.llm_handler import LLMHandler
from utils.data_aggregator import DataAggregator

def display_tables(tables: list, doc_processor, financial_analyzer) -> list:
    """Display and analyze tables"""
    table_dataframes = []
    if not tables:
        st.write("No tables found in the document.")
        return table_dataframes

    st.header("Extracted Tables")
    for i, table in enumerate(tables):
        st.subheader(f"Table {i + 1}")
        df = doc_processor.parse_table(table)
        if df is not None:
            st.dataframe(df, use_container_width=True)
            table_dataframes.append(df)

            # Display metrics
            metrics = financial_analyzer.calculate_basic_metrics(df)
            if metrics is not None:
                st.write("Calculated Metrics:")
                st.write(metrics)

            # Display ratios
            ratios = financial_analyzer.calculate_financial_ratios(df)
            if ratios:
                st.write("Financial Ratios:")
                for metric_name, metric_df in ratios.items():
                    st.write(metric_df)
        else:
            st.warning(f"Unable to parse Table {i + 1}.")
    
    return table_dataframes

# def display_texts(texts: list) -> list:
#     """Display extracted texts"""
#     st.header("Extracted Text")
#     extracted_texts = []
#     for i, text in enumerate(texts):
#         st.markdown(f"### Text Segment {i + 1}")
#         st.write(text.text)
#         extracted_texts.append(text.text)
#     return extracted_texts
def display_texts(texts: list) -> list:
    """Display extracted texts"""
    st.header("Extracted Text")
    extracted_texts = []
    for i, text in enumerate(texts):
        # st.markdown(f"### Text Segment {i + 1}")
        
        # Ensure text is a string
        if hasattr(text, 'text'):
            extracted_text = text.text
        else:
            extracted_text = str(text)
        
        # Display text and append to list
        # st.write(extracted_text)
        extracted_texts.append(extracted_text)
    
    return extracted_texts

def main():
    # App configuration
    st.set_page_config(page_title=APP_TITLE, layout=APP_LAYOUT)
    st.title(APP_TITLE)
    st.sidebar.header("Upload Financial Document")

    # Initialize components
    doc_processor = DocumentProcessor(UNSTRUCTURED_API_KEY, UNSTRUCTURED_API_URL)
    financial_analyzer = FinancialAnalyzer()
    llm_handler = LLMHandler()
    data_aggregator = DataAggregator()

    # File upload
    uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file:
        # Save and process file
        with open("temp_uploaded.pdf", "wb") as f:
            f.write(uploaded_file.read())
        
        st.sidebar.success("File uploaded successfully!")
        st.info("Extracting data from the document...")

        # Process document
        tables, texts = doc_processor.process_pdf("temp_uploaded.pdf")
        
        # Display and process data
        table_dataframes = display_tables(tables, doc_processor, financial_analyzer)
        extracted_texts = display_texts(texts)
        # xtracted_texts = texts

        # Chat interface
        st.header("Ask Questions")
        user_question = st.text_input("Ask a question about the document:")
        extracted_texts = [text.text if hasattr(text, 'text') else str(text) for text in texts]

        
        # if user_question and (table_dataframes or extracted_texts):
            
        #     context = data_aggregator.aggregate_context(
        #         table_dataframes, 
        #         extracted_texts
        #     )
        #     response = llm_handler.get_response(context, user_question)
        #     st.write("Response:", response)
        if user_question and (table_dataframes or extracted_texts):
            # Aggregate context (tables and extracted text)
          context = data_aggregator.aggregate_context(table_dataframes, extracted_texts)
    
          # Generate AI response
          response = llm_handler.get_response(context, user_question)
    
           # Display only the AI-generated response
          st.write("Response:", response)


if __name__ == "__main__":
    main()