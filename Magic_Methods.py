import csv

class Astronaut:
    def __init__(self, name, flightHour, status):
        self.__name = name
        self.__flightHour = flightHour
        self.__status = status

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name

    def get_flightHour(self):
        return self.__flightHour

    def set_flightHour(self, flightHour):
        self.__flightHour = flightHour

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def __gt__(self, other):
        print(f"Does {self.__name} have more flight hours than {other.__name}?")
        return self.__flightHour > other.__flightHour

    def __ge__(self, other):
        print(f"Does {self.__name} have at least the same flight hours than {other.__name}?")
        return self.__flightHour >= other.__flightHour

    def __eq__(self, other):
        print(f"Does {self.__name} have  the same flight hours than {other.__name}?")
        return self.__flightHour == other.__flightHour

    def __str__(self):
        return f"{self.__name}, {self.__status}"


with open("astronauts.csv", "r") as aCSV:
    astronautDict = list(csv.DictReader(aCSV))

astronautList = list(map(lambda x: Astronaut(x["Name"], int(x["Space Flight (hr)"]), x["Status"]), astronautDict))

print(astronautList[0].__dict__)

print(astronautList[3] > astronautList [5])

for i in astronautList:
    print(i)

