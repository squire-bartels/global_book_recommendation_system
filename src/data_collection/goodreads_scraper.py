import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file with the specified encoding and separator
file_path = 'raw/book1-100k.csv'  # Replace with your actual file path
books_df = pd.read_csv(file_path, sep=";", on_bad_lines='skip', encoding='Latin-1')

# Display the first few rows and columns
print(books_df.head())
print(books_df.columns)



