import os
import sys
if (sys.platform == 'win32'):
    os.system('powershell Expand-Archive bike-sharing-dataset.zip')
    os.system('powershell Expand-Archive -Path bike-sharing-dataset/Bike-Sharing-Dataset.zip -DestinationPath ./data -force')
    print("Unzipping in Windows...")
else:
    os.system('unzip bike-sharing-dataset.zip')
    os.system('unzip bike-sharing-dataset/Bike-Sharing-Dataset.zip ./data')
    print("Unzipping in MacOS or Linux...")
os.system('rm bike-sharing-dataset.zip')
os.system('rm -rf bike-sharing-dataset')
print("Completed.")