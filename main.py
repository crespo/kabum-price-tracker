from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    url = 'https://www.kabum.com.br/produto/15296/cartucho-de-tinta-epson-133-ciano-t133220'

    browser = get_web_driver()
    browser.get(url)

    name = browser.find_element(By.XPATH, '//*[@id="__next"]/main/article/section/div[2]/h1').text
    price = browser.find_element(By.XPATH, '//*[@id="blocoValores"]/div[3]/b').text\
        .replace("R$ ", "").replace(".", "").replace(",", ".")

    print("name: " + name +
          "\nprice: R$" + price)


def get_web_driver():
    optional = webdriver.ChromeOptions()
    optional.headless = True
    driver = webdriver.Chrome(options=optional)
    return driver


if __name__ == '__main__':
    main()
