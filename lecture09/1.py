from datetime import datetime


def timer1(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result

    return wrapper


@timer1
def any_function():
    # очень интересная функция
    return


any_function()
