#!/user/bin/bash python3.13
# Author: David Redmon
# Goal: This project is a learning idea based on roadmap.sh Task Tracker CLI project idea
#       Let me know if you see any improvements fit.

import cmd

class Task:
    def __init__(self, task, description, tid, status, created, last_updated):
        self.task = task
        self.description = description
        self.tid = id(self)
        self.status = status
        self.created = created
        self.last_updated = last_updated

class TestCLI(cmd.Cmd):
    prompt = 'tasker-cli-> '
    Intro = 'Welcome to tasker, Type help or ? to list commands'

    def test(self):
        """print line test"""
        print("TEST TEST TEST")

    if __name__ == '__main__':
        TestCLI().cmdloop()