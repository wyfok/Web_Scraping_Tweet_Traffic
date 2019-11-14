from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


# Function of waiting until the present of the element on the web page
def waiting_func(by_variable, attribute):
    try:
        WebDriverWait(driver, 10).until(lambda x: x.find_element(by=by_variable,  value=attribute))
    except (NoSuchElementException, TimeoutException):
        print('{} {} not found'.format(by_variable, attribute))
        exit()


# Function to find the total height of the web page
'''
def scroll_height(start, end, step):
    _ = start
    while _ < end:
        yield _
        _ += step
    yield end
'''

# Access to Twitter
url = r'https://twitter.com'
driver = webdriver.Chrome()
driver.get(url)

# Find login box
waiting_func('class name', 'js-signin-email')
email = driver.find_element_by_class_name('js-signin-email')
email.send_keys('YOUR EMAIL ADDRESS')
password = driver.find_element_by_name('session[password]')
password.send_keys('YOUR PASSWORD', Keys.ENTER)

# Find profile icon
waiting_func('css selector', "[aria-label=Profile]")
profile = driver.find_element_by_css_selector("a[aria-label='Profile']")
profile.click()

'''
SCROLL_PAUSE_TIME = 3

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


path = []

for i in scroll_height(0, last_height, 500):
    driver.execute_script("window.scrollTo(0, {});".format(i))
    tweet = driver.find_elements_by_css_selector("article[role='article']")
    for j in tweet:
        waiting_func('css selector', "a[aria-label='View Tweet activity']")
        traffic = j.find_element_by_css_selector("a[aria-label='View Tweet activity']")
        traffic_link = traffic.get_attribute('href')
        if traffic_link not in path:
            path.append(traffic_link)
'''


path = []
while True:
    waiting_func('css selector', "a[aria-label='View Tweet activity']")
    last_height = driver.execute_script("return document.body.scrollHeight")
    traffic_path = driver.find_elements_by_css_selector("a[aria-label='View Tweet activity']")
    path.extend([traffic.get_attribute('href') for traffic in traffic_path])
    driver.execute_script("window.scrollTo(0, {})".format(last_height+500))
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if last_height == new_height:
        break

for i in path:
    driver.get(i)
    waiting_func('id', 'react-root')
    a = driver.find_element_by_id('react-root')
    waiting_func('css selector', "iframe[class='r-1yadl64 r-16y2uox']")
    b = driver.find_element_by_css_selector("iframe[class='r-1yadl64 r-16y2uox']")
    waiting_func('tag name', 'iframe')
    iframe = driver.find_element_by_tag_name('iframe')
    driver.switch_to.frame(iframe)
    #waiting_func('class name', 'ep-TweetPerformance')
   # #c = driver.find_element_by_class_name('ep-TweetPerformance')
    detail = driver.find_element_by_tag_name('body')

    waiting_func('class name', 'ep-MetricTopContainer')
    impression = detail.find_element_by_class_name('ep-MetricTopContainer')
    print(impression.text)
    try:
        WebDriverWait(driver, 3).until(
            lambda x: x.find_element(by='class name', value='ep-ViewAllEngagementsButton'))
    except TimeoutException:
        continue
    view_all = driver.find_element_by_class_name('ep-ViewAllEngagementsButton')
    view_all.click()
    waiting_func('class name', 'ep-EngagementsSection')
    engagesection = driver.find_element_by_class_name('ep-EngagementsSection')
    waiting_func('class name', 'ep-MetricTopContainer')
    engagement = engagesection.find_element_by_class_name('ep-MetricTopContainer')
    print(engagement.text)
    waiting_func('class name', 'ep-DetailedEngagementsSection')
    detail = engagesection.find_element_by_class_name('ep-DetailedEngagementsSection')
    waiting_func('class name', 'ep-SubSection')
    engagement_details = detail.find_elements_by_class_name('ep-SubSection')
    for _ in engagement_details:
        print(_.text)
