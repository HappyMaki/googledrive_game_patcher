from GDrive import DriveUtil
from file_utils import unzip_file
from updater import download_latest_version
import os
gDrive = DriveUtil()
gDrive.upload_to_drive()
gDrive.share_file_to_public()

file_id = gDrive.remote_file_info["id"]
destination = './temporary.zip'
gDrive.download_file_from_google_drive(file_id, destination)

unzip_file("./temporary.zip", "./Game_Files", deleteZip=False)




while True:
    try:
        os.chdir('./patcher')
        print(os.getcwd())
        download_latest_version()
        restart = input('\nFinished; run again? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    except FileNotFoundError:
        print(os.getcwd())
        download_latest_version()
        restart = input('\nFinished; run again? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

#TODO: Jake Topics
#TODO: Docker



#Use credentials through credentials txt
#make a json file in config for refresh token and credentials
#download unityhub and unity

#detail how to get refresh token/create credentials

