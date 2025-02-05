import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {'user-agent': 'Mozilla/5.0 \
            (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/84.0.4147.105 Safari/537.36'}

urls = [
    'https://groww.in/us-stocks/nke',
    'https://groww.in/us-stocks/shop',
    'https://groww.in/us-stocks/rgti',
    'https://groww.in/us-stocks/spot',
    'https://groww.in/us-stocks/pltr',
    'https://groww.in/us-stocks/grab'
]

stonks = []

for url in urls:
    page = requests.get(url, headers=headers)

    if page.status_code != 200:
        print(f"Failed to fetch {url}, status code: {page.status_code}")
        continue

    soup = BeautifulSoup(page.text, 'html.parser')

    try:
        company = soup.find('h1', {'class': 'usph14Head displaySmall'}).text.strip()

        price = soup.find('span', {'class': 'uht141Pri contentPrimary displayBase'}).text.strip()

        change_element = soup.find('div', {'class': 'uht141Day bodyBaseHeavy contentNegative'})
        # if stock is going positive, different className to extract
        if not change_element:
            change_element = soup.find('div', {'class': 'uht141Day bodyBaseHeavy contentPositive'})
        change = change_element.text.strip() if change_element else "N/A"

        volume_cells = soup.find_all('td', {'class': 'bodyLargeHeavy'})
        volume = volume_cells[2].text.strip() if len(volume_cells) > 2 else "N/A"

        stonks.append([company, price, change, volume])

    except AttributeError as e:
        print(f"Could not extract data for {url}: {e}")
    
    time.sleep(5)


df = pd.DataFrame(stonks, columns=["Company", "Price", "Change", "Volume"])
df.to_excel('stocks.xlsx', index=False)

print('Done')

