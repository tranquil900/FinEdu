"""
Handles data aggregation from different sources
"""

import pandas as pd
from typing import List, Optional

class DataAggregator:
    @staticmethod
    def aggregate_context(
        table_dataframes: List[pd.DataFrame], 
        extracted_texts: List[str]
    ) -> str:
        """
        Aggregate data from tables and texts into a single context string
        
        Args:
            table_dataframes: List of pandas DataFrames containing table data
            extracted_texts: List of extracted text strings
            
        Returns:
            str: Combined context string
        """
        context = ""
        
        # Add table data
        if table_dataframes:
           for df in table_dataframes:
              context += df.to_string() + "\n\n"
    
    # Add extracted texts, ensuring they are strings
        if extracted_texts:
            context += "\n".join(str(text) for text in extracted_texts)
    
        return context.strip()