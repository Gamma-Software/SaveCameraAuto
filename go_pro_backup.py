#!/usr/bin/python3
import os
import shutil
from pathlib import Path
import requests

def telegram_bot_sendtext(bot_message):
    bot_token = os.getenv('BOT_TOKEN')
    bot_chatID = os.getenv('BOT_ID')
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def main():
    folder_src = "/run/user/1000/gvfs/mtp:host=GoPro_HERO8_BLACK_C3331350619413/GoPro MTP Client Disk Volume/DCIM"
    folder_dst = "/mnt/data/shares/data/gopro"

    # if Go Pro Not connected
    if not os.path.exists(folder_src):
        exit(0)

    # if destination folder doesn't exists create it
    if not os.path.exists(folder_dst):
        print("Folder doesn not exists, create it", folder_dst)
    
    files_in_gopro = list(Path(folder_src).rglob("*.[mM][pP]4"))
    files_backuped = list(Path(folder_dst).rglob("*.[mM][pP]4"))

    filename_in_gopro = [os.path.basename(filepath) for filepath in files_in_gopro]
    filename_backuped = [os.path.basename(filepath) for filepath in files_backuped]

    diff = set(filename_in_gopro) ^ set(filename_backuped)

    files_to_backup = []
    for file in diff:
        for file_in_gopro in files_in_gopro:
            if os.path.basename(file_in_gopro) in file:
                files_to_backup.append(file_in_gopro)
    
    if len(diff) > 0:
        print("Backup Go Pro")
        backuped = False
        for file in diff:
            for file_in_gopro in files_in_gopro:
                if os.path.basename(file_in_gopro) in file:
                    src = file_in_gopro
                    dst = os.path.join(folder_dst, os.path.basename(file_in_gopro))
                    print("Copy: ", src, " -> ", dst)
                    shutil.copyfile(src, dst)
                    backuped = True
        if backuped:
            telegram_bot_sendtext("Les nouvelles vidéo de la GoPro sont disponibles")
    else:
        telegram_bot_sendtext("La GoPro est branchée mais rien n'est à copier")
        print("No Go Pro files to backup")

if __name__ == "__main__":
    # execute only if run as a script
    main()