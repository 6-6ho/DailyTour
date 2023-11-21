import pandas as pd
import os


# region_path = '../Data/OutBound_Data/country_info.csv'
def seperate_file() : # 연도별 분리
    data_path = 'Data/OutBound_Data/Outbound_Month_Data_Fillna.csv'

    df = pd.read_csv(data_path, encoding='cp949')
    data = pd.DataFrame(df)
    print(data)

    for year in data['month']:
        year_df = data[data['month'] == year]
        save_to_csv(year, year_df)
        # year_df.to_csv(f'Data/Year_Data/{year}.csv', index=False, encoding='cp949')

def save_to_csv(year, year_df) :
     # 행과 열 바꾸기
    df_trans = year_df.transpose()
    
    country_list = df_trans.index[1:].tolist()      # 국가이름이 index로 되어 있어서 index를 가져와 리스트로 반환
    emi_list = df_trans.iloc[:,0][1:].tolist()     # 첫번째열(출국자 수)가져와 리스트로 반환
    month_list = [year] * len(country_list)
    #year_list = [year] * len(country_list)  # year 컬럼을 위한
    
    data = {
        'CNT_NAME' : country_list,
        'EMI' : emi_list,
        'YEAR' : 2023,
        'MONTH' : month_list

    }

    new_df = pd.DataFrame(data)
    print(new_df)

    new_df.to_csv(f'Data/Year_Data/Outbound_Data_{year}월.csv', encoding='utf-8', index=False)


def add_cntCode():
    reg_pd = pd.read_csv('Data/region_Data/region_data.csv', encoding='utf-8')
    country_df = pd.DataFrame(reg_pd)


    # reg_pd.to_csv('Data/region_Data/region_data2.csv', encoding='utf-8', index=False)


    directory = 'Data/Year_Data'  

    files = [file.split('.')[0] for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

    for file in files:
        fileName = file+ '.csv'
        filePath = os.path.join(directory, fileName)
        
        emi_df = pd.read_csv(filePath, index_col=0, encoding='utf-8')

        merged_df = pd.merge(emi_df, country_df, on='CNT_NAME', how='left')
        print(merged_df)
        merged_df.to_csv(f'Data/Year_Data/{file}_merge.csv', encoding='utf-8', index=False)



def save_to(year, year_df) :
    # 파일들이 저장된 디렉토리
    directory = 'Data/Year_Data'  

    # 디렉토리 내의 모든 CSV 파일 이름 읽기
    files = [file.split('.')[0] for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

    # 각 파일을 읽어와 행과 열을 바꾼 후 저장
    for file in files:

        fileName = file + '.csv'
        file_path = os.path.join(directory, fileName)
        
        # CSV 파일을 DataFrame으로 읽어오기
        df = pd.read_csv(file_path, index_col=0, encoding="cp949")
        
        # 행과 열 바꾸기
        df_transposed = df.transpose()

        # print(df_transposed)
        df_transposed = df_transposed.rename_axis('cnt_name')
        df_transposed['year'] = file
        # df_transposed.rename(columns={ file : 'emi'} , inplace=True)

        # header = df_transposed.iloc[0]
        # print(header)
        # df_transposed = df_transposed.iloc[1:]

        # df_transposed = df_transposed.drop(10, axis=0)
        print(df_transposed)

        # df_transposed.columns = header
        # df_transposed.rename(columns={ file : 'emi'} , inplace=True)

        # print(df_transposed)

        # 새로운 파일 이름 생성 (기존 파일 이름에 '_transposed' 추가)
        # new_file_name = file.split('.')[0] + '_transposed.csv'
        # new_file_path = os.path.join(directory, new_file_name)
        
        # # 행과 열이 바뀐 DataFrame을 CSV 파일로 저장
        # df_transposed.to_csv(new_file_path, encoding="cp949")

    print("Files transposed and saved successfully.")

def main() :
    add_cntCode()
    # seperate_file()

if __name__ == '__main__' :
    main()