import csv

def add_raw_csv(data):
    filepath = "./data.csv"
    with open(filepath, 'a',newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

if __name__ == '__main__':
    data = [["Title","URL","Abstract"]]
    add_raw_csv(data)
