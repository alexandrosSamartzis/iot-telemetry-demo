import pandas as pd
import os

def test_csv_load():
    file_path = "../../data/smart_manufacturing_data.csv"
    assert os.path.exists(file_path), "CSV file missing!"
    df = pd.read_csv(file_path)
    assert not df.empty, "Dataframe is empty"
    assert "temperature" in df.columns, "Missing expected column"

def test_sample_logic():
    assert 1 + 1 == 2