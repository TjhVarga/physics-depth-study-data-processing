# Crumple Zone Analysis

This project analyzes crumple zone data obtained from different collision runs. It performs data filtering, sorting, trendline fitting, and impulse calculation for each collision event. It also generates plots of the data and trendlines.

## Prerequisites

To run this project, you need to have the following installed:

- Python (version 3.6 or higher)
- pandas (Python library for data manipulation)
- matplotlib (Python library for data visualization)
- numpy (Python library for numerical operations)
- scipy (Python library for scientific computing)

You can install these dependencies by running the following command:

```shell
pip install pandas matplotlib numpy scipy
```

If you have both Python 2 and Python 3 installed, you may need to use `pip3` instead of `pip`.

If you use MacOS, please install xcode command line tools by running this command first. This will take 1.2 GB of disk space.

```shell
xcode-select --install
```

## Getting Started

1. Clone this repository to your local machine. Do this with `git clone` or by downloading the ZIP file.
2. Open a terminal window and navigate to the project directory.
3. Rename the csv file from sparkvue to `Crumple Zone Data.csv` and place it in the project directory.
4. Run the following command to start the program:

```shell
make all
```

## Additional Notes
- You can modify the degree of the polynomial trendline by updating the degree variable in the graph.py file.
- The code assumes that the CSV file has columns named "Time (s)" and "Force (N)" (this is standard with SparkVue). If your data has different column names, make sure to update the column names in the code accordingly.
- The code assumes that the CSV file contains data for different collision runs. If you have a different data structure or naming convention, you may need to modify the code to adapt to your specific requirements.
- If you encounter any issues or have any questions, please feel free to open an issue in the GitHub repository.

## Authors
Written by ChatGPT, Curated and modified by me.
Feel free to modify this to your hearts desire.