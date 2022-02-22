from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime
import calendar
import authorization

now = datetime.date.today()

# кол-во дней в месяце
border = calendar.monthrange(now.year, now.month)

driver = webdriver.Chrome()
driver.get(authorization.site)
time.sleep(2)


element = driver.find_elements(By.NAME, 'phone')
element[0].send_keys(authorization.telephone_number)
element = driver.find_elements(By.NAME, 'code')
element[0].send_keys(authorization.code)
element = driver.find_element(By.XPATH, '//button[@type="submit"]')
element.click()
time.sleep(2)


# Находим элемент начального пункта отправления
element = driver.find_element(By.XPATH, '//div[@class="sc-chPdSV gWxTLm"]')
element.click()
time.sleep(2)
# Находим элемент поиска
element = driver.find_element(By.XPATH, '//input[@placeholder="Поиск"]')
# Вводим НПО
element.send_keys(authorization.pointA)
# Находим по введенным данным НПО
element = driver.find_element(By.XPATH, '//div[@class="sc-ckVGcZ kRavWO"]')
element.click()
# Находим элемент конечного пункта отправления
element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div/form/div/div[1]/div[1]/div[3]/div[1]')
element.click()
# Находим элемент поиска
element = driver.find_element(By.XPATH, '//input[@class="sc-dnqmqq bRNGuv"]')
# Вводим КПО
element.send_keys(authorization.pointB)
# Находим по введенным данным КПО
element = driver.find_element(By.XPATH, '//div[@class="sc-ckVGcZ kRavWO"]')
element.click()


# находим календарь
element = driver.find_element(By.XPATH, '//div[@class="sc-bwzfXH frCQpJ"]')
element.click()
# находим сегодня
today = driver.find_element(By.XPATH, "//div[@class='DayPicker-Day DayPicker-Day--selected DayPicker-Day--today']")
if (int(today.text) + 7) > border[1]:
    difference = int(today.text)+7 - border[1]
    # перелистываем месяц
    element = driver.find_element(By.XPATH, "//*[@id='findBusForm']/div/form/div/div[3]/div[2]/div/div/div/div[1]/span[2]")
    element.click()
    time.sleep(10)
    element = driver.find_element(By.XPATH, f"//*[contains(text(), {difference})]")
    element.click()
else:
    # нашел этот же день на след неделе
    element = driver.find_element(By.XPATH, f"//div[contains(text(), {int(today.text)+7})]").click()

# поиск билетов
element = driver.find_element(By.XPATH, '//*[@id="findBusForm"]/div/form/button')
element.click()
time.sleep(3)
# находим время отправления
element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[3]/div[2]/button")
element.click()
driver.close()
exit("НЕТ МЕСТ")
time.sleep(3)
try:
    # находим начальную остановку
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/form/div/div[1]/div")
    element.click()
except:
    driver.close()
    exit("НЕТ МЕСТ")
# Находим элемент поиска
element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/form/div/div[1]/div[2]/div[1]/input')
element.click()
element.send_keys("Автостанция")
# выбираем
element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/form/div/div[1]/div[2]/div[2]/div")
element.click()
# time.sleep(3)
# находим конечную ост
element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/form/div/div[3]/div[1]")
element.click()
# time.sleep(3)
# выбираем конечную ост
element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/form/div/div[3]/div[2]/div[2]/div")
element.click()
time.sleep(10)
# бронируем
# element = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/form/button").click()
# time.sleep(30)









# res = requests.get('https://obs.by')
#
#
# print(res.text)
