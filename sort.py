import pandas as pd
import numpy as np
import os
import re

CSV_FILTERED = "Crumple Zone Data Filtered.csv"
df = pd.read_csv("Crumple Zone Data Filtered.csv")

# Extract the headers from the CSV file into a list
def extract_run_names(file_path):
    df = pd.read_csv(file_path)
    headers = df.columns.tolist()
    pattern = r'Force \(N\) (\w+\s?\d*)'
    run_names = []
    for header in headers:
        match = re.search(pattern, header)
        if match:
            run_names.append(match.group(1))
    return run_names

# Define list
runs=extract_run_names(CSV_FILTERED)
offset = {}  # Dictionary to store the offset for each run
output_folder = "output_data"
os.makedirs(output_folder, exist_ok=True)  # Create the output folder if it doesn't exist
CUTOFF_THRESHOLD = 0.2  # Specify the cutoff threshold

adjusted_data = df.copy()  # Create a copy of the original data

for run in runs:
    # Filter the data for the current run
    run_data = adjusted_data[adjusted_data.columns[adjusted_data.columns.str.contains(run)]]
    
    # Find the index where the force exceeds 0.07 N
    collision_start_index = np.argmax(run_data[f"Force (N) {run}"] > CUTOFF_THRESHOLD)
    
    # Get the time value at the collision start index
    collision_start_time = run_data.iloc[collision_start_index][f"Time (s) {run}"]
    
    # Calculate the offset for the current run
    offset[run] = collision_start_time
    
    # Adjust the time values by subtracting the offset
    run_data[f"Time (s) {run}"] -= collision_start_time
    
    # Update the adjusted DataFrame with the adjusted time values
    adjusted_data.update(run_data)

# Print the adjusted DataFrame
print(adjusted_data)

# Save the adjusted DataFrame to a CSV file
adjusted_data.to_csv(os.path.join(output_folder, "Crumple Zone Data Adjusted.csv"), index=False)

# Split runs into separate CSV files, remove unwanted rows, and save the data
for run in runs:
    # Filter the adjusted DataFrame for the current run
    run_data = adjusted_data[adjusted_data.columns[adjusted_data.columns.str.contains(run)]]
    
    # Specify the output file path for the current run
    output_file = os.path.join(output_folder, f"{run}_data.csv")
    
    # Save the run data to a separate CSV file
    run_data.to_csv(output_file, index=False)
    
    # Load the saved file as a DataFrame
    run_df = pd.read_csv(output_file)
    
    # Remove rows with time values less than -0.01 seconds
    run_df = run_df[run_df[f"Time (s) {run}"] >= -0.01]
    
    # Save the modified DataFrame back to the file, overwriting the previous contents
    run_df.to_csv(output_file, index=False)
    
    # Print a message to indicate that the data was saved
    print(f"Saved data for {run} to {output_file}")
