import time

class Timer:
    def __init__(self) -> None:
        self.__start__ = 0
        self.__end__ = 0
        self.__time_elapsed__ = 0

    @property
    def start_time(self):
        self.__start__ = time.time()

    @property  
    def end_time(self):
        self.__end__ = time.time()
        self.__time_elapsed__ = self.__end__ - self.__start__

    @property
    def get_time(self):
        return self.__time_elapsed__

