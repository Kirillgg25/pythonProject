a = input("Ведите свой пример ")

def checker(*exc_types):
    def checker(function):
        def checker(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
            except (exc_types) as exc:
                print(f"We have problems {exc}")
            else:
                print(f"No problems. Result – {result}")
        return checker
    return checker
@checker(NameError, TypeError, SyntaxError, ZeroDivisionError)
def calculate(expression):
    return eval(expression)
calculate(a)