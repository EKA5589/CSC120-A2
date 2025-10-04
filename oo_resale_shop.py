from computer import Computer 

class ResaleShop: 
    

   
    inventory: list = []
   
    def __init__(self, inventory:list):
        self.inventory== inventory

    def buy(self, computer:Computer):
        self.inventory.append(computer)
        print(computer.description, "has been purchased for $", computer.price, ".")

    def sell(self, computer:Computer):
        for i in self.inventory:
            if computer == i:
                self.inventory.remove(computer)
                print(computer.description, "has been sold for $", computer.price, ".")
            else :
                print(computer.description, "could not be found within our inventory.")
        

    def printInventory(self):
        for computer in self.inventory:
            print(computer.description, "is in Resale Shop's Inventory")


def main():
    newComputer: Computer = Computer("2019 Macbook Pro", "Intel", 256, 16, "High Sierra", 2019, 1000)
    myComputer: Computer = Computer("2013 Macbook", "Windows", 128, 16, "Big Sur", 2013, 300)
    empty_List = []
    newresaleShop: ResaleShop = ResaleShop(empty_List)
    newresaleShop.buy(newComputer)
    newresaleShop.buy(myComputer)
    newresaleShop.printInventory()
    newresaleShop.sell(newComputer)


if __name__ == "__main__":
    main()