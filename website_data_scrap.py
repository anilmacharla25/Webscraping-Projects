from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
# Set the Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# Initialize the webdriver
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe",options=chrome_options)
# driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
df=pd.DataFrame({'Name':[''],'Address':[''],'Mobile Number':[''],'Email':['']})
# postal_codes = ["SW1W 0NY", "PO16 7GZ", "GU16 7HF", "L1 8JQ"]
postal_codes = ['SW1W 0NY', 'E14 5AB', 'B1 1RF', 'S1 2BX', 'WC2H 8LA', 'M1 5AN', 'SE1 7PB', 'EH1 1YZ', 'G2 3GF', 'NR2 1RG', 'CF10 1EP', 'BT1 1EG', 'AB10 1QB', 'TS1 1AA', 'KY1 1JN', 'BD1 1BL', 'LA1 1JZ', 'PO1 2RG', 'LU1 2EY', 'OX1 1HB']

for code in postal_codes:
    # Navigate to a URL
    driver.get(f'https://partner.uw.co.uk/search/results?q={code}&qp={code}&l=en_GB')
    name=driver.find_elements(By.CLASS_NAME,'Teaser-container')
    print(len(name))
    driver.implicitly_wait(10)
    for n in name:
        person_data=n.text.split('\n')
        df=df.append({'Name':person_data[0],'Address':person_data[1],'Mobile Number':person_data[2],'Email':person_data[3]},ignore_index=True)
        print('---------------')

    df.to_csv('partner_uw.csv')
    print(df)
driver.quit()
