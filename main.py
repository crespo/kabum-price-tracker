import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    url = 'http://google.com/'
    browser = get_web_driver()
    browser.get(url)

    try:
        name = browser.find_element(By.XPATH, '//*[@id="__next"]/main/article/section/div[2]/h1').text
    except selenium.common.exceptions.NoSuchElementException:
        name = 'Not Found'

    try:
        price = browser.find_element(By.XPATH, '//*[@id="blocoValores"]/div[3]/b').text\
            .replace("R$ ", "").replace(".", "").replace(",", ".")
    except selenium.common.exceptions.NoSuchElementException:
        price = 'Not Found'

    print("name: " + name +
          "\nprice: " + price)


def get_web_driver():
    optional = webdriver.ChromeOptions()
    optional.headless = True
    driver = webdriver.Chrome(options=optional)
    return driver


if __name__ == '__main__':
    main()
