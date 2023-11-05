import pandas as pd

df = pd.read_csv("Recent_10_Year_Outbound.csv", na_values=[''])

yearly_changes = [8.3, 20.1, 15.9, 18.4, 8.3, 0.1, -85.1, -71.4, 436.1, 420.2]

missing_values_by_country = df.isna().sum()

print("각 국가별 결측치 개수:")
print(missing_values_by_country)

def fill_missing_values(row, idx, df, changes):
    for country in df.columns[1:]:  # 'Year' 열 이후의 모든 국가에 대해 반복
        if pd.isna(row[country]):
            # 이전 연도 값으로부터 채우기
            if idx > 0 and pd.notna(df.at[idx - 1, country]):
                prev_year_value = df.at[idx - 1, country]
                row[country] = prev_year_value * (1 + changes[idx - 1] / 100)
            # 다음 연도 값으로부터 채우기
            elif idx < len(df) - 1 and pd.notna(df.at[idx + 1, country]):
                next_year_value = df.at[idx + 1, country]
                row[country] = next_year_value / (1 + changes[idx] / 100)
    return row

df = df.apply(lambda row: fill_missing_values(row, row.name, df, yearly_changes), axis=1)

output_file_path = "결과를_저장할_파일_경로.csv"
df.to_csv(output_file_path, index=False)

print("결과가 저장된 파일 경로:", output_file_path)
