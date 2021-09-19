class CoffeeMachine:
    def __init__(self):
        self.amount_money = 550
        self.amount_water = 400
        self.amount_milk = 540
        self.amount_coffee = 120
        self.amount_cups = 9
 
    def buying(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee_kind = input()
        espresso = "1"
        latte = "2"
        cappuccino = "3"
        back = "back"
        if coffee_kind == espresso:
            self.making_coffee(250, 0, 16, 4)
        elif coffee_kind == latte:
            self.making_coffee(350, 75, 20, 7)
        elif coffee_kind == cappuccino:
            self.making_coffee(200, 100, 12, 6)
        elif coffee_kind == back:
            return
            


    def making_coffee(self, water, milk, coffee, money):
        if self.amount_water >= water:
            self.amount_water -= water
        else:
            print("Sorry, not enough water!")
            return
        if self.amount_milk >= milk:
            self.amount_milk -= milk
        else:
            print("Sorry, not enough milk!")
            return
        if self.amount_coffee >= coffee:
            self.amount_coffee -= coffee
        else:
            print("Sorry, not enough coffee!")
            return
        if self.amount_cups >= 1:
            self.amount_cups -= 1
        else:
            print("Sorry, not enough cups!")
            return
        self.amount_money += money
        print("I have enough resources, making you a coffee!")
           

    def filling(self):
        print("Write how many ml of water you want to add:")
        self.amount_water += int(input())
        print("Write how many ml of milk you want to add:")
        self.amount_milk  += int(input())
        print("Write how many grams of coffee beans you want to add:")
        self.amount_coffee += int(input())
        print("Write how many disposable coffee cups you want to add:")
        self.amount_cups += int(input())
        
    def taking(self):
        print(f"I gave you ${self.amount_money}")
        self.amount_money = 0
                
    def remaining(self):
        print(f'''The coffee machine has:
        {self.amount_water} of water
        {self.amount_milk} of milk
        {self.amount_coffee} of coffee beans
        {self.amount_cups} of disposable cups
        {self.amount_money} of money''')
        
best_machine = CoffeeMachine() 
  
while True:
    print("Write action (buy, fill, take, remaining, exit):")
    pick = input()
    buy = "buy"
    fill = "fill"
    take = "take"
    exit = "exit"
    reszta = "remaining"
    if pick == buy:
        best_machine.buying()  
    elif pick == fill:
        best_machine.filling()
    elif pick == take:
        best_machine.taking()
    elif pick == reszta:
        best_machine.remaining()
    elif pick == exit:
        break
              
