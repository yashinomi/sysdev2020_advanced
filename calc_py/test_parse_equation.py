import unittest
from calc_str_eval import parse_add_or_minus, parse_multi_or_div


class TestEquationParse(unittest.TestCase):
    def test_additive(self):
        correct: int = 1
        equation: str = "0+1"
        result = parse_add_or_minus(equation)
        self.assertEqual(correct, result)

        correct: int = 5
        equation: str = "2+3"
        result = parse_add_or_minus(equation)
        self.assertEqual(correct, result)

    def test_substractive(self):
        correct: int = -1
        equation: str = "0-1"
        result = parse_add_or_minus(equation)
        self.assertEqual(correct, result)

        correct: int = 1
        equation: str = "2-1"
        result = parse_add_or_minus(equation)
        self.assertEqual(correct, result)

    def test_mult(self):
        correct: int = 0
        equation: str = "0*1"
        result = parse_multi_or_div(equation)
        self.assertEqual(correct, result)

        correct: int = 2
        equation: str = "2*1"
        result = parse_multi_or_div(equation)
        self.assertEqual(correct, result)


def main():
    try:
        correct: int = 3
        equation: str = "0+1*3"
        result = parse_add_or_minus(equation)
        assert correct == result, f"want {correct}, got {result}"

        correct: int = -1
        equation: str = "0*3-1"
        result = parse_add_or_minus(equation)
        assert correct == result, f"want {correct}, got {result}"

        correct: int = 0
        equation: str = "2/2-1"
        result = parse_add_or_minus(equation)
        assert correct == result, f"want {correct}, got {result}"

        correct: int = 5
        equation: str = "2+3+1-2/2"
        result = parse_add_or_minus(equation)
        assert correct == result, f"want {correct}, got {result}"
    
    except AssertionError as err:
        print("AssertionError :", err)


if __name__ == "__main__":
    main()
