''' starlight13 '''
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit (using all data from 1880 to 2013)
    slope_all, intercept_all, r_value_all, p_value_all, std_err_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create x values from 1880 to 2050 for the first line
    x_all = range(1880, 2051)
    y_all = [slope_all * x + intercept_all for x in x_all]
    plt.plot(x_all, y_all, 'r-')

    # Create second line of best fit (using data from 2000 onwards)
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    
    # Create x values from 2000 to 2050 for the second line
    x_2000 = range(2000, 2051)
    y_2000 = [slope_2000 * x + intercept_2000 for x in x_2000]
    plt.plot(x_2000, y_2000, 'g-')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
