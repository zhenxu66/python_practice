
class battery:
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity

    def des(self):
        print(f"{self.model} capacity is {self.capacity}")

class module(battery):
    def __init__(self, serialnumber, tsu, model, capacity):
        super().__init__(model, capacity)
        self.serialnumber = serialnumber
        self.tsu = tsu

    def prtmodel(self):
        print(f"{self.model} with capacity of {self.capacity} is built with tsu type {self.tsu} with SN of {self.serialnumber}")



def main():
    batt1 = battery('50G', '4.7Ah')
    batt1.des()

    module1= module(4140, 'type A', 'M48A', '2Ah')
    module1.des()
    module1.prtmodel()

if __name__ == "__main__":
    main()