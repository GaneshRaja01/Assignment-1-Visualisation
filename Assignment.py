# -*- coding: utf-8 -*-
# Student ID: 22024637
# Name: Ganesh Kumar Rajendran



import pandas as pd
import matplotlib.pyplot as plt

def barplot (dataframe, title, xlabel = None, ylabel = None):
    """ Function to create a barplot. Arguments:
        A dataframe with the needed coloumns
        title contains the title of the plot
        xlabel contains the name of x axis
        ylabel conntains the name of y axis
    """
    df_belgium_poland = dataframe[['Belgium', 'Poland']]
    #plotting line graph
    plt.figure()
    df_belgium_poland.plot.bar()
    plt.title(title)
    
    # labelling
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    plt.legend(loc='upper left', prop={'size': 8})
    # save as png
    plt.savefig("barplot.png")
    plt.show()
    return

def lineplot(dataframe, title, xlabel = None, ylabel = None):
    """ Function to create a lineplot. Arguments:
        A dataframe with the needed coloumns
        title contains the title of the plot
        xlabel contains the name of x axis
        ylabel conntains the name of y axis
    """
    
    # these line converts the type of index column to str
    dataframe.index = dataframe.index.astype("str")
    
    #plotting line graph
    plt.figure()
    dataframe.plot.line()
    plt.title(title)
    
    # labelling
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    plt.legend(loc='lower left', prop={'size': 8})
    # save as png
    plt.savefig("linplot.png")
    plt.show()
    return

def pieplot(dataframe, title, year, xlabel = None, ylabel = None):
    """ Function to create a pieplot. Arguments:
        A dataframe with the needed coloumns
        title contains the title of the plot
    """
  
    df_eu_energy_consumption_1990 = dataframe.loc[year]
    print(df_eu_energy_consumption_1990)
    
    #plotting line graph
    plt.figure()
    df_eu_energy_consumption_1990.plot.pie()
    plt.title(title)
    
    # labelling
    plt.ylabel(ylabel)
    
    # save as png
    plt.savefig(f'{title}.png')
    plt.show()
    return

#Reading GDP per capita table dataset and set index column
dataframe = pd.read_csv("GDP_per_capita_table.csv", index_col=0)
barplot(dataframe, 'GDP bar graph', 'year', 'Countries' )
    

dataframe = pd.read_csv("GDP_per_capita_table.csv", index_col=0)
lineplot(dataframe, 'GDP per capita', 'year', 'Gross Domestic Product' )

df_eu_energy_consumption = pd.read_csv('Final energy consumption by product type.csv', index_col=0)
pieplot(df_eu_energy_consumption, 'Energy consumption in 1990', 1990)
pieplot(df_eu_energy_consumption, 'Energy consumption in 2019', 2019)


