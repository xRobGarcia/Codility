import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "Lesson 12 Euclidean algorithm" / "CommonPrimeDrivisors.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("common_prime_drivisors", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


mod = _load_module()
\

class TestCommonPrimeDivisors(unittest.TestCase):
    def test_prompt_example(self):
        A = [15, 10, 3]
        B = [75, 30, 5]
        self.assertEqual(mod.solution(A, B), 1)

    def test_same_prime_sets_with_different_powers(self):
        A = [2, 12, 15]
        B = [4, 18, 75]
        self.assertEqual(mod.solution(A, B), 3)

    def test_pairs_with_extra_prime_factor(self):
        A = [10, 9, 14]
        B = [30, 5, 28]
        self.assertEqual(mod.solution(A, B), 1)

    def test_edge_cases(self):
        cases = [
            ([1], [1], 1),
            ([2], [4], 1),
            ([2], [3], 0),
            ([12], [18], 1),
            ([12], [20], 0),
        ]

        for A, B, expected in cases:
            with self.subTest(A=A, B=B):
                self.assertEqual(mod.solution(A, B), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)