import duckdb
import pandas as pd
from constants import QUERY_PATH_BASED_ON_CATEGORY

class QueryHandler:
    def __init__(self, query_category:str):
        self.query_category = query_category

        if self.query_category in QUERY_PATH_BASED_ON_CATEGORY.keys():
            self.query_text = self.select_query()

            if isinstance(self.query_text, str):
                self.df_result = self.execute_query_and_return_dataframe()
        else:
            self.df_result = None


    def select_query(self) -> str:
        # Reading the file from the local SQL Query
        with open(QUERY_PATH_BASED_ON_CATEGORY[self.query_category]) as file:
            return file.read()

    def execute_query_and_show(self) -> None:
        duckdb.sql(self.query_text).show()
    
    def execute_query_and_return_dataframe(self) -> pd.DataFrame:
        return duckdb.sql(self.query_text).df()