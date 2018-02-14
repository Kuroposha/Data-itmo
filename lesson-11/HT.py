from collections import namedtuple

def return_namedtuple(*pron):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if isinstance(result , tuple):
                klassnoe_name = namedtuple('ostroumnoe_name', list(pron))
                result = klassnoe_name(*result)

                return result(*result)
        return func(*args, **kwargs)
    return decorator

@return_namedtuple('one', 'two', 'three')
def func():
    return 1, 2, 3

r = func()
print(r.three) # 3
