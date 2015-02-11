"""
Notice that iteration variables persist outside scope of loops.
"""

ii = 0
for ii in range(10):
    pass

print ii
