# This is similar example ase miltithreading_I,
# But in this case we create class and then through the class we pass the params

# Importing necessary libraries
import threading
import time

# Creating the class
class myThread(threading.Thread):
    # Defining class constructor
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    # defining function run
    def run(self):
        print("Starting " + self.name)
        # calling function 'print_time'
        print_time(self.name, self.delay, 5)
        print("Exiting " + self.name)

# function print_time with all the necessary params
def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Starting threads
thread1.start()
thread2.start()
print("Main Thread") 