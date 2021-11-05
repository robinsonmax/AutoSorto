import os
import datetime

print(
    "This program sorts a bunch of files into a YYYY/MM/[File] folder stucture")

while True:
    folder = input(
        "\nPlease paste the folder you want to organsie below.\nThis program will sort through all the loose files in that folder.\n> ")
    try:
        folder = folder.replace("\\", "/")
        files = os.listdir(folder)
        print("\n", len(files), "files detected")
        break
    except:
        os.system('cls')
        print("Path doesn't exist")


confirmation = input("\nStart organsiation? (Y/N)\n> ")

if(not(confirmation.lower() == "y" or confirmation.lower() == "yes")):
    print("closing ...")
    quit()


print("Starting...")

for index in range(len(files)):
    file = files[index]
    filePath = folder + "/" + file
    if(os.path.isdir(filePath)):
        continue
    print("Processing", file)
    fileDate = os.path.getmtime(filePath)
    fileYear = datetime.datetime.utcfromtimestamp(fileDate).strftime("%Y")
    fileMonth = datetime.datetime.utcfromtimestamp(fileDate).strftime("%m")
    newPath = folder + "/" + fileYear + "/" + fileMonth
    if not os.path.exists(newPath):
        os.makedirs(newPath)
    os.replace(filePath, newPath + "/" + file)

print("Done")
