from src.sorting import sort_by
import pytest


jobs_list = [
    {"date_posted": "2020-01-01", "max_salary": 6000, "min_salary": 2000},
    {"date_posted": "2021-01-01", "max_salary": 5000, "min_salary": 1000},
    {"date_posted": "2019-01-01", "max_salary": 7000, "min_salary": 3000},
]

min = [
    jobs_list[1],
    jobs_list[0],
    jobs_list[2],
]

max = [
    jobs_list[2],
    jobs_list[0],
    jobs_list[1],
]

date = [
    jobs_list[1],
    jobs_list[0],
    jobs_list[2],
]


sort_by(
    [
        {"date_posted": "2021-01-01", "max_salary": 5000, "min_salary": 1000},
        {"date_posted": "2020-01-01", "max_salary": 6000, "min_salary": 2000},
        {"date_posted": "2019-01-01", "max_salary": 7000, "min_salary": 3000},
    ],
    "date_posted",
)


def test_sort_by_criteria():
    sort_by(jobs_list, "min_salary")
    assert jobs_list == min

    sort_by(jobs_list, "max_salary")
    assert jobs_list == max

    sort_by(jobs_list, "date_posted")
    assert jobs_list == date

    with pytest.raises(
        TypeError, match="missing 1 required positional argument: 'criteria'"
    ):
        sort_by(jobs_list)


# agradecimentos ao pedro henrique.

