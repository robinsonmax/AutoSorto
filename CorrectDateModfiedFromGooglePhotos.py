import os
import time
import datetime
import json


def correctModifiedTime(file):
    try:
        jsonFile = open(file + ".json", "r")
        jsonData = json.load(jsonFile)
        jsonFile.close()
        timeStamp = jsonData["photoTakenTime"]["timestamp"]
        date = datetime.datetime.fromtimestamp(int(timeStamp))
    except:
        print("Error getting time stamp from JSON for file:", file)
        return False

    try:
        modTime = time.mktime(date.timetuple())
        os.utime(file, (modTime, modTime))
        print(date, "Updated modified date of file:", file)
        return True
    except:
        print("Error updating date modified of file:", file)
        return False


print(
    "This program updates the Date Modified of a bunch of files exported from Google Photos.")

while True:
    folder = input(
        "\nPlease paste the folder you want to organsie below.\nThis program will sort through all the loose files in that folder, using the photoTakenTime from the JSON file associated with it.\n> ")
    try:
        folder = folder.replace("\\", "/")
        files = os.listdir(folder)
        print("\n", len(files), "files detected")
        break
    except:
        os.system('cls')
        print("Path doesn't exist")


confirmation = input("\nStart update? (Y/N)\n> ")

if(not(confirmation.lower() == "y" or confirmation.lower() == "yes")):
    print("closing ...")
    quit()


print("Starting...")

numberOfFiles = len(files)
for index in range(numberOfFiles):
    file = files[index]
    filePath = folder + "/" + file
    if(os.path.isdir(filePath) or filePath.split(".")[-1].lower() == "json"):
        continue
    print("Processing", index, "/", numberOfFiles, file)
    correctModifiedTime(filePath)

print("Done")
