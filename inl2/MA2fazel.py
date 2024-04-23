"""
Solutions to module 2 - A calculator
Student: Fazel Naser
Mail: fazel.naser.9727@student.uu.se
Reviewed by: Tom
Reviewed date:
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

from MA2tokenizer import TokenizeWrapper
from tokenize import TokenError
import math


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


def fib(n: int):
    memory = {0: 0, 1: 1}

    def _fib(n: int):
        if n not in memory:
            memory[n] = _fib(n - 1) + _fib(n - 2)
        return memory[n]
    
    if (float(n) - int(n) != 0.0) or (int(n) < 0):
        raise EvaluationError(f"Argument to fib is {n}. Must be integer >= 0")
    else:
        return _fib(n)

def fact(n):
    if n.is_integer() and n >= 0:
        return math.factorial(int(n))
    else:
        raise EvaluationError("Wrong arg for fact")


variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
func_1 = {"sin": math.sin, "cos": math.cos, "exp": math.exp, "log": math.log, "fib": fib, "fac": fact}
func_n = {"min": min, "max": max, "sum": sum, "mean": lambda x: sum(x) / len(x)}


def statement(wtok, variables):
    """ See syntax chart for statement"""
    if wtok.is_at_end():
        pass
    else:
        result = assignment(wtok, variables)
        if not wtok.is_at_end():
            raise SyntaxError("Unexpected token")
    return result


def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_number():
            raise SyntaxError("Expected variable after '='")
        else:
            variables[wtok.get_current()] = result
            wtok.next()
    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while True:
        oper = wtok.get_current()
        if oper == '+':
            wtok.next()
            result = float(result) + float(term(wtok, variables))
        elif oper == '-':
            wtok.next()
            result = float(result) - float(term(wtok, variables))
        else:
            break
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while True:
        oper = wtok.get_current()
        if oper == '*':
            wtok.next()
            result = float(result) * float(factor(wtok, variables))
        elif oper == '/':
            wtok.next()
            x =  float(factor(wtok, variables))
            if x == 0:
                raise EvaluationError("*** Evaluation error: Division by zero")
            else:
                result = float(result) / x
        else:
            break
    return result


def factor(wtok, variables):
    """ See syntax chart for factor
        Follow the syntax chart as closely as possible!
        Check only for syntax error error - not for evaluation errors!
    """
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() == ')':
            wtok.next()
        else:
            raise SyntaxError("Expected ')'")

    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.get_current() in variables:
        result = variables[wtok.get_current()]
        wtok.next()

    elif wtok.is_name():
        result = wtok.get_current()
        wtok.next()
        if result in func_1:
            wtok.next()
            var = float(assignment(wtok, variables))
            if (result == "log") and (var <= 0):
                raise EvaluationError(f"Argument to {result} is {var}. Must be integer > 0")
            result = func_1[result](var)
            wtok.next()
        elif result in func_n:
            result = wtok.get_previous()
            var = arglist(wtok, variables)
            result = func_n[result](var)
        else:
            raise EvaluationError(f"Undefined variable: {wtok.get_current()}")
    elif wtok.get_current() == '-':
        wtok.next()
        result = -1 * float(factor(wtok, variables))
        
    else:
        raise SyntaxError("Expected number, name or '('")
    return result


def arglist(wtok, variables):
    """ 
        Handles functions that have multiple parameters
    """
    lst = []
    if wtok.get_current() != '(':
        raise SyntaxError("Expected '('")

    wtok.next()
    result = assignment(wtok, variables)
    lst.append(result)

    while True:
        if wtok.get_current() == ',':
            wtok.next()
            result = assignment(wtok, variables)
            if wtok.is_number():
                raise SyntaxError("Expected a number after ','")
            else:
                lst.append(result)
        elif wtok.get_current() == ')':
            wtok.next()
            break
        else:
            raise SyntaxError("Expected ',' or ')'")
    return lst


def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file.

    You need to add handling of EvaluationError in this function!
    """

    print("Numerical calculator")
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0] == '#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        elif wtok.get_current() == "vars":
            for key, val in variables.items():
                print(f"{key} : {val}")
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result

                if wtok.is_at_end():
                    print('Result:', result)
                else:
                    raise SyntaxError("Unexpected token")

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                    f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')

            except EvaluationError as ee:
                print("***Evaluation error: ", ee.arg)


if __name__ == "__main__":
    main()
