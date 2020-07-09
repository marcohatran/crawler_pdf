from pathlib import Path
import requests
filename = Path('test.pdf')
url = 'https://www.vcbs.com.vn/vn/Communication/GetReport?reportId=7666'
response = requests.get(url)
filename.write_bytes(response.content)