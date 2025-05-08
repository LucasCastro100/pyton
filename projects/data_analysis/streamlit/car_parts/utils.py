import os
import pandas as pd

def get_table(table_name):
    data = pd.read_csv(f"files/{table_name}.csv")
    return data