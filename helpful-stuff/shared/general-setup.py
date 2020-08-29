def main():
    import platform
    import os
    print("Setting up shortcuts")
    op = platform.system()

    if op == "Windows":
        os.system("doskey developer-search = python ../cmd-developer-search.py")
    elif op == "Linux" or op == "Darwin":
        """ Help wanted: Don't have / understand a Linux or MAC so someone has to fill this in """
        pass

main()

"""
---------------
Important Notes
---------------

This file is still in development stage

---------------

The shortcut keys are also dependent on this folder being whole so don't delete anything

This means you have to be in this folder for you to be able to run the shortcuts

---------------

"""
