from functools import wraps
import datetime


def logger(f):
    @wraps(f)
    def logging(*args, **kwargs):
        with open(f'{datetime.date.today()}.log', 'a') as file:
            file.write(f'{str(f(*args, **kwargs))}\n')
        return f(*args, **kwargs)
    return logging
