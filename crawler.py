from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path='/home/renan/Documents/workspace/python/cblol_stats/geckodriver')
url = "https://lolesports.com/schedule?leagues=cblol-brazil"

def getData(url):
    driver.get(url)

    for i in range (0,4):
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

        print(driver.get_window_position(windowHandle='current')['y'])

        time.sleep(1.4)

    # driver.set_window_position(0, 0, windowHandle='current')
    
    home_team_names = []

    dates = []

    for i in range (3,48,5):
        dates.append(driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[2]/div[{}]/div/span[3]'.format(i)).text)

        print(dates)

    home_team_names.append(driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[2]/div[1]/a/div[2]/div[1]/div/h2/span[2]').text)

    print(home_team_names)
    print(dates)

    driver.close()

getData(url)