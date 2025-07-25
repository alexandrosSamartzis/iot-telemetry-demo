import pandas as pd
import os

# test the file path of the data file, the data qualification and completion of the data
def test_csv_load():
    file_path = "./data/smart_manufacturing_data.csv"
    assert os.path.exists(file_path), "CSV file missing!"
    df = pd.read_csv(file_path)
    assert not df.empty, "Dataframe is empty"
    assert "temperature" in df.columns, "Missing expected column"

# simple check test of logic in the code
def test_sample_logic():
    assert 1 + 1 == 2
    
