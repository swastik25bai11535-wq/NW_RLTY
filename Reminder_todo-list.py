class password_check:
    """
    Manages password authentication for user login.

    Attributes:
        password (str): The correct password set during initialization.
        unlocked (bool): Indicates whether authentication was successful.
    """
    def __init__(self, password):
        self.password = password
        self.unlocked = False
    
    def enter_password(self, PASSWORD):
        if PASSWORD == self.password:
            self.unlocked = True
    def final(self):#final step
        if self.unlocked == True:
            print("You are logged in ")
            return True
        else:
            print("enter the correct password")
            return False

import datetime

class reminder:
    """
    Handles time-based reminders for morning, afternoon, and evening tasks.

    Attributes:
        morning_reminder (str): Reminder message for morning.
        afternoon_reminder (str): Reminder message for afternoon.
        evening_reminder (str): Reminder message for evening.
    """

    def __init__(self,morning_reminder , afternoon_reminder, evening_reminder ):
        self.morning_reminder = morning_reminder
        self.afternoon_reminder = afternoon_reminder
        self.evening_reminder = evening_reminder
    def notification(self ):
        current_time =  datetime.datetime.now()
        b = datetime.time( 6,0,0)
        c = datetime.time( 12,0,0)
        d = datetime.time( 18,0,0)
        if current_time.time() == b:
            print("!!!!!! TIME FOR ", self.morning_reminder)
        if current_time.time() == c:
            print("!!!!!! TIME FOR ", self.afternoon_reminder)
        if current_time.time() == d:
            print("!!!!!! TIME FOR ", self.evening_reminder)
        else :
            print("no reminder right now")

class todo_list:
    """
    Manages a to-do list with task completion tracking and status display.

    Attributes:
        task1, task2, task3, task4 (str): Four initial tasks.
        completed_task (list): List of completed tasks.
        remaining_task (list): List of remaining tasks.
        completed (bool): Indicates if all tasks are completed.
    """
    def __init__(self,task1, task2, task3, task4):
        self.task1 = task1
        self.task2 = task2
        self.task3 = task3
        self.task4 = task4
        self.completed_task = []
        self.remaining_task = [task1, task2, task3, task4]
        self.completed = False
    def update(self,a):
        if a == self.task1:
            self.completed_task.append(a)
            self.remaining_task.remove(a)
        if a == self.task2:
            self.completed_task.append(a)
            self.remaining_task.remove(a)
        if a == self.task3:
            self.completed_task.append(a)
            self.remaining_task.remove(a)
        if a == self.task4:
            self.completed_task.append(a)
            self.remaining_task.remove(a)
        if self.remaining_task == []:
            self.completed = True
    def praise(self):
        print("WOW!!!!!   You've completed your tasks")
    def display_completed_tasks(self):
        return self.completed_task
    def display_remaining_tasks(self):
        return self.remaining_task

def unlock():
    
    a = password_check("Vityarthi")
    a.enter_password(input("enter password : "))
    final = a.final()
    if final == True:
        b = reminder("Breakfast", "Driving Practice", "study")
        b.notification()
    if final == False:
            unlock()
def manage_task():
    c = todo_list("Data structures", "Algorithm", "Vityarthi project", "meditation")   
    c.update(input("update : "))
    c.update(input("update : "))
    print("the completed tasks are : " ,c.display_completed_tasks())
    print("the remaining tasks are : ", c.display_remaining_tasks())
    c.update(input("update : "))
    print("the completed tasks are : " ,c.display_completed_tasks())
    print("the remaining tasks are : ",c.display_remaining_tasks())
    c.update(input("update : "))
    c.praise()# A little praise will boost the confidence

unlock()

manage_task()  
    
