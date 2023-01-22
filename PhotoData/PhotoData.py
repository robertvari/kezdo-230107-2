import os, json
from PIL import Image, ExifTags

def main():
    folder = get_folder_path()
    photo_files = get_photos(folder)
    photo_data = collect_data(photo_files)


def get_folder_path():
    folder_path = r"D:\Work\_PythonSuli\kezdo-230107\photos"
    check_folder_path(folder_path)
    
    return folder_path

def check_folder_path(folder_path):
    # check if path exists
    assert os.path.exists(folder_path), f"The path: {folder_path} doesn't exist :((("

    # check if this is a folder
    assert os.path.isdir(folder_path), f"The path: {folder_path} must be a directory. :((("

def get_photos(folder_path):
    # load files and folders from folder_path
    folder_content = os.listdir(folder_path)

    # todo: filter folder content. Only .jpg files allowed!
    alowed_extensions = ["jpg", "jpeg"]

    # filter folder_content and collect .jpg and .jpeg files
    photo_files = []
    for item in folder_content:
        full_path = os.path.join(folder_path, item)
        
        # todo skip folders
        if os.path.isdir(full_path):
            continue

        item_list = item.lower().split(".")
        extension = item_list[-1]

        if extension in alowed_extensions:
            photo_files.append(full_path)

    return photo_files

def collect_data(photo_list):
    photo_data = {}

    return photo_data

def save_data():
    pass

main()