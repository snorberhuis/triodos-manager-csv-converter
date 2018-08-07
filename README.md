# Bank Transaction Converter for Manager
This simple Python script converts transactions in a format provided by the `Triodos Bank` to a format usable by `Manager.io`.
My company uses Triodos banking and the free [Manager.io](https://www.manager.io) desktop client for bookkeeping.
Using this converter I am able to download transaction records in csv and import them in `Manager.io`.

# Usage

1. Download the `csv` from the online banking Triodos into the `in` folder.
2. Run `python convert-csv.sh.py`.
3. Import the highest numbered csv file in `out`.