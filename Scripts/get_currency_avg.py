import pandas as pd
import requests
from datetime import datetime, timedelta

# 국가 코드와 통화 데이터프레임 생성
cnt_code_with_currency = {
    'CNT_CODE': ['JP', 'CN', 'VN', 'TH', 'PH', 'HK', 'TW', 'MO', 'SG', 'MY', 'ID', 'KH', 'TR', 'IN', 'MN', 'MM', 'ES', 'DE', 'AU', 'GB', 'SI', 'RU', 'US', 'CA', 'MX', 'AU', 'NZ'],
    'CURRENCY': ['JPY', 'CNH', 'VND', 'THB', 'PHP', 'HKD', 'TWD', 'MOP', 'SGD', 'MYR', 'IDR', 'KHR', 'TRY', 'INR', 'MNT', 'MMK', 'EUR', 'EUR', 'AUD', 'GBP', 'EUR', 'RUB', 'USD', 'CAD', 'MXN', 'AUD', 'NZD']
}
cc_df = pd.DataFrame(cnt_code_with_currency)

# 날짜 포매팅 함수
def format_date(date):
    return date.strftime('%Y%m%d')

# API URL 설정
base_url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
authkey = 'QFenQjzBrzZixROTFHyY5QN2IMkUmZ0e'
data = 'AP01'

# 환율 평균값을 저장할 데이터프레임 초기화
rates_df = pd.DataFrame()

# 날짜 설정: 최근 6개월
end_date = datetime.now() - timedelta(days=1)
start_date = end_date - timedelta(days=180)

# 각 국가별 환율 데이터 수집
while start_date <= end_date:
    if start_date.weekday() < 5:  # 주말 제외
        searchdate = format_date(start_date)
        url = f'{base_url}?authkey={authkey}&searchdate={searchdate}&data={data}'

        try:
            response = requests.get(url).json()
            if response:
                ex_pd = pd.DataFrame(response)
                ex_pd['ttb'] = ex_pd['ttb'].str.replace(',', '').str.extract('(\d+(?:\.\d+)?)').astype(float)

                # 각 국가별 환율 데이터를 cc_df와 병합
                merged_df = cc_df.merge(ex_pd[['cur_unit', 'ttb']], left_on='CURRENCY', right_on='cur_unit', how='left')
                rates_df = pd.concat([rates_df, merged_df[['CNT_CODE', 'CURRENCY', 'ttb']]], ignore_index=True)
                
        except requests.RequestException as e:
            print(f"Request Error: {e}")
        except pd.errors.EmptyDataError as e:
            print(f"Pandas Error: {e}")

    start_date += timedelta(days=1)

grouped = rates_df.groupby(['CNT_CODE', 'CURRENCY'])
avg_rates_df = grouped['ttb'].mean().reset_index()
count_rates_df = grouped['ttb'].count().reset_index()

# 'ttb' 열을 'EXCHANGE_AVG'로 이름 변경 및 데이터의 수 포함
avg_rates_df = avg_rates_df.rename(columns={'ttb': 'EXCHANGE_AVG'})
count_rates_df = count_rates_df.rename(columns={'ttb': 'VALID_COUNT'})

# 결과 데이터프레임 결합
final_df = pd.merge(avg_rates_df, count_rates_df, on=['CNT_CODE', 'CURRENCY'])

# 결과 저장
csv_output_path = 'country_currency_avg.csv'
final_df.to_csv(csv_output_path, index=False, encoding='utf-8')