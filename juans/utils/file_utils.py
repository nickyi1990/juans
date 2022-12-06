import os


def get_folder_size(folder_path="."):

    size = 0
    Folderpath = folder_path
    for path, dirs, files in os.walk(Folderpath):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)
    print(f"Folder size: {int(size/1024/1024)} MB")
