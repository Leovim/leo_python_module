def print_args(function):
    def wrapper(*args, **kwargs):
        code = function.func_code
        for arg, value in zip(code.co_varnames, args):
            print i + ': ' + j
        return function(*args, **kwargs)
    return wrapper
