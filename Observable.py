class Observable():
    observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify(self, *args):
        for i in range(len(self.observers)):
            self.observers[i].update(args[0])
