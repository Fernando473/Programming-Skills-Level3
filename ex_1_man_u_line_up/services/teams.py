from utils.read_json import read_file
from utils.mapper import Data

def get_teams(file_path) -> [Data]:
    try:
        results = []
        data = read_file(file_path)
        info = data.get("data")
        for i in range(len(info)):
            results.append(Data.from_dict(info[i]))
        return results[0],results[1]
    except Exception as e:
        print("Something went wrong " + str(e))