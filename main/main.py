from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
#driver.add_argument("--headless")
driver.get(
    'https://agendamentosonline.mne.gov.pt/AgendamentosOnline/app/scheduleAppointmentForm.jsf')

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="scheduleForm:tabViewId:ccnum"]')))


username = driver.find_element(By.XPATH, '//*[@id="scheduleForm:tabViewId:ccnum"]').send_keys('') #id goes here
    
password = driver.find_element(By.XPATH,
    '//*[@id="scheduleForm:tabViewId:dataNascimento_input"]').send_keys('') #date of birth goes here
button = driver.find_element(By.XPATH,
    '//*[@id="scheduleForm:tabViewId:searchIcon"]').click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="scheduleForm:postcons_label"]')))

cookie = driver.find_element(By.XPATH,
    '//*[@id="j_idt313"]').click()

posto = driver.find_element(By.XPATH,'//*[@id="scheduleForm:postcons_label"]').click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'ui-selectonemenu-items ui-selectonemenu-list ui-widget-content ui-widget ui-corner-all ui-helper-reset')]")))
ul = driver.find_element(By.XPATH,
    "//ul[contains(@class, 'ui-selectonemenu-items ui-selectonemenu-list ui-widget-content ui-widget ui-corner-all ui-helper-reset')]").click()

actions = ActionChains(driver)
actions.send_keys(Keys.DOWN)
actions.send_keys(Keys.ENTER)
actions.perform()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="scheduleForm:email"]')))
email = driver.find_element(
    By.XPATH, '//*[@id="scheduleForm:email"]')
email.clear()
email.send_keys("email") #email goes here

categoria = driver.find_element(
    By.XPATH, '//*[@id="scheduleForm:categato_label"]').click()

actions.send_keys(Keys.DOWN)
actions.send_keys(Keys.DOWN)
actions.send_keys(Keys.ENTER)
actions.perform()

time.sleep(0.5)
ato = driver.find_element(
    By.XPATH, '//*[@id="scheduleForm:atocons_label"]').click()
actions.send_keys(Keys.DOWN)
actions.send_keys(Keys.ENTER)
actions.perform()

adicionar = driver.find_element(
    By.XPATH, '//*[@id="scheduleForm:bAddAto"]').click()

time.sleep(1)
temp = driver.find_element(By.XPATH, '//*[@id="scheduleForm:dataTableListaAtos:0:j_idt104_content"]').click()

actions.send_keys(Keys.END)
actions.perform()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="scheduleForm:dataTableListaAtos:0:selCond_input"]')))

accept_conditions = driver.find_element(
    By.XPATH, '//*[@id="scheduleForm:dataTableListaAtos:0:selCond"]').click()

time.sleep(0.5)
submit = driver.find_element(
    By.XPATH, '//*[@id="scheduleForm:dataTableListaAtos:0:bCal"]').click()
keyword = input("enter a character or press enter to continue")
