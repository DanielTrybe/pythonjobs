from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, encoding='utf-8') as file:
        dicionario = []
        result = csv.DictReader(file, delimiter=',', quotechar='"')
        for item in result:
            dicionario.append(item)
        return dicionario
