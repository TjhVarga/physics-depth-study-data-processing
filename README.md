# Crumple Zone Analysis

This project analyzes crumple zone data obtained from different collision runs. It performs data filtering, sorting, trendline fitting, and impulse calculation for each collision event. It also generates plots of the data and trendlines.
## Prerequisites

To run this project, you need to have Python (version 3.6 or higher) installed on your computer. If you don't have Python installed, you can download it from the official website: https://www.python.org/downloads/

If you use MacOS, please install xcode command line tools by running this command first. This will take 1.2 GB of disk space.

```shell
xcode-select --install
```

## Getting Started

1. Clone this repository to your local machine. Click on the green "Code" button on the repository page and select "Download ZIP". Extract the contents of the ZIP file to a folder on your computer.
2. Open a web browser and go to the Python website: https://www.python.org/downloads/
3. Download and install Python by clicking on the appropriate installer for your operating system. Follow the installation instructions provided.
4. Once Python is installed, open the folder where you extracted the repository files.
5. Look for the file named "Crumple Zone Data.csv" and rename it to "Crumple_Zone_Data.csv" (without spaces). Move the renamed file to the same folder as the repository files.
6. Install the required dependencies by entering the following command in terminal, then pressing enter:
```shell
pip install pandas matplotlib numpy scipy
```
If you have both Python 2 and Python 3 installed, you may need to use `pip3` instead of `pip`.
7. In terminal, type in "cd " (without quotes) and drag the folder containing the code files into the terminal window. Press enter.
8. In your file explorer, drag the SparkVue CSV file into the folder containing the code files. Rename the file to "Crumple Zone Data.csv".
9. Back in terminal, type in the following command and press enter:
```shell
make all
```
10. After a few seconds, the program will finish running. You should see a new folder named "output_plots" and "output_data" containing the generated plots and CSV files.

## Additional Notes
- The code assumes that the CSV file has columns named "Time (s)" and "Force (N)" (this is standard with SparkVue). If your data has different column names, make sure to update the column names in the code accordingly.
- The code assumes that the CSV file contains data for different collision runs. If you have a different data structure or naming convention, you may need to modify the code to adapt to your specific requirements.
- If you encounter any issues or have any questions, please feel free to open an issue in the GitHub repository, or ask me in person.

## Authors
Written by ChatGPT, Curated and modified by me.
Feel free to modify this to your hearts desire.