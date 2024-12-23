"""
Application configuration
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration variables
UNSTRUCTURED_API_KEY = os.getenv("UNSTRUCTURED_API_KEY")
UNSTRUCTURED_API_URL = os.getenv("UNSTRUCTURED_API_URL")

# Hugging Face settings
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
HF_MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.2"

# App settings
APP_TITLE = "Financial Document Analyzer"
APP_LAYOUT = "wide"