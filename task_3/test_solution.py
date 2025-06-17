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
        }, 8),
        # empty lesson intervals
        ({
            'lesson': [],
            'pupil': [90, 100, 140, 200],
            'tutor': [100, 120, 130, 140]
        }, 0),
        # empty pupil intervals
        ({
            'lesson': [100, 200],
            'pupil': [],
            'tutor': [100, 120, 130, 140]
        }, 0),
        # empty tutor intervals
        ({
            'lesson': [100, 200],
            'pupil': [90, 100, 140, 200],
            'tutor': []
        }, 0),
        # empty all intervals
        ({
            'lesson': [],
            'pupil': [],
            'tutor': []
        }, 0),
        ({
            'lesson': [100, 200],
            'pupil': [90, 110, 150, 210],
            'tutor': [95, 105, 180, 220] 
        }, 25),
        ({
            'lesson': [100, 200],
            'pupil': [120, 130, 140, 150], 
            'tutor': [110, 160]   
        }, 20),
        ({
            'lesson': [100, 200],
            'pupil': [110, 120, 130, 140, 150, 160],
            'tutor': [115, 125, 135, 145, 155, 165]  
        }, 15),
        ({
            'lesson': [100, 200],
            'pupil': [90, 210],
            'tutor': [90, 210]  
        }, 100),
        ({
            'lesson': [100, 200],
            'pupil': [110, 120],
            'tutor': [130, 140] 
        }, 0),
        ({
            'lesson': [100, 200],
            'pupil': [110, 120, 130, 140, 150, 160, 170, 180],
            'tutor': [105, 205]
        }, 40),
        ({
            'lesson': [100, 200],
            'pupil': [110, 120, 115, 125], 
            'tutor': [105, 130]            
        }, 15),
        ({
            'lesson': [100, 200],
            'pupil': [110, 120, 130, 140, 150, 160],
            'tutor': [105, 115, 125, 135, 145, 155] 
        }, 15),
        ({
            'lesson': [100, 200],
            'pupil': [110, 120, 130, 140, 150, 160], 
            'tutor': [120, 130, 140, 150, 160, 170] 
        }, 0),
        ({
            'lesson': [100, 200],
            'pupil': [110, 120, 130, 140, 150, 160],
            'tutor': [110, 120, 130, 140, 150, 160]
        }, 30),
        ({
            'lesson': [100, 200],
            'pupil': [110, 120, 130, 140, 150, 160],
            'tutor': [120, 130, 140, 150, 160, 170] 
        }, 0)
    ]
)
def test_appearance(intervals, expectation):
    assert appearance(intervals) == expectation
