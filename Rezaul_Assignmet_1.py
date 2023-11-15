"""
Created on Tue Nov 14 02:18:26 2023

@author: Md Rezaul Karim
Student ID: 22094702
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# read the txt data and clean it up
data = pd.read_csv(
    "UK.txt",
    encoding="utf-8",
    delim_whitespace=True,
    header=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
)
# save the data as csv
data.to_csv(
    "UK.csv",
    index=False,
    header=[
        "year",
        "jan",
        "feb",
        "mar",
        "apr",
        "may",
        "jun",
        "jul",
        "aug",
        "sep",
        "oct",
        "nov",
        "dec",
        "win",
        "spr",
        "sum",
        "aut",
        "ann",
    ],
)

# read the csv data
df = pd.read_csv("UK.csv")
df2 = pd.read_csv('US_Crime_Rates.csv')


def line_plot(df2):
    """Create a line plot of US Crime Rates (1850-2023)
    Args:
        df2 (pandas dataframe): data
    """
    # Extracting data from below crime types
    crime_types = ['Murder','Property', 'Forcible_Rape','Robbery', 'Larceny_Theft','Vehicle_Theft']
   
    # Creating line chart and label to show legend
    plt.plot(df2.Year, df2[crime_types], label=crime_types)
  
    #Add title and label to chart
    plt.xlabel('Year')
    plt.ylabel('Number of people in Million')
    plt.title('US Crime Report')
    plt.legend()
    
    # Dispaly the chart
    plt.show()


def scatter_plot(df):
    """Create a scatter plot of January vs. February Precipitation in the UK (1850-2023).
    It shows a positive correlation between the two variables.
    Args:
        df (pandas dataframe): data
    """
    # Extracting data for January and February
    january_precipitation = df["jan"]
    february_precipitation = df["feb"]

    # Creating a scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(january_precipitation, february_precipitation, c="blue", alpha=0.7)
    
    #Add title and label to chart
    plt.title("Scatter Plot: January vs. February Precipitation (1850-2023)")
    plt.xlabel("January Precipitation (mm)")
    plt.ylabel("February Precipitation (mm)")
    
    #grid in graph for better readability and reference
    plt.grid(True)
    
    # Dispaly the chart
    plt.show()


def bar_chart(df):
    """Create a bar chart of Seasonal Average Precipitation in the UK (1850-2023)
    Args:
        df (pandas dataframe): data
    """
    # Extractiing Precititation data from DataFrame
    seasonal_data = df[["win", "spr", "sum", "aut"]]
    
    # Create Bar chart to visualize 
    plt.figure(figsize=(12, 6))
    seasonal_data.mean().plot(kind="bar", color=["blue", "green", "orange", "red"])
    
    # Add title and label to chart
    plt.title("Seasonal Average Precipitation in the UK (1850-2023)")
    plt.xlabel("Season")
    plt.ylabel("Average Precipitation (mm)")
    
    # Rotating X-axis label for batter readability
    plt.xticks(rotation=0)
    
    # Dispaly the chart
    plt.show()

#below call 3 types of plot to show
line_plot(df2)
scatter_plot(df)
bar_chart(df)

