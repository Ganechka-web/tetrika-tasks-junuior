import pytest

from task_3.solution import appearance


@pytest.mark.parametrize(
    ['intervals', 'expectation'],
    [
        ({
            'lesson': [0, 6],
            'pupil': [0, 4, 3, 6],
            'tutor': [-1, 3, 4, 5]
        }, 4),
        ({
            'lesson': [0, 6],
            'pupil': [-3, 0, -2, 0],
            'tutor': [0, 4, 2, 5]
        }, 0),
        # test mutual interruption
        ({
            'lesson': [0, 10],
            'pupil': [0, 3, 1, 2, 5, 9, 6, 10, 10, 20],
            'tutor': [-2, 4, 5, 7, 6, 10],
        }, 8)
    ]
)
def test_appearance(intervals, expectation):
    assert appearance(intervals) == expectation
