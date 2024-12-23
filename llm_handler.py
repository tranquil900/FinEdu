# """
# LLM handling using Hugging Face Inference API
# """

# from langchain_community.llms import HuggingFaceHub
# from .prompts import FINANCIAL_ASSISTANT_PROMPT
# from config import HUGGINGFACE_API_KEY, HF_MODEL_ID

# class LLMHandler:
#     def __init__(self):
#         self.llm = HuggingFaceHub(
#             repo_id=HF_MODEL_ID,
#             huggingfacehub_api_token=HUGGINGFACE_API_KEY,
#             model_kwargs={
#                 "temperature": 0.1,
#                 "max_length": 512,
#                 "top_p": 0.95
#             }
#         )
#         self.prompt_template = FINANCIAL_ASSISTANT_PROMPT

#     def get_response(self, context: str, question: str) -> str:
#         """
#         Get LLM response using Hugging Face Inference API
        
#         Args:
#             context (str): The context information
#             question (str): The user's question
            
#         Returns:
#             str: The LLM's response
#         """
#         query_prompt = self.prompt_template.format_prompt(
#             context=context, 
#             question=question
#         )
#         return self.llm.invoke(query_prompt.to_string())
"""
LLM handling using Hugging Face API
"""
from typing import Optional
from langchain_community.llms import HuggingFaceHub
from .llm_config import LLMConfig
from .prompts import FINANCIAL_ASSISTANT_PROMPT
from config import HUGGINGFACE_API_KEY, HF_MODEL_ID

class LLMHandler:
    def __init__(self):
        config = LLMConfig()
        self.llm = HuggingFaceHub(
            repo_id=HF_MODEL_ID,
            huggingfacehub_api_token=HUGGINGFACE_API_KEY,
            model_kwargs={
                "temperature": config.temperature,
                "max_length": config.max_length,
                "top_p": config.top_p,
                "repetition_penalty": config.repetition_penalty
            }
        )
        self.prompt_template = FINANCIAL_ASSISTANT_PROMPT

    def get_response(self, context: str, question: str) -> str:
        """
        Get LLM response using Hugging Face API
        
        Args:
            context (str): The context information
            question (str): The user's question
            
        Returns:
            str: The LLM's response
        """
        try:
            prompt = self.prompt_template.format(
                context=context,
                question=question
            )
            return self.llm.invoke(prompt)
        except Exception as e:
            return f"Error getting LLM response: {str(e)}"