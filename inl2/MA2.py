"""
Solutions to module 2 - A calculator
Student: 
Reviewed by:
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
import math
from tokenize import TokenError

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

func_1 = {"sin": math.sin, "cos": math.cos, "exp": math.exp, "log": math.log, "fib": fib, "fac": fact}
func_n = {"min": min, "max": max, "sum": sum, "mean": lambda x: sum(x) / len(x)}


def statement(wtok, variables):
    # kollar om vi är vid slutet av
    # om inte kör vi assignment
    # är vi inte i slutet har vi ett error efter assigmnet
    """ See syntax chart for statement"""
    if wtok.is_at_end():
        pass
    else:
        result = assignment(wtok, variables)
        if not wtok.is_at_end():
            raise SyntaxError("Unexpected tokem")
    return result 


def assignment(wtok, variables):
    # kallar expression om den kommer till ett = skapar vi en varibel
    # givet att det är ett korrekt variabelnamn som anges
    # antaget att när variabel deklareras bör namnet vara sista som anges
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)
    while wtok.get_current() == "=":
        wtok.next()
        if wtok.is_number():
            raise SyntaxError("Expected variable after '='")
        else:
            variables[wtok.get_current()] = result
            wtok.next()
    return result


def expression(wtok, variables):
    # kör först igenom alla multiplikationer
    # därefter kor vi igenom 
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
    # här går vi igenom multiplikationer
    # factor bör returnera en operator och vi multiplicerar den med en till factor
    # vi forstätter att multiplicera såvida factor ger * eller /
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while True:
        op = wtok.get_current()
        if op == "*":
            wtok.next()
            result = float(result) * float(factor(wtok, variables))
        elif op == "/":
            wtok.next()
            denominator = float(factor(wtok, variables))
            if denominator == 0: 
                raise EvaluationError("Evaluation error: division by zero")
            else:
                result = float(result)/denominator
        else:
            break
        
    return result


def factor(wtok, variables):
    # factor kollar om vi har en parantes
    # har vi den kör vi om hela proceduren igenom hlea parantesen
    # kollar öven om vi har ett nummer, då skippar den till nästa som resterande funktioner kan ta nytta av
    # kollar också om vi har några inbyggda funktioner att kalla på
    """ See syntax chart for factor
        Follow the syntax chart as closely as possible!
        Check only for syntax error error - not for evaluation errors!
    """
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()

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
            if result == "log" and var <= 0:
                raise EvaluationError("Error: log(x) defined for x>0")
            result = func_1[result](var)
            wtok.next()
        elif result in func_n:
            result = wtok.get_previous()
            var = mult_args(wtok, variables)
            result = func_n[result](var)
        else:
            raise EvaluationError("Undifined variable:"+ str(wtok.get_current()))
    elif wtok.get_current() == "-":
        wtok.next()
        result = -1 * float(factor(wtok, variables))
    
    else:
        raise SyntaxError(
            "Expected number or '('")
    return result
def mult_args(wtok, variables):
    rey = []
    if wtok.get_current() != "(":
        raise SyntaxError("Expected '('")
    wtok.next()
    result = assignment(wtok, variables)
    rey.append(result)
    while True:
        if wtok.get_current() == ",":
            wtok.next()
            result = assignment(wtok, variables)
        elif wtok.get_current()==")":    
            wtok.next()
            break
    return rey
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
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    
    init_file = 'inl2/MA2init.txt'
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
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                    f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')
                
            except EvaluationError as ee:
                print("*** Evaluation error: ", ee.arg)


if __name__ == "__main__":
    main()
