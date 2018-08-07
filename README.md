# Triodos Manager CSV converter
This simple Python script converts transactions in a format provided by the `Triodos Bank` to a format usable by `Manager.io`.
My company uses Triodos banking and the free [Manager.io](https://www.manager.io) desktop client for bookkeeping.
Using this converter I am able to download transaction records in csv and import them in `Manager.io`.

# Usage

1. Download the `csv` from the online banking Triodos.
2. Run `python convert-csv.py <triodos.csv>`.
3. Import the csv file into `Manager.io`.

# Example
python convert-csv.py example_data/example-triodos.csv
