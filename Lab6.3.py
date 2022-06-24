import random, time
from threading import Thread

class SleepyThread(Thread):

    def __init__(self, number, sleepMax):
        Thread.__init__(self, name="Thread " + str(number))
        self.sleepInterval = random.randint(1, sleepMax)
    def run(self):
        print("%s starting, with sleep interval: %d seconds" % \
              (self.getName(), self.sleepInterval))
        time.sleep(self.sleepInterval)
        print("%s waking up" % self.getName())

def main():
    numThreads = int(input("Enter the number of threads: "))
    sleepMax = int(input("Enter the maximum sleep time: "))
    threadList = []
    for count in range(numThreads):threadList.append(SleepyThread(count + 1, sleepMax))
    for thread in threadList: thread.start()

if __name__ == "__main__":
    main()

