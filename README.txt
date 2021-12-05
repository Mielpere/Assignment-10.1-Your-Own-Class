Michael Perez
Harikrishna Kuttivelil 
CSE-20-03
04 December 2021
README
Description of Class: This is a class that shows how objects are used within python, knowing that objects consist of both data and methods that is exactly what I did. I made a class that breaks down a cake by the amount of pieces and what type of flavor it is. This is a class code that would alert users of how much cake is being eaten at an event and what type of cake is being eaten more, for ordering more or less cake. 
Description of Class and Data Variables:
1. Class: I created a Cake class in order to create different types of objects of cake that I wanted. It sets up my template for constructing what is stored inside such as the variables, flavor and pieces. 
2. Flavor: This was a data variable that was stored as a string which could be declared anywhere in the class where it was called, given a type of flavor. 
3. Pieces: This was a data variable that stayed consistent throughout the whole code. I made it set to 10, meaning that a whole cake is 10 pieces all together.  
Description of Methods:
1. def __str__(self): I created a x variable to make a method that would return the amount of cake slices left from the whole cake. It uses both data variables I created for a string that finds which specific cake needs more or less slices. /Users/meaptyne/Downloads/Report.txt
2. def eat_Piece(self): For this method, this removes one piece of cake from the whole cake. I did this by creating an if statement where if self.pieces is greater than 0, there would be a slice of cake subtracted. It calls the pieces variable whenever a cake is eaten in an if statement. 
3. def add_Piece(self): For this method, this adds one piece of cake to order/make. I did this by creating an if statement where if self.pieces is less than 100 (it could have been more than 100 but I was being reasonable in the situation of an event/gathering), there would be a slice of cake added to order. It calls the pieces variable whenever a cake is eaten so more can be made in an if statement.
4. def getPieces(self): In this method, it calls the pieces variable to get the given amount of pieces in the cake at the moment that is being tested in the main. It then returns the variable for pieces and this is called through the class.
5. def getFlavor(self): In this method, it calls the flavor variable to get what type of flavor the cake that is being tested in the main. It then returns the variable for flavor and this is called through the class.
Description of Demo Program:
In the demo program it essentially computes the amount of slices that have been eaten or how many slices need to be readded depending on how much cake is left of what flavor. The first thing I did was make two types of cakes in my main function, vanilla and chocolate, and I tested for both instances. For vanilla I used the getPieces, getFlavor, and add_piece to find how much cake needed to be added for a range of 5. For chocolate I used the getPieces, getFlavor, and eat_piece to find how much cake was being eaten with a range of 7. 
Instructions: 
To run the demo program, you have to create a cake flavor in the main function through the class above and print it (Ex. Cake1= Cake(“Strawberry”)). For that cake flavor, you would then test it through calling one of the functions like add_Piece or eat_Piece which would then tell you how many pieces are left though the getPieces method.