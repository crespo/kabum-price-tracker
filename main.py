import requests
from bs4 import BeautifulSoup


def main():
    product = new_product('https://www.kabum.com.br/produto/270813/placa-de-video-asus-dual-nvidia-geforce-gtx-1650'
                          '-oc-4gb-gddr5-preto-90yv0cv2-m0na00')

    print(product.to_string())


def new_product(url):
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    name = soup.title.string
    price = soup.find(class_="regularPrice").string
    return Product(name, price)


class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def to_string(self):
        return 'name: ' + self.__name + '\nprice: ' + self.__price


if __name__ == '__main__':
    main()
