import csv
import os
import sys


class TriodosBankRow:

    def __init__(self, date, account, amount, direction, payee, other_account, something, description):
        self.Date = date
        self.Account = account

        self.Amount = convert_amount(amount)

        self.Direction = direction
        if self.Direction == "Debet":
            self.Amount = -1 * self.Amount

        self.Payee = payee
        self.OtherAccount = other_account
        self.Something = something
        self.Description = description

    def string(self):
        return "Account: " + self.Account + "\n" + \
               "Amount: " + str(self.Amount) + "\n" + \
               "Direction: " + self.Direction + "\n" + \
               "Payee: " + self.Payee + "\n" + \
               "OtherAccount: " + self.OtherAccount + "\n" + \
               "Description: " + self.Description + "\n"

    def convert_to_manager_bank_row(self):
        return ManagerBankRow(
            self.Date,
            self.Payee,
            "",
            self.Description,
            self.Amount)


class ManagerBankRow:

    def __init__(self, date, payee, reference, description, amount):
        self.Date = date
        self.Payee = payee
        self.Reference = reference
        self.Description = description
        self.Amount = amount

    def export_to_csv(self):
        return [
            self.Date,
            self.Payee,
            self.Reference,
            self.Description,
            self.Amount,
        ]


def convert_amount(amount):
    amount = amount.replace('.', '')

    text = list(amount)
    text[-3] = '.'

    return float(''.join(text))


def import_from_csv(file_name):
    rows = []
    with open(file_name, 'rb') as csvFile:
        bank_rows = csv.reader(csvFile)
        for bank_row in bank_rows:
            rows.append(TriodosBankRow(*bank_row))
    return rows


def export_to_csv(file_name, rows):
    with open(file_name, 'wb') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', )
        csv_writer.writerow(["Date", "Payee", "Reference", "Description", "Amount"])
        for bank_row in rows:
            csv_writer.writerow(bank_row.export_to_csv())


def process_input_file(input, output):
    print "Processing file " + input + "..."
    print "Converting rows..."
    triodos_rows = import_from_csv(input)

    manager_rows = []
    for triodos_row in triodos_rows:
        manager_rows.append(triodos_row.convert_to_manager_bank_row())

    export_to_csv(output, manager_rows)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: python convert-csv.py <file-name>")
        exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[1]
    process_input_file(input_file, output_file)
