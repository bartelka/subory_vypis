nazov = input("Zadaj názov súboru, ktorý chceš prechádzať(napr.C:\\Program Files):")
import os

def folders(path, depth=0):
    for item in os.listdir(path):
        if os.path.isdir(path+"\\"+item) and item[0] not in ".$":
            print("-" * depth, item)
            if os.listdir(path+"\\"+item):
                folders(path+"\\"+item, depth+1)

folders(nazov)
