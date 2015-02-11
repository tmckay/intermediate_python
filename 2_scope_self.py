"""
You need to use self in methods!
"""

class Shrubbery(object):
    def say_ni(self):
        print 'ni'

    def what_do_the_knights_say(self):
        self.say_ni()
        # This doesn't work
        # say_ni()

sh = Shrubbery()
sh.what_do_the_knights_say()
