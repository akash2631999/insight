import os
from libs.download_file import download_file
from swapper import swapper
import cv2

def clean_up_data(input_file, output_file):
    if os.path.exists(input_file):
        os.remove(input_file)
    if os.path.exists(output_file):
        os.remove(output_file)   
    print("data cleaned")    

def detect_file(input_img_url,output_img_url):
    input_path = download_file(input_img_url)
    output_path = download_file(output_img_url)
    
    try:
        result = swapper(input_path,output_path)
        _, result_data = cv2.imencode('.jpg', result)
        result_bytes = result_data.tobytes()
        return result_bytes
    finally:
        clean_up_data(input_path, output_path)
if __name__ == "__main__":
    detect_file()    