import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('C:/Users/mario/Downloads/ROMERO/Projects/Movies/data.csv')

  labels, values = utils.get_keys_values(data)
  charts.generate_pie_chart(labels, values)

if __name__ == '__main__':
  run()