import os


def get_folder_size(folder_path="."):
    """获取文件夹下所有文件的大小, 单位为MB"""
    size = 0
    Folderpath = folder_path
    for path, dirs, files in os.walk(Folderpath):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)
    return round(size / 1024 / 1024, 2)
