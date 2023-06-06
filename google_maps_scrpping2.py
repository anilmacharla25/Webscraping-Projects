from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import sys
# Set the Chrome options
chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
import time
from webdriver_manager.chrome import ChromeDriverManager
df=pd.DataFrame([{'Business Name':'','Address':'','Description':'','Phone Number':'','Website':'','Reviews':'','Timings':'','Image link':''}])
import pandas as pd

# df = pd.DataFrame({'Business Name':'','Address':'','Description':'','Phone Number':'','Website':'','Reviews':'','Timings':'','Image link':''})

print(df)

# Initialize the webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com/maps/search/top+dermatologist+in+bangalore/')
time.sleep(10)
urls=driver.find_elements(By.CLASS_NAME,'hfpxzc')
print(len(urls))
for url in urls:
    url_link=url.get_attribute('href')
    # print(url_link)
    url.click()
    time.sleep(5)
    clinic_name=driver.find_element(By.CLASS_NAME,'lMbq3e')
    time.sleep(1)
    # print(clinic_name.text)
    clinic_name=clinic_name.text
    print(clinic_name.split('\n'))
    clinic_info_list=clinic_name.split('\n')
    
    clinic_title=clinic_info_list[0]
    rating=clinic_info_list[-3]
    reviews=clinic_info_list[-2]
    description=clinic_info_list[-1]
    print('------------printing address--------')
    address=driver.find_element(By.CLASS_NAME,'rogA2c ')
    time.sleep(1)
    print(address.text)
    address=address.text

    # list_data=driver.find_elements(By.CLASS_NAME,'AeaXub')
    # time.sleep(1)
    # for list in list_data:
    #     print(list.text)
    #     time.sleep(1)
    img_link=driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[1]/div[1]/button/img')
    print(img_link)
    time.sleep(1)
    img_link=img_link.get_attribute('src')
    print(img_link)
    try:
        website=driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[6]/a')
        time.sleep(1)
        site_link=website.get_attribute('href')
        print(site_link)
    except:
        print('site link not updated')
    time.sleep(1)
    mobile=driver.find_element(By.CLASS_NAME,'rogA2c ')
    print(mobile)
    time.sleep(1)
    print(mobile.text)
    mobile=mobile.text
    timing=driver.find_element(By.CLASS_NAME,'MkV9')
    time.sleep(1)
    print(timing.text)
    timings=timing.text
    print('----------------***------------------------')
    data4mobile=''
    list1=driver.find_elements(By.CLASS_NAME,'AeaXub')
    for list in list1:
        print(list.text)
        text=list.text
        data4mobile+=text
    
    try:
        mobile_num=re.search(r"\+\d{2}\s\d{5}\s\d{5}",data4mobile).group()
    except:
        mobile_num='NA'
    print(clinic_title,address,description,mobile_num,site_link,reviews,timings,img_link)
    print(mobile_num)
    print('==========================================================================')
    
    # df=pd.DataFrame([{'Business Name':clinic_title,'Address':address,'Description':description,'Phone Number':'','Website':'','Reviews':'','Timings':'','Image link':''}])

    

