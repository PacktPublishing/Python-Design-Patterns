import copy

class Memento:

    def __init__(self, data):
        # make a deep copy of every variable in the given class
        for attribute in vars(data):
            setattr(self, attribute, copy.deepcopy(getattr(data, attribute)))


class Undoable:

    def __init__(self):
        # each instance keeps the latest saved copy so that there is only one
        # copy of each in memory
        self.__last = None

    def save(self):
        self.__last = Memento(self)

    def undo(self):
        for attribute in vars(self):
            setattr(self, attribute, getattr(self.__last, attribute))


class Data(Undoable):

    def __init__(self):
        super(Data, self).__init__()
        self.numbers = []
