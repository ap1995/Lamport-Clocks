import threading

class LamportClock:
    time = 0
    processID = 0
    def __init__(self, time, processID, queue):
        self.lock = threading.Lock()
        self.time = 1
        self.processID = processID

    def incrementTime(self):
        self.time = self.time +1
        print("Current Lamport time is "+ self.getLamportTime())

    def getLocalTime(self):
        return self.time

    def getLamportTime(self):
        return (str(self.time) + "."+ str(self.processID))

