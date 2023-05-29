filter:
	python3 filter.py

sort:
	python3 sort.py

graph:
	python3 graph.py

reset:
	rm -rf output_data
	rm -rf output_plots
	rm -f "Crumple Zone Data Adjusted.csv"
	rm -f "Crumple Zone Data Filtered.csv"

all: reset filter sort graph
