# rank,name,year,rating,genre,certificate,run_time,tagline,budget,box_office,casts,directors,writers
import csv

def read_csv(path):
    with open(path, encoding="utf8") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            dict_1 = {key: value for key, value in iterable}
            data.append(dict_1)
        return data
    
if __name__ == "__main__":
    data = read_csv('C:/Users/mario/Downloads/ROMERO/Projects/Movies/data.csv')
    print(data[1])


