
print("[My-Budget-management]\n")

class Management:
    def __init__(self,month,week,amount, budget):
        self.Month = month
        self.Week = week
        self.Amount = amount
        self.Budget = budget
        print("On {} in {}, I will take the amount of {} for {}".format(self.Month,self.Week, self.Amount, self.Budget))

        #Week, Amount > my attributes
        #week , amount > my dummy arguments

# main
# Object of my Class
January = Management("January","week 2", 400, "Transport"),
February = Management("February", "week 2", 700, "Grocery"),
March = Management("March", "week 2", 300, "Internet Data"),
April = Management("April", "week 5", 250, "Toiletries")


