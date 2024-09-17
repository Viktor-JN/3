class Inventory:
    def __init__(self, id, name, description, price, quantity):
        self.items = {}
        self.id = id
        self.name = name
        self.price = price
        self.desc = description
        self.quantity = quantity
        append_string = f"id: {self.id}, Name: {self.name}, price: {self.price}, description: {self.desc}, quantity: {self.quantity}"
        self.items[name] = append_string
       
    #TODO: Skapa check_inventory (visa produkter)
    def check_inventory(self):
        for i in self.items:
            print(i)
    
    def check_specific(self):
        for i in self.items:
            print(i)
        choice = input("Vilken vill du kolla på: ")
        print(self.items[choice])
        
    #TODO: Skapa add_item-metod för produkter

    #TODO: Skapa remove-metod för produkter
    def remove_item(self):
        for index, i in self.items():
            print(i, self.items[index][i])

    #TODO: Skapa sparfunktion
    #TODO: (Frivillig) Skapa en metod som visar mest sålda produkt

def main():
    adress = Inventory(16, "Hus", "En bostad", "10kr", 5)
    print(adress.name)
    adress.check_inventory()
    print(adress.items['Hus'])

if __name__ == "__main__":
    main()