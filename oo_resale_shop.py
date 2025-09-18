from Computer import Computer 

class ResaleShop: #Class that allows you to buy computer (add it from the inventory), sell computer (remove it from the inventory) and shows the inventory when asked
    # computer_ID: int
    store_Balance: float 

    # What attributes will it need?
    inventory : list = []
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

    def __init__(self, store_balance:float, inventory:list):
        self.inventory= inventory
        self.store_Balance = store_balance

    def buy_Computer(self, computer:Computer):
        self.inventory.append(computer)
        # self.inventory.index = self.computer_ID
        self.store_Balance -= computer.price
        # print(computer.description, "has a computer ID of", self.inventory.index)
        print(computer.description, "has been purchased for $", computer.price, ". The store's balance is now $", self.store_Balance)

    def sell_Computer(self, computer:Computer):
        self.inventory.remove(computer)
        self.store_Balance += computer.price
        print(computer.description, "has been sold for $", computer.price, ". The store's balance is now $", self.store_Balance)

    def show_Inventory(self):
        for computer in self.inventory:
            print(computer.description, "is in Resale Shop's Inventory")


def main():
    newComputer: Computer = Computer("2019 Macbook Pro", "Intel", 256, 16, "High Sierra", 2019, 1000)
    newComputer.updatePrice(300)
    empty_List = []
    newresaleShop: ResaleShop = ResaleShop(3000.00, empty_List)
    newresaleShop.buy_Computer(newComputer)
    newresaleShop.show_Inventory() 
    newresaleShop.sell_Computer(newComputer)

if __name__ == "__main__":
    main()