import pandas as pd
import requests

cnt_code_with_currency = {
    'CNT_CODE': ['JP', 'CN', 'VN', 'TH', 'PH', 'HK', 'TW', 'MO', 'SG', 'MY', 'ID', 'KH', 'TR', 'IN', 'MN', 'MM', 'ES', 'DE', 'AU', 'GB', 'SI', 'RU', 'US', 'CA', 'MX', 'AU', 'NZ'],
    'CURRENCY': ['JPY', 'CNH', 'VND', 'THB', 'PHP', 'HKD', 'TWD', 'MOP', 'SGD', 'MYR', 'IDR', 'KHR', 'TRY', 'INR', 'MNT', 'MMK', 'EUR', 'EUR', 'AUD', 'GBP', 'EUR', 'RUB', 'USD', 'CAD', 'MXN', 'AUD', 'NZD']
}

cc_df = pd.DataFrame(cnt_code_with_currency)

authkey = 'QFenQjzBrzZixROTFHyY5QN2IMkUmZ0e'
searchdate = '20231129'
data = 'AP01'

url = f' https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={authkey}&searchdate={searchdate}&data={data}'

response = requests.get(url).json()
ex_pd = pd.DataFrame(response)

csv_output_path = '../Data/DB/country_currency.csv'
save_df.to_csv('../Data/DB/country_currency.csv', index=False, encoding='utf-8')