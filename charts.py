import matplotlib.pyplot as plt

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal') 
  plt.show() 

if __name__ == '__main__': 
  labels = ()
  values = []

  generate_pie_chart(labels, values)