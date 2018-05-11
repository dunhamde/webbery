import time

class Activity:
    name = 'hello world'
    score = 99

    def __init__(self, aname):
        self.name = aname

    def Score(self):
        return self.score
    def Name(self):
        return self.name
    def AReport(self):
        print('Name: ' + self.name + ', Score: ' + str(self.score))

class Event:
    def __init__(self,ename,edate,act):
        self.name = ename
        self.date = edate
        self.activity = act


    def Report(self):
        print(self.name)
        print(self.date)
        self.activity.AReport()


x = Activity('jumping')
print(x.Name())
print(x.Score())

date = time.strftime("%d/%m/%Y")
ev = Event('wod', date, x)
ev.Report()