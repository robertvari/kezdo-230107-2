import os, json
from PIL import Image, ExifTags
from openpyxl import Workbook

def main():
    folder = get_folder_path()
    photo_files = get_photos(folder)
    photo_data = collect_data(photo_files)
    
    save_data(photo_data, format="xlsx")

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

    # read image data
    for image_file in photo_list:
        img = Image.open(image_file)
        size = img.size
        exif_data = img._getexif()

        if not exif_data:  # skip images without exif data
            continue

        camera_model = exif_data.get(0x0110)
        date = exif_data.get(0x9003)
        iso = exif_data.get(0x8827)
        
        # add image data to photo_data
        photo_data[image_file] = {
            "size": size,
            "camera_model": camera_model,
            "date": date,
            "iso": iso
        }

    return photo_data

def save_data(photo_data: dict, format="json"):
    """This function saves data to .json format by default.
    \nxlsx format also suported.
    """

    def save_xlsx():
        workbook = Workbook()
        active_sheet = workbook.active

        active_sheet["A1"] = "File Path"
        active_sheet["B1"] = "Date"
        active_sheet["C1"] = "Size"
        active_sheet["D1"] = "Camera"
        active_sheet["E1"] = "ISO"

        for index, filepath in enumerate(photo_data):
            row = index + 3
            active_sheet[f"A{row}"] = filepath
            active_sheet[f"B{row}"] = photo_data[filepath]["date"]
            active_sheet[f"C{row}"] = str(photo_data[filepath]["size"])
            active_sheet[f"D{row}"] = photo_data[filepath]["camera_model"]
            active_sheet[f"E{row}"] = photo_data[filepath]["iso"]


        
        workbook.save("photo_data.xlsx")


    if format == "json":
        with open("photo_data.json", "w") as data_file:
            json.dump(photo_data, data_file)
        
        print("Data saved to photo_data.json")
    
    elif format == "xlsx":
        save_xlsx()
    
    else:
        print(f"Format: {format} not suported :(")

main()