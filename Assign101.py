'''
Michael Perez

Assignment 10.1: Your Own Class

Sources: Textbook, Lecture, and Python Library
'''
class Cake: #creating a class for a cake
    def __init__(self, flavor): #defining the variables through a constructor
        self.flavor = flavor #creates a flavor for string that is required to make function work 
        #self.layers = layers 
        self.pieces = 10 #each cake has a standard 10 slices

    def __str__(self): #creating a string that returns the variables above 
        x = "%s cake slices left = %d" % (self.flavor, self.pieces)
        return x #creates a message to show how much cake is left

    def eat_Piece(self): #function that removes one piece from the whole cake 
        if self.pieces > 0: #created an if statement that makes functios work if there is more than 0 pieces of cake 
            self.pieces -= 1 #takes a piece of cake away 
        else:
            print("No more pieces of cake left") #creating a message to say no more cake 
  
    def add_Piece(self): #function that adds one piece to the whole cake 
        if self.pieces < 100: #created an if statement that makes functios work if there is less than 100 pieces of cake 
            self.pieces += 1 #adds one piece of cake 
            print("More cake has been delivered!") #creating a message to say more cake has been delivered 
        else:
            print("There is enough for everyone, we have ordered 100 slices of cake!")

    def getPieces(self): #gets the given amount of pieces in the cake
        return self.pieces #returns variable for pieces 

    def getFlavor(self): #gets the given flavor of cake 
        return self.flavor #returns variable for flavor 

def main():
    #Creating cakes from the class created above 
    Cake1 = Cake("Vanilla") 
    Cake2 = Cake("Chocolate")
    print(Cake1)
    print(Cake2)
    #Testing for vanilla cake for instance adding
    print("-"*20)
    print("Number of slices left in Cake1: %s" % Cake1.getPieces())
    print("Eating a slice of %s!" % Cake1.getFlavor())
    Cake1.add_Piece()
    print(Cake1)

    print("-"*20)
    for y in range(5):
        print("Eating a slice of %s!" % Cake1.getFlavor())
        Cake1.add_Piece()
        print(Cake1)
    #Testing for chocolate cake for instance subtracting
    print("-"*20)
    print("Number of slices left in Cake2: %s" % Cake2.getPieces())
    print("Eating a slice of %s!" % Cake2.getFlavor())
    Cake2.eat_Piece()
    print(Cake2)

    print("-"*20)
    for y in range(7):
        print("Eating a slice of %s!" % Cake2.getFlavor())
        Cake2.eat_Piece()
        print(Cake2)

if __name__ == "__main__":
  main()