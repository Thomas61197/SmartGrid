# import pandas as pd
# import matplotlib.pyplot as plt

# d1_houses = pd.read_csv("district-1_houses.csv")
# d1_houses.plot(kind='scatter',x='x',y='y') # scatter plot
# # print(d1_houses)


# d1_batteries =  pd.read_csv('district-1_batteries.csv')
# d1_batteries[['x','y']] = d1_batteries.positie.str.split(",",expand=True)

# d1_batteries.plot(kind='scatter',x='x',y='y', color="orange")


# # plt.scatter(x='x', y='y', label='Generated samples')
# # plt.scatter(d1_batteries, label="Class #1 (Setosa)", color="red", alpha=.3) 

# print(d1_batteries)


# plt.title('SmartGrid')


# #grid 
# plt.minorticks_on()
# plt.grid(which='minor', color='lightgrey')
# plt.grid(which='major', color='grey')

# # plot size
# px = 1/plt.rcParams['figure.dpi']
# plt.figsize=(800*px, 1200*px)

# plt.show()