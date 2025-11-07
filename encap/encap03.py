class Machine:
    def __init__(self):
        pass
    def __start_engine(self):
        print("Engine started")

    def start(self):
        return self.__start_engine()  # Access a private method Through a Public Method //  Use Name Mangling (Not Recommended, but Works)
m = Machine()
m.start()