import random
import pathlib

import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=%E9%B8%A3%E4%BA%BA+%E5%8A%A8%E6%BC%AB&sca_esv=27995ac6706bcd53&udm=2&biw=1678&bih=849&sxsrf=ADLYWIKmEATaCj7DXaPgQqCx4CjTor7Ecg%3A1735287592588&ei=KGNuZ6a1I5X12roPu7Sv8Ag&ved=0ahUKEwim6aeEwseKAxWVulYBHTvaC44Q4dUDCBE&uact=5&oq=%E9%B8%A3%E4%BA%BA+%E5%8A%A8%E6%BC%AB&gs_lp=EgNpbWciDem4o-S6uiDliqjmvKtI8SFQ4QJYhhtwA3gAkAEAmAGBAaABhwWqAQMxLjW4AQPIAQD4AQGYAgWgAuUBwgIEECMYJ8ICBRAAGIAEwgIHEAAYgAQYDJgDAIgGAZIHAzMuMqAH_gc&sclient=img"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
images = soup.find_all("img")

for image in images:
    print(image["src"])
    try:
        img_response = requests.get(image["src"])
        path = "train/mingren/" + str(random.randint(0, 10000)) + ".jpg"
        if not pathlib.Path(path).exists():
            pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "wb") as f:
            f.write(img_response.content)
    except Exception as e:
        print(e)
