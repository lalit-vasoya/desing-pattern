# ------------------------------
# Observer Design Pattern[Behavioral]
# ------------------------------
# Define a one-to-many dependency between objects
# where a state change in one object results in all its dependents being notified and updated automatically.


class Subject:

    def __init__(self):
        self.__subscribers = []

    def subscribe(self, observer):
        # register the observer
        self.__subscribers.append(observer)

    def get_subscriber(self):
        # list all subscriber
        return [type(sub).__name__ for sub in self.__subscribers]

    def notify(self, notification_msg):
        for sub in self.__subscribers:
            sub.notify(notification_msg)


class Observer1:

    def __init__(self, subject):
        # Subscribe observer1 object to the subject class object
        subject.subscribe(self)

    def notify(self, notification_msg):
        # receive notification from the subject class
        print(type(self).__name__, notification_msg)


class Observer2:

    def __init__(self, subject):
        # Subscribe observer1 object to the subject class object
        subject.subscribe(self)

    def notify(self, notification_msg):
        # receive notification from the subject class
        print(type(self).__name__, notification_msg)


if __name__ == '__main__':

    subject = Subject()

    print('Subscriber are :', subject.get_subscriber())
    observer1 = Observer1(subject)
    observer2 = Observer2(subject)

    subject.notify(": Ping from subject class")
    print('Subscriber are :', subject.get_subscriber())
