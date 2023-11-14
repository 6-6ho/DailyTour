import pandas as pd

csv_path = 'OutBound_Data/Outbound_Month_Data.csv'
output_path = 'OutBound_Data/Outbound_Month_Data_Fillna.csv'

df = pd.read_csv(csv_path)

# 연도별 전년도 대비 증가율
increase_rates = {
    'month': [1, 2, 3, 4, 5, 6, 7, 8],
    'increase_rate': [0, 3, 17, -2, -11, -5, -18, 3]
}

rates_df = pd.DataFrame(increase_rates)


# 결측치 처리 함수 
def fill_missing_values(df, rates_df):
    for column in df.columns[1:]:
        
        for i in range(1, len(df)):
            # 현재 값이 NaN이고, 이전 연도의 값이 NaN이 아닌 경우 (아래로 내려가면서 채우기)
            if pd.isnull(df.at[i, column]) and not pd.isnull(df.at[i-1, column]):
                current_month = df.at[i, 'month']
                print(current_month)
                rate = rates_df.loc[rates_df['month'] == current_month, 'increase_rate'].iloc[0] / 100
                df.at[i, column] = df.at[i-1, column] * (1 + rate)
                
                # 첫 번째 값이 NaN이면 그 이후 첫 번째 비NaN 값을 찾아 역산을 수행 (위로 올라가면서 채우기)
            elif pd.isnull(df.at[0, column]):
                first_valid_index = df[column].first_valid_index()
                for j in range(first_valid_index-1, -1, -1):
                    rate = rates_df.loc[rates_df['month'] == df.at[j+1, 'month'], 'increase_rate'].iloc[0] / 100
                    df.at[j, column] = df.at[j+1, column] / (1 + rate)
    return df

filled_df = fill_missing_values(df, rates_df)

# 모든 값을 정수로 변환
for column in filled_df.columns[1:]:  # 'month' 컬럼을 제외
    filled_df[column] = filled_df[column].apply(lambda x: int(round(x)) if not pd.isnull(x) else x)

# 결과를 CSV 파일로 저장
filled_df.to_csv(output_path, index=False)
