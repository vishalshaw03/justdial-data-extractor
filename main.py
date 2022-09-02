import requests
from helpers.extract import extractContent
import csv

from helpers.utils import (
    checkFilePath,
    coloredInput,
    errorMessage,
    infoMessage,
    successMessage,
)

# url = "https://www.justdial.com/Kolkata/Tutorials-For-Gate/nct-10502744"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}


def main():
    page = 0
    url = ""
    fileName = ""
    fieldnames = ["Name", "Phone", "Address"]
    csvfile = None
    writer = None

    try:
        url = coloredInput("Enter the URL: ")

        if not url:
            errorMessage("Invalid URL!")
            exit(1)

        fileName = coloredInput("Enter the output FileName: ")

        fileName = checkFilePath(fileName)

        if not fileName:
            errorMessage("Invalid FileName!")
            exit(1)

        csvfile = open(fileName, "w", newline="")
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        infoMessage("\nFetching data...")
        res = requests.get(url, headers=headers)

        while extractContent(res.content, writer) != 0:
            page += 1
            if page == 25:
                break

            res = requests.get(url + "/page-" + str(page), headers=headers)

        successMessage("Extract complete!")

    except Exception as e:
        errorMessage("Error!")
        print(e)

    finally:
        csvfile.close()


main()
