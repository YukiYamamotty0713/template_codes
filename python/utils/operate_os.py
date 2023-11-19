import os

def get_filepath(folder_path,extension):
#================================================================
#フォルダパスを入力し、条件(extension)に合ったファイルパスを取得する。
#================================================================
    file_paths = []
    try:
        for file_name in os.listdir(folder_path):
            if file_name.endswith(extension):
                file_path = os.path.join(folder_path, file_name)
                file_paths.append(file_path)
    except OSError as e:
        print(f"Error reading files in {folder_path}: {e}")
    return file_paths