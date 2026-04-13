import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    data = {}

    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    if not os.path.join(cwd_path, file_name):
        return None
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    if field in data:
        return data
    return data[field]

def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

if __name__ == '__main__':
    main()