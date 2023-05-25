import csv
def read_from_csv():
    with open('database.csv', newline='') as database3:
        csv_reader = csv.reader(database3)
        csv_reader.__next__()
        csv_reader.__next__()
        csv_reader.__next__()
        print(csv_reader.line_num)
        print('hello')
read_from_csv()