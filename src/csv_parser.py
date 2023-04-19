import csv
from csv import reader


def add_raw_csv(data):
    filepath = "../data.csv"
    with open(filepath, 'a', newline="", encoding='utf-16') as f:
        writer = csv.writer(f, dialect='excel', delimiter='\t', quoting=csv.QUOTE_ALL)
        writer.writerows(data)


def add_raw_csv_with_filepath(data, filepath):
    with open(filepath, 'a', newline="", encoding='utf-16') as f:
        writer = csv.writer(f, dialect='excel', delimiter='\t', quoting=csv.QUOTE_ALL)
        writer.writerow(data)


# CSVからテキストに変換するだけ
def csv_to_text():
    str = ""
    filepath = "../data_6k.csv"
    textpath = "../data_6k.txt"
    with open(filepath, "r") as my_file:
        # pass the file object to reader()
        file_reader = reader(my_file)
        # do this for all the rows

        # a = 0
        for i in file_reader:
            str += i[2]
            str += "\n"
        #     # print the rows
        #     print(str(a) + " " + i[2].strip('\n'))
        #     a += 1
        #     with open(textpath, 'a+') as ff:
        #         print(i[2].strip('\n'), file=ff)

    f = open(textpath, mode='w')
    f.write(str.rstrip('\r\n'))
    f.close()


if __name__ == '__main__':
    # data = [["Title","URL","Abstract"]]
    # add_raw_csv(data)
    csv_to_text()
