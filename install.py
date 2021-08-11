#!/usr/bin/python3
import os

def main():
    folder_dst = "/mnt/data/shares/data/gopro"

    # if destination folder doesn't exists create it
    if not os.path.exists(folder_dst):
        print("Create folder", folder_dst)
        os.makedirs(folder_dst, 0o775)
        os.chown(folder_dst, 1000, 1000) # Rudloff id and group Root
        os.chmod(folder_dst, 0o775) # Give all read access but Rudloff write access 


if __name__ == "__main__":
    # execute only if run as a script
    main()