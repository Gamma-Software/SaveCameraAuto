#!/usr/bin/python3
import os
import filecmp
import shutil
from pathlib import Path

def main():
    folder_src = "/run/user/1000/gvfs/mtp:host=GoPro_HERO8_BLACK_C3331350619413/GoPro MTP Client Disk Volume/DCIM"
    folder_dst = "/mnt/data/shares/data/gopro"

    # if Go Pro Not connected
    if not os.path.exists(folder_src):
        exit(0)

    # if destination folder doesn't exists create it
    if not os.path.exists(folder_dst):
        print("Create folder", folder_dst)
        os.makedirs(folder_dst, 0o740)
        os.chown(folder_dst, 82, 82) # Rudloff id and group Root
        os.chmod(folder_dst, 0o774) # Give all read access but Rudloff write access 
    
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
        for file in diff:
            for file_in_gopro in files_in_gopro:
                if os.path.basename(file_in_gopro) in file:
                    src = file_in_gopro
                    dst = os.path.join(folder_dst, os.path.basename(file_in_gopro))
                    print("Copy: ", src, " -> ", dst)
                    shutil.copyfile(src, dst)
    else:
        print("No Go Pro files to backup")

    exit(0)
    if not os.path.exists(dst) and result:
        print("Backup go pro")
        shutil.copyfile(src, dst)

if __name__ == "__main__":
    # execute only if run as a script
    main()