import os
from libs.get_file_name import get_file_name
import requests


def download_file(url, extension="jpg"):
    file_name = get_file_name(url)
    file_to_write_in = os.path.join("/tmp", "{}.{}".format(file_name, extension))
    response = requests.get(url, allow_redirects=True)
    file = open(file_to_write_in, "wb")
    file.write(response.content)
    file.close()
    print("file downloaded")
    return file_to_write_in

if __name__ == "__main__":
    download_file()
