from bs4 import BeautifulSoup, element
import csv
from helpers.phone import generate_number, get_data_bw, return_op

def getDigitMap(content: bytes) -> dict:
    css = get_data_bw(str(content), ".icon-", ".mobilesv")
    dmap = return_op(css)

    return dmap


def storeContent(item: element.Tag, dmap: dict, fileWriter: csv.DictWriter) -> None:
    instituteName = ""
    phoneNo = ""
    address = ""
    try:
        instituteName = item.find("span", class_="lng_cont_name").get("data-cn")

        contactElement = item.find("p", class_="contact-info")
        phoneNo = generate_number(contactElement, dmap)

        addressElement = item.find("span", class_="cont_fl_addr")
        address = addressElement.get_text()

        # print(instituteName, phoneNo, address)

        fileWriter.writerow(
            {"Name": instituteName, "Phone": phoneNo, "Address": address}
        )
    except:
        # print("err")
        pass


def extractContent(content: bytes, fileWriter: csv.DictWriter) -> int:

    soup = BeautifulSoup(content, "html.parser")
    # soup = BeautifulSoup(content,"lxml")

    items = soup.find_all("li", class_="cntanr")

    if len(items) == 0:
        return 0

    dmap = getDigitMap(content)

    for item in items:
        storeContent(item, dmap, fileWriter)

    return len(items)
