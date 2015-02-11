"""
Metaclasses make classes
"""

def do_screenshot(func):
    def _do_screenshot(*args, **kwargs):
        print 'Took a screenshot for {0}'.format(func.__name__)
        return func(*args, **kwargs)
    return _do_screenshot


class ScreenshotTestsMeta(type):
    
    def __init__(self, name, bases, attrs):
        for key, value in attrs.items():
            if key.startswith('test_'):
                if hasattr(value, '__call__'):
                    setattr(self, key, do_screenshot(value))
        type.__init__(self, name, bases, attrs)


class SuperTests(object):

    __metaclass__ = ScreenshotTestsMeta

    def test_search_box(self):
        print 'test_search_box' 

    def reload_page(self):
        print 'reload_page' 


if __name__ == '__main__':
    st = SuperTests()
    st.test_search_box()
    st.reload_page()
