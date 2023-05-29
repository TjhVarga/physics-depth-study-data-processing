import pandas as pd

# Read the CSV file into a pandas DataFrame.
df = pd.read_csv('Crumple Zone Data.csv')

# Filter out columns that don't contain the word "time" or "force" and do not contain the phrase "Date and Time".
df = df.loc[:, df.columns.str.contains('Time|Force') & ~df.columns.str.contains('Date and Time')]

# Print the DataFrame.
print(df)

# Save the DataFrame to a CSV file.
df.to_csv('Crumple Zone Data Filtered.csv', index=False)