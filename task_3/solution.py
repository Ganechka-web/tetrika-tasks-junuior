def appearance(intervals: dict[str, list[int]]) -> int:
    """Returns total being seconds on the lesson by intervals"""
    def concat_intervals_by_lesson(
            intervals: list[int], lesson: list[int, int]
    ) -> list[int]:
        """Returns concated intervals according to the lesson"""
        for i in range(0, len(intervals), 2):
            if intervals[i] < lesson[0]:
                intervals[i] = lesson[0]
            if intervals[i] > lesson[1]:
                intervals[i] = lesson[1]

            if intervals[i + 1] > lesson[1]:
                intervals[i + 1] = lesson[1]
            if intervals[i + 1] < lesson[0]:
                intervals[i + 1] = lesson[0]

        return intervals
    
    def merge_overlapping_intervals(intervals: list[int]) -> list[int]:
        """Returns merged intervals, exclude interruptions"""
        pairs_intervals: list[tuple[int, int]] = [
            (intervals[i], intervals[i + 1]) 
            for i in range(0, len(intervals), 2)
        ]
        
        merged_intervals = [pairs_intervals[0]]
        for i in range(1, len(pairs_intervals)):
            if merged_intervals[-1][1] > pairs_intervals[i][0]:
                merged_intervals[-1] = (merged_intervals[-1][0],
                                        max(pairs_intervals[i][1], merged_intervals[-1][1]))
            else:
                merged_intervals.append(pairs_intervals[i])
        return [
            i for pair in merged_intervals for i in pair 
        ]

    total_being_seconds = 0

    # check if at least one interval is empty
    if not all((intervals['lesson'], intervals['pupil'], intervals['tutor'])):
        return total_being_seconds

    # merging and concating intervals
    pupil_intervals = concat_intervals_by_lesson(
        merge_overlapping_intervals(intervals['pupil']), 
        intervals['lesson']
    )
    tutor_intervals = concat_intervals_by_lesson(
        merge_overlapping_intervals(intervals['tutor']), 
        intervals['lesson']
    )
    for i in range(0, len(pupil_intervals), 2):
        a, b = pupil_intervals[i], pupil_intervals[i + 1]
        for j in range(0, len(tutor_intervals), 2):
            c, d = tutor_intervals[j], tutor_intervals[j + 1]

            # pupil a|----+++++|b
            # tutor     c|+++++----|d
            if a < c and b > c and d > b:
                total_being_seconds += b - c
                continue

            # pupil     a|+++-----|b
            # tutor c|---+++|d
            if a > c and a < d and b > d:
                total_being_seconds += d - a
                continue

            # pupil a|---++++++---|b
            # tutor    c|+++++|d
            if a <= c and b >= d:
                total_being_seconds += d - c
                continue

            # pupil    a|++++|b
            # tutor c|--+++++---|d   
            if a >= c and b <= d:
                total_being_seconds += b - a
                continue

    return total_being_seconds
    

tests = [
    {
        'intervals': {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
            'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
        },
        'answer': 3117
    },
    {
        'intervals': {
            'lesson': [1594702800, 1594706400],
            'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
            'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
        },
        'answer': 3577
    },
    {   
        'intervals': {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692033, 1594696347],
            'tutor': [1594692017, 1594692066, 1594692068, 1594696341]
        },
        'answer': 3565
    },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
