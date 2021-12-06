# Import internal library
import codecademylib3
# 1 
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
#Loading csv files into pandas dataframe
Golden_Ticket_Award_Winners_Wood = pd.read_csv("Golden_Ticket_Award_Winners_Wood.csv")
Golden_Ticket_Award_Winners_Steel = pd.read_csv("Golden_Ticket_Award_Winners_Steel.csv")
#Inspect Datafrmes
print(Golden_Ticket_Award_Winners_Wood.head())
print(Golden_Ticket_Award_Winners_Steel.head())

# 2
# Create a function to plot rankings over time for 1 roller coaster
def create_plot(roller_name, park_name, df):
  plot_data = df[["Year of Rank", "Rank"]][(df.Name == roller_name) & (df.Park == park_name)]
  plot_data = plot_data.sort_values(by = "Year of Rank")
  plt.plot(plot_data["Year of Rank"], plot_data["Rank"])
  plt.title("Ranking of " + str(roller_name) + " at " + str(park_name) + " over time")
  plt.xlabel("Years")
  plt.ylabel("Rank")
  ax = plt.subplot()
  ax.invert_yaxis()
  plt.show()

# 3
# Create a plot of El Toro ranking over time
create_plot("El Toro", "Six Flags Great Adventure", Golden_Ticket_Award_Winners_Wood)
plt.clf()
# Create a plot of El Toro and Boulder dash hurricanes
def create_plot2(roller_name1, roller_name2, park_name1, park_name2, df):
  plot_data1 = df[["Year of Rank", "Rank"]][(df.Name == roller_name1) & (df.Park == park_name1)]
  plot_data1 = plot_data1.sort_values(by = "Year of Rank")
  plot_data2 = df[["Year of Rank", "Rank"]][(df.Name == roller_name2) & (df.Park == park_name2)]
  plot_data2 = plot_data2.sort_values(by = "Year of Rank")
  plt.plot(plot_data1["Year of Rank"], plot_data1["Rank"], color = "red", label = roller_name1)
  plt.plot(plot_data2["Year of Rank"], plot_data2["Rank"], color = "green", label = roller_name2)
  plt.title("Ranking of " + str(roller_name1) + " and " + str(roller_name2) + " over time")
  plt.xlabel("Years")
  plt.ylabel("Rank")
  plt.show()
#Testing the function
create_plot2("El Toro", "Boulder Dash", "Six Flags Great Adventure", "Lake Compounce", Golden_Ticket_Award_Winners_Wood)
plt.clf()
# 4
# Create a function to plot top n rankings of roller coasters over time
def create_plot3(n, df):
  plot_data3 = df[["Name", "Year of Rank", "Rank"]][df.Rank <= n]
  for i in plot_data3.Name.unique():
    plot_data4 = plot_data3[["Year of Rank", "Rank"]][df.Name == i]
    plot_data4 = plot_data4.sort_values(by = "Year of Rank")
    plt.plot(plot_data4["Year of Rank"], plot_data4["Rank"])
  plt.title("Rankings of top " + str(n) + " roller coasters over time")
  plt.xlabel("Year")
  plt.ylabel("Rank")
  plt.legend(plot_data3.Name.unique())
  plt.show()

# Create a plot of top n rankings over time
create_plot3(5, Golden_Ticket_Award_Winners_Wood)
# 5
# load roller coaster data into a pandas dataframe
roller_coasters = pd.read_csv("roller_coasters.csv")
#Inspecting the dataframe
print(roller_coasters.head())

# 6
# Create a function to plot histogram of numerical column values
plt.clf()
def create_plot4(df, column_name):
  df = df.dropna()
  plt.hist(df[column_name])
  plt.title("Frequency of " + column_name + " of different roller coasters")
  plt.xlabel(column_name)
  plt.ylabel("Frequency")
  plt.show()
# Create histogram of roller coaster speed
create_plot4(roller_coasters, "speed")
# Create histogram of roller coaster length
plt.clf()
create_plot4(roller_coasters, "length")
# Create histogram of roller coaster number of inversions
plt.clf()
create_plot4(roller_coasters, "num_inversions")
#Height
#plt.clf()
#create_plot4(roller_coasters, "height")
#Taking outliers from the heights data in a new function to plot height since there are a lot of outliers making the data skewed
# Create a function to plot histogram of height values
def create_plot5(df, column_name):
  df = df.dropna()
  heights = df[df[column_name] <= 140]
  plt.hist(heights[column_name])
  plt.title("Frequency of " + column_name + " of different roller coasters")
  plt.xlabel(column_name)
  plt.ylabel("Frequency")
  plt.show()
# Create a histogram of roller coaster height
plt.clf()
create_plot5(roller_coasters, "height")
# 7
# Create a function to plot inversions by coaster at park
plt.clf()
#print(roller_coasters.num_inversions.unique())
def create_plot6(df, park_name):
  df = df[df.park == park_name]
  coaster_names = df['name']
  number_inversions = df['num_inversions']
  plt.bar(range(len(coaster_names)), number_inversions)
  plt.title("Number of Inversions of roller coasters at " + park_name)
  plt.xlabel("Roller Coasters")
  plt.ylabel("Number of Inversions")
  ax = plt.subplot()
  ax.set_xticks(range(len(coaster_names)))
  ax.set_xticklabels(coaster_names, rotation = 30)
  plt.show()
# Create barplot of inversions by roller coasters
create_plot6(roller_coasters, "Parc Asterix")
# 8
# Create a function to plot a pie chart of status.operating
plt.clf()
def create_plot7(df):
  status_operating = df[df.status == "status.operating"]
  status_closed = df[df.status == "status.closed.definitely"]
  status_counts = [len(status_operating), len(status_closed)]
  plt.pie(status_counts, labels = ["Operating", "Closed"], autopct = "%0.1f%%")
  plt.title("Status of roller coasters")
  plt.axis("equal")
  plt.show()
# Create pie chart of roller coasters
create_plot7(roller_coasters)
# 9
# Create a function to plot scatter of any two columns
plt.clf()
def create_plot8(df, column_name1, column_name2):
  plt.scatter(df[column_name1], df[column_name2])
  plt.title("Graph of " + column_name2 + " vs " + column_name1)
  plt.xlabel(column_name1)
  plt.ylabel(column_name2)
  plt.show()
# Create a function to plot scatter of speed vs height
create_plot8(roller_coasters, "height", "speed")
# Create a scatter plot of roller coaster height by speed
plt.clf()
create_plot8(roller_coasters, "speed", "height")
#Creating a plot to find out which seating type is most popular
plt.clf()
roller_seat_count = roller_coasters.groupby("seating_type").name.count().reset_index()
seats = pd.Series.tolist(roller_seat_count.seating_type)
roller_seat_count = roller_seat_count.name.astype("int")
print(roller_seat_count)
import numpy as np
seat_count = pd.Series.tolist(roller_seat_count)
print(seats)
print(seat_count)
plt.bar(range(len(seat_count)), seat_count)
ax = plt.subplot()
ax.set_xticks(range(len(seat_count)))
ax.set_xticklabels(seats, rotation = 40)
plt.title("Seating Types of Roller Coasters")
plt.xlabel("Seat Types")
plt.ylabel("Number")
plt.show()