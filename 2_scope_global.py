"""
This script demonstrates Python scope
"""

MODULE_GLOBAL = 'global'

def attempt_to_change_global():
    MODULE_GLOBAL = 'changed'
    print MODULE_GLOBAL

attempt_to_change_global()

print MODULE_GLOBAL

def really_change_global():
    global MODULE_GLOBAL
    MODULE_GLOBAL = 'changed'
    print MODULE_GLOBAL

really_change_global()

print MODULE_GLOBAL
