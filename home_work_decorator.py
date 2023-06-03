def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) == str:
            result_end = f"<b> {result} <b>"
            return result_end
        return result

    return wrapper


@decorator
def check_integer(values):
    return values


print(check_integer("Big boy"))
