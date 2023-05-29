import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.integrate import trapz

# Specify plot size
HEIGHT = 6
WIDTH = 24

# Specify the Peak Height Threshold
PEAK_HEIGHT_THRESHOLD = 0.07 # Default: 0.07

# Specify the polynomial degree
DEGREE = 3

# Specify the enlarged plot sample size
TIME_RANGE = 0.03 # Default: 0.1

# # Enable LaTeX rendering in matplotlib
# plt.rcParams['text.usetex'] = True

# Assuming you have the CSV files for each run

runs = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'Control 1', 'Control 2', 'Control 3']
plots = []

output_folder = "output_plots"
os.makedirs(output_folder, exist_ok=True)  # Create the output folder if it doesn't exist

for run in runs:
    # print('plots: ', plots)

    # Specify the input file path for the current run
    input_file = os.path.join("output_data", f"{run}_data.csv")
    
    # Read the data from the CSV file
    run_data = pd.read_csv(input_file)

    # Set the figure size
    plt.figure(figsize=(WIDTH, HEIGHT))
    
    # Create a scatter plot with connecting lines
    plt.plot(run_data[f"Time (s) {run}"], run_data[f"Force (N) {run}"], marker='o', markersize=2, linestyle='-')
    
    # Set the plot title and labels
    plt.title(f"Force vs. Time - {run}")
    plt.xlabel("Time (s)")
    plt.ylabel("Force (N)")
    
    # Find peaks in the force data
    peaks, _ = find_peaks(run_data[f"Force (N) {run}"], height=PEAK_HEIGHT_THRESHOLD)

    # Get the time and force values at the peaks
    peak_times = run_data[f"Time (s) {run}"][peaks]
    peak_forces = run_data[f"Force (N) {run}"][peaks]

    # Create a polynomial trendline using numpy.polyfit()
    last_peak_index = peaks[-1]
    coefficients = np.polyfit(peak_times[:last_peak_index+1], peak_forces[:last_peak_index+1], DEGREE)
    trendline = np.polyval(coefficients, run_data[f"Time (s) {run}"].values)
    
    # Get the equation of the polynomial
    equation = np.poly1d(coefficients)

    # Plot the trendline
    plt.plot(run_data[f"Time (s) {run}"], trendline, color='red')

    # Set the x-axis tick locations and labels
    # x_ticks = np.arange(run_data[f"Time (s) {run}"].min(), run_data[f"Time (s) {run}"].max() + 1.008, 1.008)  # Adjust the interval as needed
    # plt.xticks(x_ticks)

    # Calculate total impulse for each bump
    total_impulse = 0.0
    for i in range(len(peaks)-1):
        start_index = peaks[i]
        end_index = peaks[i+1]
        force_values = run_data[f"Force (N) {run}"][start_index:end_index+1].values
        time_values = run_data[f"Time (s) {run}"][start_index:end_index+1].values
        impulse = trapz(force_values, time_values)
        total_impulse += impulse

    # Round the impulse to 4 significant figures
    rounded_impulse = round(total_impulse, 4)

    # Create the equation string with LaTeX formatting for superscripts
    equation_parts = [f"{round(coefficients[i], 2)}t^{{{DEGREE-i}}}" for i in range(DEGREE+1)]
    equation = r"Trendline Equation: $y = " + "+".join(equation_parts) + r"$"
    impulse_text = f"Total Impulse: {rounded_impulse} Ns"

    # Add the equation and the total impulse to the graph
    plt.text(0.95, 0.95, equation, color='red', transform=plt.gca().transAxes, fontsize=10, ha='right', va='top')
    plt.text(0.95, 0.85, impulse_text, color='black', transform=plt.gca().transAxes, fontsize=10, ha='right', va='top')
    
    # Add plot to list of plots
    plots.append(plt)

     # Create an enlarged plot of the first collision
    if len(peaks) > 0:
        first_collision_index = peaks[0]
        time_range = TIME_RANGE  # Adjust the time range here (in seconds)
        delta_time = time_range / 2.0
        start_index = max(0, first_collision_index - int(delta_time * run_data[f"Time (s) {run}"].count()))
        end_index = min(first_collision_index + int(delta_time * run_data[f"Time (s) {run}"].count()), len(run_data))

        # Create a new figure and axis for the enlarged plot
        fig, ax = plt.subplots(figsize=(WIDTH, HEIGHT))

        # Plot the enlarged first collision
        ax.plot(run_data[f"Time (s) {run}"][start_index:end_index], run_data[f"Force (N) {run}"][start_index:end_index], marker='o', markersize=2, linestyle='-')

        # Set the plot title and labels for the enlarged plot
        ax.set_title(f"First Collision - {run}")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Force (N)")

        # Calculate the impulse for the first collision
        force_values = run_data[f"Force (N) {run}"][start_index:end_index].values
        time_values = run_data[f"Time (s) {run}"][start_index:end_index].values
        impulse = trapz(force_values, time_values)

        # Round the impulse to 4 significant figures
        rounded_impulse = round(impulse, 4)

        # Add the impulse information to the plot
        impulse_text = f"Impulse: {rounded_impulse} Ns"
        ax.text(0.95, 0.95, impulse_text, color='black', transform=ax.transAxes, fontsize=10, ha='right', va='top')

        # Save the enlarged plot as an image file
        output_file = os.path.join(output_folder, f"{run}_enlarged_plot.png")
        plt.savefig(output_file)

        print(f"Enlarged plot for {run} to {output_file}")

        # Close the figure to free up resources
        plt.close(fig)

    # Save the original plot as an image file
    output_file = os.path.join(output_folder, f"{run}_plot.png")
    plt.savefig(output_file)

    # Clear the current figure
    # plt.clf()  
    
    print(f"Saved plot for {run} to {output_file}")

# # Show all of the plots
# for plt in plots:
#     plt.show()
