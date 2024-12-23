"""
LLM configuration and settings
"""
from dataclasses import dataclass

@dataclass
class LLMConfig:
    temperature: float = 0.1
    max_length: int = 1000
    top_p: float = 0.95
    repetition_penalty: float = 1.1