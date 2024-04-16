def get_file_name(url):
    url_list = url.split("/")
    last_url = url_list[len(url_list) - 1]
    file_name = last_url.split(".")[0]
    return file_name


if __name__ == "__main__":
    get_file_name()