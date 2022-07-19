import csv

def add_raw_csv(data):
    filepath = "./data.csv"
    with open(filepath, 'a') as f:
        writer = csv.writer(f)
        writer.writerows(data)

if __name__ == '__main__':
    data = [["1","URL","Title","Abstract"]]
    add_raw_csv(data)
