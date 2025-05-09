#!/user/bin/bash python3.13
# Author: David Redmon
# Goal: This project is a learning idea based on roadmap.sh Task Tracker CLI project idea
#       Let me know if you see any improvements fit.

TOSAVE = dict()

# TODO
# - [ ] REDO SAVES
# - [ ] map out dataflow
# - [ ] TBD
import cmd
import datetime
import os
import pickle
from dataclasses import dataclass
from unittest import case


@dataclass
class Task:
    def __init__(self, task="default", description="default desc", tid=0, status="None", created=datetime.datetime.now(), last_updated=datetime.datetime.now()):
        self.task = task
        self.description = description
        self.tid = tid
        self.status = status
        self.created = created
        self.last_updated = last_updated

    def save_object(self):
        taskdict = {'task': self.task, 'description': self.description, 'tid': self.tid, 'status': self.status, 'created': self.created, 'last_updated': self.last_updated}
        TOSAVE[self.task] = taskdict
#        with open('./taskslist.pkl', 'wb') as outp:
#            pickle.dump(taskref, outp)

def pickle_loader(filename):
    with open(filename, 'rb') as inp:
        while True:
            try:
                yield pickle.load(inp)
            except EOFError:
                break

def resave_object(savedict: dict=TOSAVE, taskref: dict=TOSAVE.keys(), key: str=TOSAVE.keys(), updated_val: str=TOSAVE.values()) -> None:
    """

    :type key: str
    """
    savedict[taskref].update({key: updated_val})
    return None



class TaskCLI(cmd.Cmd):
    Intro = "Welcome to tasker, Type help or ? to list commands \n"
    prompt = "tasker-cli-> "

    def __init__(self):
        super().__init__()

    def do_test(self, line):
        """print line test"""
        print("TEST TEST TEST")

    def do_add(self, line):
        """add a task"""
        ntask = Task()
        ntask.task = input("What is your task: ")
        ntask.description = input("Enter a breif description of the task: ")
        ntask.status = "TODO"
        ntask.created = datetime.datetime.now()
        ntask.last_updated = datetime.datetime.now()
        ntask.tid = id(ntask.task)
        ntask.save_object()

    def do_list(self, line):
        """list tasks"""
        # for entry in pickle_loader('./taskslist.pkl'):
        for taskitem in TOSAVE.values():
            print('Task: {}\n\tDescription: {}\n\tStatus: {}\n\tCreated: {}\n\tLast Updated: {}'.format(taskitem.get('task'), taskitem.get('description'), taskitem.get('status'), taskitem.get('created'), taskitem.get('last_updated')))


    def do_update(self, args):
        """update a task"""
        for entry in pickle_loader('./taskslist.pkl'):
            try:
                if args == entry.keys():
                    tmpupdatedict = entry.copy()
            except:
                return print("Not a task, try again")
                pass
        updatecmd = input("{}\n\t 1. In Progress \n\t 2. Finished \n\t 3. Delete\n".format(args))
        match updatecmd:
            case "1":
                resave_object(taskref=args, key="status", updated_val="In Progress")
            case "2":
                 resave_object(taskref=args, key="status", updated_val="In Progress")
            case "3":
                 TOSAVE.pop(args)
            case _:
                 print("not an option")

if __name__ == '__main__':
    TaskCLI().cmdloop()