import pandas as pd

# CSV 파일 경로
csv_path = "Recent_10_Year_Outbound.csv"

# CSV 파일 불러오기
df = pd.read_csv(csv_path, na_values=['', ' '])

# 연도별 출국자수 증가율 리스트
yearly_changes = [8.3, 20.1, 15.9, 18.4, 8.3, 0.1, -85.1, -71.4, 436.1, 420.2]

# 결측치 채우기
for col in df.columns[1:]:
    for i in range(1, len(df)):
        if pd.isnull(df.at[i, col]):
            # 이전 년도로 결측치를 채우기 시도
            df.at[i, col] = df.at[i-1, col] * (1 + yearly_changes[i-1] / 100)
            
            # 만약 이전 년도로 결측치를 채웠는데 그 결과가 결측치라면 다음 년도로 시도
            if pd.isnull(df.at[i, col]):
                df.at[i, col] = df.at[i+1, col] * (1 + yearly_changes[i] / 100)

# 결과 출력
print("각 국가별 결측치 개수:")
print(df.isna().sum())

# 결과 저장
output_file_path = "Recent_10_Year_Outbound_Not_Nan.csv"
df.to_csv(output_file_path, index=False)

print("결과가 저장된 파일 경로:", output_file_path)
