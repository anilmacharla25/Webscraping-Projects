#this code bypasses captcha and logins into portal of tcs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from python_anticaptcha import AnticaptchaClient,ImageToTextTask
import time

def get_captcha_text(location, size):
    # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"
    im = Image.open('screenshot.jpg')
    left = location['x']
    top = 500
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    im = im.crop((left, top, right, bottom)) # defines crop points
    im.save('screenshot.png')
    input('stop')
    print('------------------------------------------------>>>>>>>>>>>>>')
    # time.sleep(3)
    api_key = 'b2b510888e9324fdf42975d81168b15a'   # danish
    captcha_fp = open('screenshot.jpg', 'rb')
    client = AnticaptchaClient(api_key)
    task = ImageToTextTask(captcha_fp)
    job = client.createTask(task)
    job.join()
    time.sleep(3)
    # print(job.get_captcha_text())
    result = job.get_captcha_text()

    return result

path="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get('https://gbis.tcsapps.com/agency/')
print(driver.title)
uid=driver.find_element_by_xpath('//*[@id="loginForm:j_idt21"]')
uid.send_keys('uid')
pwd=driver.find_element_by_xpath('//*[@id="loginForm:j_idt26"]')
pwd.send_keys('pwd')

li = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID,'captchaImg')))
# li = driver.find_element(By.ID,'captchaImg')
location = li.location
# print(location)
size = li.size
# print(size,'******')
driver.save_screenshot('screenshot.jpg')
##input('stop')
captcha = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="captchaImg"]')))
captcha_text = get_captcha_text(location,size)
# print(captcha_text,'----------------------->>>>>>> CAPTCHA IMAGE')
captcha = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID,"loginForm:captcha"))).send_keys(captcha_text)
time.sleep(1)

time.sleep(5)
driver.quit()

