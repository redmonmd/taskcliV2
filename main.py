#!/user/bin/bash python3.13
# Author: David Redmon
# Goal: This project is a learning idea based on roadmap.sh Task Tracker CLI project idea
#       Let me know if you see any improvements fit.

TASKLST = []
TASKDICT = {}

import cmd
import datetime
import os
import pickle
from dataclasses import dataclass

@dataclass
class Task:
    def __init__(self, task="default", description="default desc", tid=0, status="None", created=datetime.datetime.now(), last_updated=datetime.datetime.now()):
        self.task = task
        self.description = description
        self.tid = tid
        self.status = status
        self.created = created
        self.last_updated = last_updated

    def save_object(taskobjsave, tasklist=TASKLST):
        tasklist.append(taskobjsave)
        with open('./taskslist.pkl', 'wb') as outp:
            pickle.dump(tasklist, outp, pickle.HIGHEST_PROTOCOL)

    def show(self):
        print('\nTask: {}\n Description: {}\n Status: {}\n Created: {}\n Last Updated: {}\n'.format(self.task, self.description, self.status, self.created, self.last_updated))

def pickle_loader(filename):
    with open(filename, 'rb') as inp:
        while True:
            try:
                yield pickle.load(inp)
            except EOFError:
                break

class TaskCLI(cmd.Cmd):
    Intro = "Welcome to tasker, Type help or ? to list commands \n"
    prompt = "tasker-cli-> "

    def __init__(self):
        super().__init__()

    def do_test(self, line):
        """print line test"""
        print("TEST TEST TEST")

    def do_add(self, ntask=(input())):
        """add a task"""
        if ntask != "":
            ntask = Task()
        else:
            pass
        ntask.task = input("What is your task?\n")
        ntask.description = input("Enter a breif description of the task: ")
        ntask.status = "TODO"
        ntask.created = datetime.datetime.now()
        ntask.last_updated = datetime.datetime.now()
        ntask.tid = id(ntask.task)
        Task.save_object(ntask, TASKLST)

    def do_list(self, line):
        """list tasks"""
        for taskn in pickle_loader('./taskslist.pkl'):
            for n in taskn:
                print(n.show())

    def do_update(self, ):

if __name__ == '__main__':
    TaskCLI().cmdloop()