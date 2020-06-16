from bs4 import BeautifulSoup
from selenium import webdriver
from .image_search import image_search

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
browser = webdriver.Chrome('websearch/chromedriver', chrome_options=options)


def find_shopping_url(url):
    try:
        print('find_shopping_url : ', url)
        browser.get(url)
        url_shopping = browser.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[4]/a').get_attribute('href')
        return url_shopping
    except:
        return None


def find_other_web_sites(url):
    try:
        print('find_other_web_sites : ', url)
        browser.get(url)
        url_others = browser.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[1]/a').get_attribute('href')
        return url_others
    except:
        return None


def change_input_value(url):
    browser.get(url)
    input_field = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input')
    current_value = input_field.get_attribute('value')
    input_field.clear()
    input_field.send_keys('acheter ' + current_value)
    submit_button = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/button')
    submit_button.click()
    sites_urls = browser.find_elements_by_css_selector('.r > a')
    return sites_urls # browser.current_url


def scrap_similar(url):
    browser.get(url)
    inner_html = browser.execute_script("return document.body.innerHTML")
    soup = BeautifulSoup(inner_html, "html.parser")
    elements = soup.find_all('div', {'class': 'sh-dgr__content'})
    objects = []

    for elem in elements:
        obj = {
            'title': elem.find('a', {'class': 'EI11Pd'}).text,
            'price': elem.find('span', {'class': 'Nr22bf'}).text,
            'image': elem.find('img')['src']
        }
        objects.append(obj)
    return objects


def run(image):
    try:
        image_url = image_search(image)
        shopping_url = find_shopping_url(image_url)
        url_others = find_other_web_sites(image_url)
        new_url_others = change_input_value(url_others)
        new_url_others = [link.get_attribute('href') for link in new_url_others]
        return shopping_url, new_url_others  # scrap_similar(shopping_url)
    except :
        return None
