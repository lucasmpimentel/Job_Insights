from src.jobs import read


def get_unique_job_types(path):
    job_types = set()
    jobs = read(path)
    for job in jobs:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    result = list()
    for job in jobs:
        if job["job_type"] == job_type:
            result.append(job)
    return result


def get_unique_industries(path):
    industries = set()
    jobs = read(path)
    for job in jobs:
        if job["industry"] != '':
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    result = list()
    for job in jobs:
        if job["industry"] == industry:
            result.append(job)
    return result


def get_max_salary(path):
    max_salary = 0
    result = 0
    jobs = read(path)
    for job in jobs:
        try:
            max_salary = int(job["max_salary"])
        except ValueError:
            print("Valor inválido")
            pass
        if max_salary > result:
            result = max_salary
    return result


def get_min_salary(path):
    result = get_max_salary(path)
    min_salary = 0
    jobs = read(path)
    for job in jobs:
        try:
            min_salary = int(job["min_salary"])
        except ValueError:
            print("Valor inválido")
        if 0 < min_salary < result:
            result = min_salary
    return result


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Dados Inválidos")
    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError("min_salary e max_salary precisam ser inteiros")
    if type(salary) != int:
        raise ValueError("salary precisa ser inteiro")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary não pode ser maior que max_salary")
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    result = list()
    for job in jobs:
        if (
            type(job["min_salary"]) == int
            and type(job["max_salary"]) == int
            and type(salary) == int
            and job["min_salary"] < job["max_salary"]
        ):
            if(matches_salary_range(job, salary)):
                result.append(job)
    return result
