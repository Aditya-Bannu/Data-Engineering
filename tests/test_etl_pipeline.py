import pytest
import pandas as pd

# Example function to test (later import from etl_pipeline.py)
def transform_weather_data(data):
    df = pd.DataFrame(data)
    df["temp_celsius"] = (df["temp_fahrenheit"] - 32) * 5.0/9.0
    return df

def test_transform_weather_data():
    data = [{"city": "Delhi", "temp_fahrenheit": 98.6}]
    df = transform_weather_data(data)
    assert "temp_celsius" in df.columns
    assert round(df["temp_celsius"].iloc[0], 1) == 37.0
