from src.counter import count_ocurrences


def test_counter():
    path = 'src/jobs.csv'
    word = 'python'
    result = 1639
    assert count_ocurrences(path, word) == result