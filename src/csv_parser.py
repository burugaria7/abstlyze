import csv
from csv import reader

def add_raw_csv(data):
    filepath = "../data.csv"
    with open(filepath, 'a',newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

def csv_to_text():
    filepath = "../data.csv"
    textpath = "./data.txt"
    with open(filepath, "r") as my_file:
        # pass the file object to reader()
        file_reader = reader(my_file)
        # do this for all the rows
        for i in file_reader:
            # print the rows
            print(i[2])
            with open(textpath, 'a') as ff:
                print(i[2], file=ff)

if __name__ == '__main__':
    # data = [["Title","URL","Abstract"]]
    # add_raw_csv(data)
    csv_to_text()
