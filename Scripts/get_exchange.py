import pandas as pd
import requests

base_url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
authkey = 'QFenQjzBrzZixROTFHyY5QN2IMkUmZ0e'
data = 'AP01'
searchdate = '20231128'

url = f'{base_url}?authkey={authkey}&searchdate={searchdate}&data={data}'

response = requests.get(url).json()

ex_pd = pd.DataFrame(response)

print(ex_pd)