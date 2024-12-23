from unstructured.partition.pdf import partition_pdf
from unstructured_client import UnstructuredClient
import pandas as pd

class DocumentProcessor:
    def __init__(self, api_key, api_url):
        self.client = UnstructuredClient(
            api_key_auth=api_key,
            server_url=api_url
        )

    def process_pdf(self, filename):
        elements = partition_pdf(filename=filename)
        tables = [el for el in elements if el.category == "Table"]
        texts = [el for el in elements if el.category != "Table"]
        return tables, texts

    @staticmethod
    def parse_table(table):
        try:
            return pd.read_html(table.metadata.text_as_html)[0]
        except ValueError:
            return None