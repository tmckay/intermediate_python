"""
Debug this script using pdb (Python DeBugger) 

Create a breakpoint by doing:

    import pdb; pdb.set_trace()

Once in the debugger, press "n" to go to the next line.
Press "s" to step into a function and press "c" to continue
to the next breakpoint.
"""

def is_palindrome(s):
    l = len(s)
    for i in range(l/2):
        if s[i] != s[l-1-i]:
            return False
    return True

def main():
    cases = [
                'a man a plan a canal panama',
                'zillow',
                'never odd or even',
            ]

    for case in cases:
        print '{0}: {1}'.format(case, is_palindrome(case))

if __name__ == '__main__':
    main()
