"""
Decorators can wrap functions
"""

def log_function(func):

    def wrapped(*args, **kwargs):
        print 'LOG: Called "{0}"'.format(func.__name__)
        return func(*args, **kwargs)
    return wrapped

@log_function
def spam():
    print 'Sending spam and eggs'

if __name__ == '__main__':
    spam()
