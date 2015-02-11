class CaseInsensitiveStrs(object):

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value.lower() == other.value.lower()

if __name__ == '__main__':
    a = CaseInsensitiveStrs('APPLE')
    b = CaseInsensitiveStrs('aPpLe')

    assert a == b
    assert not 'APPLE' == 'aPpLe'
