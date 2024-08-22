import pandas as pd

def subDataFrame():
    """
    Creates a sub-dataframe with specific attributes from the columns given.
    Excludes rows where values in 'WindDir9am', 'WindGustDir', or 'WindDir3pm' have 3-letter inputs.
    """
    file_path = 'weatherData.csv'

    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print("File not found. Please make sure the file path is correct.")
        return None
    except pd.errors.EmptyDataError:
        print("File is empty. Please provide a non-empty CSV file.")
        return None
    except pd.errors.ParserError:
        print("Error parsing CSV file. Please make sure the file format is correct.")
        return None

    # Define required columns
    required_columns = ['RainTomorrow', 'WindDir9am', 'WindGustDir', 'WindDir3pm']
    
    # Check for missing columns
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        print(f"Error: Missing required columns in the dataset: {', '.join(missing_columns)}")
        return None

    # Filter out rows where any of the specified columns contain 3-letter inputs
    sub_df = df[
        (df['WindDir9am'].apply(lambda x: len(str(x)) != 3)) &
        (df['WindGustDir'].apply(lambda x: len(str(x)) != 3)) &
        (df['WindDir3pm'].apply(lambda x: len(str(x)) != 3))
    ][required_columns]

    return sub_df

# Call the function and print the result
result_sub_df = subDataFrame()

if result_sub_df is not None:
    print(result_sub_df)
