import pandas as pd
import matplotlib.pyplot as plt


def pressure_change():
    '''
    This function reads the weatherData.csv file and calculates the difference between the pressure at 9am and 3pm.
    It then calculates the probability of rainfall for each value of the pressure difference.
    Creates new column 'PressureDiff' in the dataframe to store the absolute difference between 'Pressure9am' and 'Pressure3pm'.
    The function then calculates the number of rainy and non-rainy days for each value of the pressure difference.
    The function then plots via line graph the relationship between the pressure difference and the probability of rainfall.
    The function practices the use of pandas and matplotlib libraries.
    '''
    weatherData = pd.read_csv('weatherData.csv')
    relevant_columns = ['Pressure9am', 'Pressure3pm', 'RainTomorrow']
    weatherData = weatherData[relevant_columns]

    pressure_diffs = []
    rainfall_probabilities = []

    for D in range(1, 13):
        weatherData['PressureDiff'] =  weatherData['Pressure9am'] - weatherData['Pressure3pm']
        weatherData['PressureDiff'] = weatherData['PressureDiff'].abs()  # Absolute difference

        min_diff_rows = weatherData[weatherData['PressureDiff'] == D]

        rainy_count = min_diff_rows[min_diff_rows['RainTomorrow'] == 'Yes'].shape[0]
        non_rainy_count = min_diff_rows[min_diff_rows['RainTomorrow'] == 'No'].shape[0]

        print(f'For D = {D}:')
        print(f'  - Rainy days:   {rainy_count}')
        print(f'  - Non-rainy days: {non_rainy_count}')
        print() 

        if non_rainy_count > 0:
            rainfall_probability = rainy_count / non_rainy_count
        else:
            rainfall_probability = float('NaN')  

        pressure_diffs.append(D)
        rainfall_probabilities.append(rainfall_probability)

    plt.figure(figsize=(10, 6))
    plt.plot(pressure_diffs, rainfall_probabilities, marker='o', linestyle='-', color='b')
    plt.title('Relationship between Pressure Difference (D) and Rainfall Probability')
    plt.xlabel('Minimum Pressure Difference (D)')
    plt.ylabel('Ratio of Rainy Days to Non-Rainy Days')
    plt.xticks(range(1, 13))
    plt.grid(True)
    plt.tight_layout()
    plt.show()

pressure_change()