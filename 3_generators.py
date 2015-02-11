"""
Generators store state between calls
"""

def range_generator(to):
    ii = 0
    while ii < to:
        yield ii
        ii+=1

for xx in range_generator(5):
    print xx
