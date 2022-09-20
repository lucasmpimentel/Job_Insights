from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, 'r') as file:
        jobs = csv.DictReader(file)
        return list(jobs)
