import pandas as pd
import numpy as np

class CreateCSV:
    @classmethod
    def time_csv_creator(cls, data, algorithms_names):
        print("in create scv")
        df = pd.DataFrame(data)
        df.to_csv(f'time_csvs\\{algorithms_names}.csv', index=False)