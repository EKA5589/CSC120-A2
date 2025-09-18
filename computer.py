class Computer: #Class that updates price, OS and refurbishes the computer

    # What attributes will it need?
    description: str
    processor_type: str 
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description:str, processor_type:str, hard_drive_capacity:int, memory:int, operating_system:str, year_made:int, price:float):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # def create_computer(description: str,
                    # processor_type: str,             Thought this was necessary.. kept for my records
    #                 hard_drive_capacity: int,
    #                 memory: int,
    #                 operating_system: str,
    #                 year_made: int,
    #                 price: int):
    #     return {'description': description,
    #         'processor_type': processor_type,
    #         'hard_drive_capacity': hard_drive_capacity,
    #         'memory': memory,
    #         'operating_system': operating_system,
    #         'year_made': year_made,
    #         'price': price}
    
    # def buyComputer(self, computer:dict): 
    #     self.computer = computer
    
    def updatePrice(self, newPrice:float): 
        self.price = newPrice
        print(self.description, "now costs $", newPrice)
        
    def updateOS(self, newOS:str):
        self.newOS = newOS
        print(self.description, "is now running", newOS, "Operating System")

    def refurbish(self, new_os: str):
        
        if new_os != self.operating_system:
                self.operating_system = new_os # update details after installing new OS
                print(self.description, "is now running", new_os)
        else :
              print("You are already running the newest operating system!")

        if self.year_made < 2000:
                self.price= 0 # too old to sell, donation only
                print(self.description, "now costs $", self.price)
        elif self.year_made < 2012:
                self.price = 250 # heavily-discounted price on machines 10+ years old
                print(self.description, "now costs $", self.price)
        elif self.year_made < 2018:
                self.price = 550 # discounted price on machines 4-to-10 year old machines
                print(self.description, "now costs $", self.price)
        else:
                self.price = 1000 # recent stuff
                print(self.description, "now costs $", self.price)

    


def main ():
    newComputer: Computer = Computer("2019 Macbook Pro", "Intel", 256, 16, "High Sierra", 2019, 1000)
    newComputer.updatePrice(300)
    newComputer.refurbish("High Sierra")
    

if __name__ == "__main__":
    main()



    # What methods will you need?