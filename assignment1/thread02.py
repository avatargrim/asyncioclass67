# running a function with arguments in another thread
from time import sleep,ctime
from threading import Thread

# custom thread class
class CustomThread(Thread):

    def run(itself):
        # block for a moment
        sleep(1)
        # display a message
        print(f'{ctime()} This is coming from another thread')
    
# create a thread
thread = CustomThread
# start the thread
thread.start()
# wait for the thread to finish
print(f'{ctime()} Waiting for thread to finish')
thread.join()
