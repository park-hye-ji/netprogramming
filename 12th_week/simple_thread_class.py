import threading
import datetime

class myThread(threading,Thread):
    def __init__(self,name,counter):
        super().__init__()
        self.name=name
        self=counter=counter