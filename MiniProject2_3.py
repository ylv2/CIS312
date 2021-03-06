#This program will allow the user to determine how much money it will take to
#make the desired number of breakfast burritos based on the recipe shown and the
#current costs of each ingredient.

#Cost and amount variables. Amounts are per unit per burrito.
unitCostEgg = float(0.48)
unitCostPotatoe = float(0.24)
unitCostCheese = float(0.31)
unitCostTortilla = float(0.37)
unitCostSausage = float(0.42)
unitAmountEgg = 3
unitAmountPotatoe = 6
unitAmountCheese = 1
unitAmountTortilla = 1
unitAmountSausage = 4

#List ingredients needed and ask the user to enter the number of burritos desired
print ('==================================================')
print ('Ingredients to make (1) LARGE breakfast burrito \n'\
       'and the approximate costs of the ingredients:\n')
print ('3 large eggs\t\t\t$', unitCostEgg)
print ('6 oz of potatoes\t\t$', unitCostPotatoe)
print ('1 oz cheddar cheese\t\t$', unitCostCheese)
print ('1 whole tortilla (10 inch)\t$', unitCostTortilla)
print ('4 oz sausage\t\t\t$', unitCostSausage)
print ()
numberBurritos = float(input('How many Burritos do you want to make? '))
print ('===================================================\n')

#Calculate amounts per item and total cost
costEgg = float(format((numberBurritos*unitCostEgg),'.2f'))
costPotatoe = float(format((numberBurritos*unitCostPotatoe), '.2f'))
costCheese = float(format((numberBurritos*unitCostCheese),'.2f'))
costTortilla = float(format((numberBurritos*unitCostTortilla),'.2f'))
costSausage = float(format((numberBurritos*unitCostSausage), '.2f'))
totalCost = float(format((costEgg+costPotatoe+costCheese+costTortilla+costSausage),'.2f'))
amountEgg = float(format((numberBurritos*unitAmountEgg), '.2f'))
amountPotatoe = float(format((numberBurritos*unitAmountPotatoe), '.2f'))
amountCheese = float(format((numberBurritos*unitAmountCheese), '.2f'))
amountTortilla = float(format((numberBurritos*unitAmountTortilla), '.2f'))
amountSausage = float(format((numberBurritos*unitAmountSausage), '.2f'))


#Prints a list of cost and amount needed per ingredient based on number of burritos being made
print ('The ingredient costs and amounts required for', numberBurritos, '\n'\
       'breakfast burrito(s) will be:\n')
print ('Eggs: \t\t$', costEgg, '\t',amountEgg, 'whole egg(s)\n'\
       'Potatoes: \t$', costPotatoe,'\t',amountPotatoe, 'oz\n'\
       'Cheese: \t$', costCheese, '\t',amountCheese, 'oz\n'\
       'Tortilla: \t$', costTortilla,'\t',amountTortilla,'Tortilla(s)\n'\
       'Sausage: \t$', costSausage,'\t',amountSausage, 'oz\n')

#Print the total cost of ingrediants
print ('Total cost: \t$', totalCost)


