import csv
from datetime import datetime
import re

month_dict = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

with open('dataset\\fsas\\fsas_full_utf8.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = [row for row in reader]

for row in rows:
    text = row[4]
    print(text)
    date_string = ""
    try:
        pattern = r"(\d{1,2})\s([a-zA-Z]+)\s(\d{4})"
        match = re.search(pattern, text)
        date_string = f"{match.group(3)}/{match.group(2)}"
        pattern_ = r"([a-zA-Z]+)"
        match_ = re.search(pattern_, date_string)
        month_name_ = match_.group(1)
        date_string = date_string.replace(month_name_, month_dict[month_name_])
    except:
        try:
            pattern = r"([a-zA-Z]+)\s(\d{4})"
            match = re.search(pattern, text)
            date_string = f"{match.group(2)}/{match.group(1)}"
            pattern_ = r"([a-zA-Z]+)"
            match_ = re.search(pattern_, date_string)
            month_name_ = match_.group(1)
            date_string = date_string.replace(month_name_, month_dict[month_name_])
        except:
            date_string = "None"

    print(date_string)
    row.append(date_string)

with open('output.csv', 'w', encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header + ['7列目'])
    writer.writerows(rows)
