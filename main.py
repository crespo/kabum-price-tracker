import requests
from bs4 import BeautifulSoup


def main():

    r = requests.get('https://www.kabum.com.br/produto/270813/placa-de-video-asus-dual-nvidia-geforce-gtx-1650-oc-4gb'
                     '-gddr5-preto-90yv0cv2-m0na00').text
    soup = BeautifulSoup(r, 'html.parser')

    name = soup.title.string
    price = soup.find(class_="regularPrice").string

    print("name: " + name +
          "\nprice: " + price)


if __name__ == '__main__':
    main()
