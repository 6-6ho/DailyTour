import pandas as pd

def func():

    csv_file_path = '../Data/google-trend/domestic.csv'

    travel_df = pd.read_csv(csv_file_path)

    first_column_name = travel_df.columns[0]

    travel_df[first_column_name] = travel_df[first_column_name].str.replace('여행', '').str.replace('해외', '').str.replace('국내', '').str.strip()

    travel_df = travel_df[travel_df[first_column_name] != '']

    travel_df.to_csv('../Data/google-trend/domestic_1.csv')


    csv_file_path = '../Data/google-trend/overseas.csv'

    travel_df = pd.read_csv(csv_file_path)

    first_column_name = travel_df.columns[0]

    travel_df[first_column_name] = travel_df[first_column_name].str.replace('여행', '').str.replace('해외', '').str.replace('국내', '').str.strip()

    travel_df = travel_df[travel_df[first_column_name] != '']

    travel_df.to_csv('../Data/google-trend/overseas_1.csv')
    
        
def remove():
    domestic_path = '../Data/google-trend/domestic_1.csv'
    overseas_path = '../Data/google-trend/overseas_1.csv'
    
    domestic_df = pd.read_csv(domestic_path)['KEYWORD']
    overseas_df = pd.read_csv(overseas_path)
    
    for keyword in domestic_df:
        overseas_df = overseas_df[~overseas_df['KEYWORD'].str.contains(keyword, case=False, na=False)]

    overseas_df.to_csv("../Data/google-trend/result.csv")
    
    
if __name__=="__main__":
    func()
    remove()
