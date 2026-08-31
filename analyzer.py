import pandas as pd

# A simple script to load a dataset, clean missing values, and show basic stats
def analyze_data(file_path):
    df = pd.read_csv(file_path)
    print("--- Dataset Info ---")
    print(df.info())
    print("\n--- Summary Statistics ---")
    print(df.describe())

# You can run this with any sample CSV file
# analyze_data('your_data.csv')
