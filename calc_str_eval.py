import sys
from typing import NoReturn, Union


def readline() -> str:
    """
    Returns a stripped input.
    """
    input_line: str = sys.stdin.readline()
    return input_line.rstrip()


def parse_multi_or_div(equation: str) -> Union[int, float]:
    return int(equation)


def parse_add_or_minus(equation: str) -> Union[int, float]:
    plus_index = equation.find("+")
    minus_index = equation.find("-")

    if plus_index == -1 and minus_index == -1:
        return parse_multi_or_div(equation)
    elif plus_index == -1:
        return parse_multi_or_div(equation[:minus_index]) - parse_add_or_minus(equation[minus_index + 1:])
    elif minus_index == -1:
        return parse_multi_or_div(equation[:plus_index]) + parse_add_or_minus(equation[plus_index + 1:])
    else:
        if -1 < plus_index and plus_index < minus_index :
            return parse_multi_or_div(equation[:plus_index]) + parse_add_or_minus(equation[plus_index + 1:])
        elif -1 < minus_index and minus_index < plus_index :
            return parse_multi_or_div(equation[:minus_index]) - parse_add_or_minus(equation[minus_index + 1:])


def main() -> NoReturn:
    equation: str = ""
    while True:
        input_line: str = readline()

        if input_line == "quit":
            exit(0)
        elif "=" not in input_line:
            equation += input_line
            continue
        else:
            equation_end_index = input_line.find("=")
            equation += input_line[:equation_end_index]
            print(parse_add_or_minus(equation))
            equation = input_line[equation_end_index + 1:]


if __name__ == "__main__":
    main()
