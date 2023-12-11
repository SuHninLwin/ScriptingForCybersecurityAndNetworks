"""
file_creator.py
Creating directory first
Then, creates text file and json file
to show data in them under current directory
"""
import os
import json
import shutil
import table_drawer


def creating_dir(foldername):
    """
    This function takes one parameter (string value)
    for creating the folder name.
    Creating the new directory under current working directory.
    If the given directory is exist,
    it removes that directory and recreate as new one.
    """
    print("Getting current directory ... ")
    directory = os.getcwd()
    print(f"Current directory: {directory}")
    print()
    print(f"Your folder name to be built: {foldername}")
    new_directory = os.path.join(directory, foldername)
    print("Directory is building ...")
    print()
    try:
        os.mkdir(new_directory)
    except FileExistsError:
        print("[-] Your directory has already exist.")
        print("Recreating your directory ...")
        # Modified from stackoverflow
        # Author: Ted Klein Bergman
        # Edited Time: Aug 24 '19 at 13:19
        shutil.rmtree(new_directory)
        # Removes the whole directory and creates the new directory
        os.mkdir(new_directory)
    print()
    print(f"Successfully build: {new_directory}")
    print()
    return new_directory


def creating_file(filename, dirname, writing_txt):
    """
    This function takes three parameters (string, string, list).
    Creating the new file under defined directory.
    It writes the texts from writing_txt into created file.
    """
    print(f"Your file name to be built: {filename}")
    file_path = os.path.join(dirname, filename)
    print("Writing to file ... ")
    with open(file_path, "a", encoding="utf-8") as file:
        for write_txt in writing_txt:
            if writing_txt.index(write_txt) in [0, 1, 2]:
                for key in write_txt:
                    file.writelines("\n")
                    file.writelines(key)
                    file.writelines("\n")
                    file.writelines(
                        str(table_drawer.packet_table_drawer(write_txt[key])))
                    file.writelines("\n\n")
            elif writing_txt.index(write_txt) == 3:
                for key in write_txt:
                    file.writelines("\n")
                    file.writelines(key)
                    file.writelines("\n")
                    file.writelines(
                        str(table_drawer.email_table_drawer(write_txt[key])))
                    file.writelines("\n\n")
            elif writing_txt.index(write_txt) == 4:
                for key in write_txt:
                    file.writelines("\n")
                    file.writelines(key)
                    file.writelines("\n")
                    file.writelines(
                        str(table_drawer.image_table_drawer(write_txt[key])))
                    file.writelines("\n\n")
            elif writing_txt.index(write_txt) == 5:
                for key in write_txt:
                    file.writelines("\n")
                    file.writelines(key)
                    file.writelines("\n")
                    file.writelines(
                        str(table_drawer.uri_table_drawer(write_txt[key])))
                    file.writelines("\n\n")
            elif writing_txt.index(write_txt) in [6, 7, 8]:
                for key in write_txt:
                    file.writelines("\n")
                    file.writelines(key)
                    file.writelines("\n")
                    file.writelines(
                        str(table_drawer.ips_table_drawer(write_txt[key])))
                    file.writelines("\n\n")
        print()
        print("Successfully written into text file. ")


def creating_json(jsonname, dirname, writing_txt):
    """
    This function takes three parameters (string, string, list).
    Creating the new json file under defined directory.
    It writes the texts from writing_txt
    into created json file as json file format.
    """
    json_dict = {}
    for json_list in writing_txt:
        tuple_json = tuple(json_list)
        dict_json = dict((key, value) for key, value in tuple_json)
        if writing_txt.index(json_list) == 0:
            json_dict.update({"Src To Dst IP <TCP>": dict_json})
        elif writing_txt.index(json_list) == 1:
            json_dict.update({"Src To Dst IP <UDP>": dict_json})
        elif writing_txt.index(json_list) == 2:
            json_dict.update({"Src To Dst IP <IGMP>": dict_json})
    print(f"Your json name to be built: {jsonname}")
    json_path = os.path.join(dirname, jsonname)
    print("Writing to json ... ")
    with open(json_path, "a", encoding="utf-8") as json_file:
        json.dump(json_dict,
                  json_file,
                  indent=5)
        print()
        print("Successfully written into json file.")
