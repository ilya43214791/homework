def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) == str:
            result_end = f"<b> {result} <b>"
            return result_end
        else:
            mistake = "Enter words"
            return mistake

    return wrapper


@decorator
def check_intenger(values):
    return values


print(check_intenger("Big boy"))
