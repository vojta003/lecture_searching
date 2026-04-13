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
    if not field in data:
        return None
    return data[field]

def linear_search(sekvence, cislo):
    result = {}
    count = 0
    for i, sek in enumerate(sekvence):
        if sek == cislo:
            count += 1
            result["pozice"] = i
            result["vyskyt"] = count
    return result

def binary_search(seznam, shoda):

    start = 0
    konec = len(seznam) - 1

    while start <= konec:
        stretnutí = (start + konec) // 2

        if seznam[stretnutí] == shoda:
            return stretnutí
        elif seznam[stretnutí] < shoda:
            start = stretnutí + 1
        else:
            konec = stretnutí - 1
    return None


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    sequential_data_2 = read_data("sequential.json", "ordered_numbers")
    print(f"Data pro lineár: {sequential_data}")
    print(f"Data pro binár: {sequential_data_2}")

    vysledek = linear_search(sequential_data,9)
    print(f"Výsledný slovník po lineáru {vysledek}")
    pozice = binary_search(sequential_data_2, 22)
    print(f"Pozice hledaného čísla v bináru je {pozice}")

if __name__ == '__main__':
    main()