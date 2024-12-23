import pandas as pd

class FinancialAnalyzer:
    @staticmethod
    def calculate_basic_metrics(df):
        if 'Revenue' in df.columns and 'Expenses' in df.columns:
            df['Net Profit'] = df['Revenue'] - df['Expenses']
            return df[['Revenue', 'Expenses', 'Net Profit']]
        return None

    @staticmethod
    def calculate_financial_ratios(df):
        metrics = {}
        
        if 'Total Assets' in df.columns and 'Total Liabilities' in df.columns:
            df['Debt-to-Equity Ratio'] = df['Total Liabilities'] / df['Total Assets']
            metrics['debt_equity'] = df[['Total Assets', 'Total Liabilities', 'Debt-to-Equity Ratio']]

        if 'Year' in df.columns and 'Revenue' in df.columns:
            df['Revenue Growth (%)'] = df['Revenue'].pct_change() * 100
            metrics['revenue_growth'] = df[['Year', 'Revenue', 'Revenue Growth (%)']]

        return metrics