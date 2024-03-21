import csv
with open("week23.csv", "w") as f:
    pen= csv.writer(f)
    header = ["Name", "CellPhone", "City"]
    pen.writerow(header)
    entry1= (["serge,777 777 777","Dallas"])
    pen.writerow(entry1)
f.close
