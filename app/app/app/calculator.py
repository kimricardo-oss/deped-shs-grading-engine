from app.strategies import StandardDepEdStrategy

TRANSMUTATION_TABLE = [
    (0.0, 39.99, 60), (40.0, 42.99, 61), (43.0, 45.99, 62),
    (46.0, 47.99, 63), (48.0, 49.99, 64), (50.0, 51.99, 65),
    (52.0, 53.99, 66), (54.0, 55.99, 67), (56.0, 57.99, 68),
    (58.0, 59.99, 69), (60.0, 61.99, 70), (62.0, 63.99, 71),
    (64.0, 65.99, 72), (66.0, 67.99, 73), (68.0, 69.99, 74),
    (70.0, 72.99, 75), (73.0, 74.99, 76), (75.0, 75.99, 77),
    (76.0, 76.99, 78), (77.0, 77.99, 79), (78.0, 78.99, 80),
    (79.0, 79.99, 81), (80.0, 80.99, 82), (81.0, 81.99, 83),
    (82.0, 82.99, 84), (83.0, 83.99, 85), (84.0, 84.99, 86),
    (85.0, 85.99, 87), (86.0, 86.99, 88), (87.0, 87.99, 89),
    (88.0, 88.99, 90), (89.0, 89.99, 91), (90.0, 90.99, 92),
    (91.0, 91.99, 93), (92.0, 92.99, 94), (93.0, 93.99, 95),
    (94.0, 94.99, 96), (95.0, 95.99, 97), (96.0, 97.49, 98),
    (97.5, 99.49, 99), (99.5, 100.0, 100)
]

class SubjectGradeEngine:
    @staticmethod
    def transmute(initial_grade: float) -> int:
        if initial_grade >= 100.0: return 100
        if initial_grade <= 0.0: return 60
        for lower, upper, transmuted in TRANSMUTATION_TABLE:
            if lower <= initial_grade <= upper:
                return transmuted
        return int(round(initial_grade))

    @classmethod
    def calculate_single_subject(cls, category: str, ww_score: float, pt_score: float, qa_score: float) -> dict:
        strategy = StandardDepEdStrategy(category)
        initial = strategy.compute_initial_grade(ww_score, pt_score, qa_score)
        transmuted = cls.transmute(initial)
        return {
            "initial_grade": initial,
            "transmuted_grade": transmuted,
            "is_passing": transmuted >= 75
        }
