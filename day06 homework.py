def start_end(f):
    def decorator(*args):
        print('start')
        result=f(*args)
        print(result)
        return('end')
    return decorator

def sum(a,b):
    return (a+b)

print(start_end(sum)(1,2))



