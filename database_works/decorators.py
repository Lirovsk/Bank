from functools import wraps

def cancel_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if func(*args, **kwargs) == "cancel":
            raise Exception("Input cancelled by user.")
        else:
            return func(*args, **kwargs)
    return wrapper