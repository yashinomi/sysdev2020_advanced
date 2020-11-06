from calc_str_eval import parse_add_or_minus


def main():
    try:
        correct: int = 1
        equation: str = "0+1"
        result = parse_add_or_minus(equation)
        assert correct == result, f"want {correct}, got {result}"

        correct: int = -1
        equation: str = "0-1"
        result = parse_add_or_minus(equation)
        assert correct == result, f"want {correct}, got {result}"

        correct: int = 1
        equation: str = "2-1"
        result = parse_add_or_minus(equation)
        assert correct == result, f"want {correct}, got {result}"

        correct: int = 5
        equation: str = "2+3"
        result = parse_add_or_minus(equation)
        assert correct == result, f"want {correct}, got {result}"
    
    except AssertionError as err:
        print("AssertionError :", err)


if __name__ == "__main__":
    main()
