# In this part we have 2 threads that we want to start at the same time but with different
# delays so we can track them

# Importing libraries that we will use
import threading
import time

# Main Function that both threads will use
def print_time(threadName, delay):
    count = 0
    # We create 5 instances of thread
    while count < 5:
        # Set the delay that is passed through args
        time.sleep(delay)
        count += 1
        # print the name that is passed through args and currect time
        print("%s: %s" % (threadName, time.ctime(time.time())))

# Used try-catch just in case
try:
    # declaration of first thread
    t1 = threading.Thread( target=print_time, args=("Thread-1",1) )
    # declaration of second thread
    t2 = threading.Thread( target=print_time, args=("Thread-2",1) )
    # Set name for first thread
    t1.setName("Aleksandar")
    # Started first thread
    t1.start()
    # Set name for second thread
    t2.setName("Dusan")
    # Started second thread
    t2.start()
except:
    # In case of an error just point to this message, do not close the program
    print("Error: unable to start thread")

# Printing how many threads are active
# In this case 3 because we declared 2 ours and 1 is default main thread
print(threading.active_count())
# Printing information about the thread, here we can see the names we set
print(threading.enumerate())