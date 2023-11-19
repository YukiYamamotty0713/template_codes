import csv

# CSVファイルのパス
csv_file_path = 'example.csv'

def read_csv_as_2d_array(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        # 二次元配列としてデータを返す
        return [row for row in csv_reader]
'''
two_dimensional_array = read_csv_as_2d_array(csv_file_path)
print(two_dimensional_array)
'''

def read_csv_as_dict_list(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        # 辞書型リストとしてデータを返す
        return [row for row in csv_reader]
'''
dictionary_list = read_csv_as_dict_list(csv_file_path)
print(dictionary_list[1]['Name'])
'''