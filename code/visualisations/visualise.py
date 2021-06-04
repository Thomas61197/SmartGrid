import pandas as pd
import matplotlib.pyplot as plt

district_number = '1'
battery_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")
house_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")

d1_houses = pd.read_csv(house_file)
d1_houses.plot(kind='scatter', x='x', y='y')

d1_batteries =  pd.read_csv(battery_file)
d1_batteries[['x','y']] = d1_batteries.positie.str.split(",",expand=True)

print(d1_batteries['x'])
print(d1_houses['x'])
print('check')


# clear the figure
plt.clf()
#plt.scatter(house_file)
plt.title('SmartGrid')
plt.scatter(d1_batteries['x'], d1_batteries['y'])
plt.scatter(d1_houses['x'], d1_houses['y'])
#grid 
plt.minorticks_on()
plt.grid(which='minor', color='lightgrey')
plt.grid(which='major', color='grey')


# plot size
# px = 1/plt.rcParams['figure.dpi']
# plt.figsize=(800*px, 1200*px)

plt.show()
plt.savefig('result.png')