import os

def file_editor():
    file_name = os.environ.get("INPUT_FILE_NAME")
    type = os.environ.get("INPUT_TYPE")
    if type == 'sort':
        update_file_content_sort(file_name)
    print("update file content sort success!")

def update_file_content_sort(file_name):
    f = open(file_name, 'r', encoding='utf-8')
    name_array = f.read().split(',')
    name_array.insert(len(name_array), name_array.pop(0))
    write_txt = ','.join(name_array)
    f = open(file_name, 'w', encoding='utf-8')
    f.write(write_txt)
    f.close

if __name__ == "__main__":
    file_editor()