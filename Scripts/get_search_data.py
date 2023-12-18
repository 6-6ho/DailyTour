import os
import pandas as pd
import glob

def aggregate_search_volumes(file_pattern):
    # Initialize a list to hold all the DataFrames
    dataframes = []

    # Loop through all files matching the pattern and add their DataFrame to the list
    for file in glob.glob(file_pattern):
        df = pd.read_csv(file)
        dataframes.append(df)

    # Concatenate all DataFrames in the list
    all_data = pd.concat(dataframes, ignore_index=True)

    # Group by country and sum the search volumes
    aggregated_data = all_data.groupby('COUNTRY_NM')['SCCNT_SM_VALUE'].sum().reset_index()
    aggregated_data.columns = ['CNT_NAME', 'SEARCH_VOL']

    # Sort the results in descending order of search volume
    aggregated_data.sort_values('SEARCH_VOL', ascending=False, inplace=True)

    return aggregated_data

def save_to_csv(df, output_file):
    # Save the DataFrame to a CSV file
    df.to_csv(output_file, index=False, encoding='utf-8')

def main_process():
    # Define the input directory where the CSV files are located
    input_directory = '../Data/Search_Data'
    # Define the output directory where the aggregated CSV file will be saved
    output_directory = '../Data/'
    # Specify the pattern to match the files
    file_pattern = os.path.join(input_directory, 'DM_OVSEA_TOUR_*.csv')
    # Specify the output file name
    output_filename = 'aggregated_search_volumes.csv'

    # Aggregate the search volumes
    aggregated_data = aggregate_search_volumes(file_pattern)
    # Define the full path to the output file
    output_file = os.path.join(output_directory, output_filename)
    # Save the aggregated data to the CSV file
    save_to_csv(aggregated_data, output_file)
    print(f'Aggregated search volume data saved to {output_file}')

if __name__ == '__main__':
    main_process()
