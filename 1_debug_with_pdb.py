"""
Debug a script using pdb
"""

def is_palindrome(s):
    s = s.replace(' ', '').lower()
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
