import json

def read_file(path_file):
    try:
        with open(path_file, 'r', encoding='utf-8') as file:
            datos = json.load(file)
            return datos
    except Exception as e:
        print(f"Something went wrong durind reading {path_file} file : {str(e)}")