import pandas as pd
import numpy as np

# 보기 쉬운 데이터 넣기
data = {
    'year': [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Japan': [1234, 1255, 2222, 5533, 5799, 1000, np.nan, 123, 442, 56788], # 코로나로 인해 중간에 2020년때 -85.1%로 급격한 감소율을 보이는데 이때의 증가율 데이터가 잘 적용되는지 봄
    'China': [np.nan, 1000, 9297, 9924, 1262, 2346, 1235, 1235, 1236, 77777], # 2014년도 데이터를 제거해서 맨 처음 데이터가 없을때 역연산을 잘 하는지 테스트를 위한 데이터
    'Singapore': [1000, 1000, 1000, 1000, 1000, 1000, np.nan, np.nan, np.nan, np.nan], # 연속된 NaN 데이터에 대해서 아래로 내려가면서 잘 채우는지에 대해서 테스트하는 데이터
    'Vietnam': [555, 555, 555, 555, 555, 555, 555, 555, 555, 555], # NaN이 존재 하지 않는 데이터
    'UK': [np.nan, np.nan, 1000, 66666, 666666, 666, 666, 6666, 6666, 6666] # 연속된 NaN 데이터가 위에 여러개 존재하는 경우 테스트
}

# 연도별 전년도 대비 증가율
increase_rates = {
    'year': [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'increase_rate': [8.3, 20.1, 15.9, 18.4, 8.3, 0.1, -85.1, -71.4, 436.1, 420.2]
}

#데이터 프레임으로
df = pd.DataFrame(data)
rates_df = pd.DataFrame(increase_rates)

# NaN 값을 처리하는 함수를 정의합니다.
def fill_missing_values(df, rates_df):
    for column in df.columns[1:]:
        for i in range(1, len(df)):
            # 현재 값이 NaN이고, 이전 연도의 값이 NaN이 아닌 경우 (아래로 내려가면서 채우기)
            if pd.isnull(df[column].iloc[i]) and not pd.isnull(df[column].iloc[i-1]):
                current_year = df['year'].iloc[i]
                rate = rates_df['increase_rate'].loc[rates_df['year'] == current_year].values[0] / 100
                df[column].iloc[i] = df[column].iloc[i-1] * (1 + rate)
            # 첫 번째 값이 NaN이면 그 이후 첫 번째 비NaN 값을 찾아 역산을 수행 (위로 올라가면서 채우기)
            elif pd.isnull(df[column].iloc[0]):
                first_valid_index = df[column].first_valid_index()
                for j in range(first_valid_index-1, -1, -1):
                    rate = rates_df['increase_rate'].iloc[j+1] / 100
                    df[column].iloc[j] = df[column].iloc[j+1] / (1 + rate)
    return df

filled_df = fill_missing_values(df, rates_df)

# 모든 값을 정수로 변환
for column in filled_df.columns[1:]:  # 'year' 컬럼을 제외
    filled_df[column] = filled_df[column].apply(lambda x: int(round(x)) if not pd.isnull(x) else x)
    
    
print(filled_df)