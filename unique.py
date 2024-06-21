import pandas as pd
import matplotlib.pyplot as plt

weatherData = pd.read_csv('weatherData.csv')

def unique_locations():
    
    '''
    Converts the location column to lower case and prints the number of unique locations in the dataset.
    Prints the unique values of the location column.
    Prints the count of the lowest 5 locations.
    Calculates the percentage of the lowest 5 locations.
    Plots a pie chart of the lowest 5 locations with their percentages.
    '''

    weatherData['Location'] = weatherData['Location'].str.lower()
    number_of_unique = weatherData['Location'].nunique()

    print(f'There are {number_of_unique} unique locations in the dataset\n')
    name_of_unique = weatherData['Location'].unique()

    print('The name of each unique location converted to lower case for no repeat data:')
    for location in name_of_unique:
        print(location)

    location_counts = weatherData['Location'].value_counts()
    lowest_five_locations = location_counts.tail()
    print(f'The count of the lowest 5 locations are:\n{lowest_five_locations}')
    percentages = (lowest_five_locations / len(weatherData)) * 100
    print('\nLocations with the fewest records with percentages:')
    print(percentages)
    
    plt.figure(figsize=(10, 5))
    plt.pie(percentages, labels=lowest_five_locations.index, autopct='%1.1f%%', startangle=140)
    plt.title('Locations with the fewest records')
    plt.show()

unique_locations()