#This program will allow the user to determine how much money it will take to
#make the desired number of breakfast burritos based on the recipe shown and the
#current costs of each ingredient.

#Cost and amount variables. Amounts are per unit per burrito.
unitCostEgg = float(2.99)
unitCostPotatoe = float(1.00)
unitCostCheese = float(4.99)
unitCostTortilla = float(3.75)
unitCostSausage = float(8.30)
unitAmountEgg = float(12)
unitAmountPotatoe = float(8)
unitAmountCheese = float(16)
unitAmountTortilla = float(12)
unitAmountSausage = float(32)

#List ingredients needed and ask the user to enter the number of burritos desired
print ('==================================================')
print ('Ingredients to make 12 breakfast burrito and the\n'\
       'approximate costs of the required ingredients:\n')
print ('12 large eggs\t\t\t$', unitCostEgg)
print ('8 oz of tater tots\t\t$', unitCostPotatoe)
print ('16 oz cheddar cheese\t\t$', unitCostCheese)
print ('12 whole tortilla (10 inch)\t$', unitCostTortilla)
print ('32 oz sausage\t\t\t$', unitCostSausage)
print ()
while True:
    try:
        numberBurritos = float(input('How many Burritos do you want to make? '))
        while numberBurritos < 1:
            print ("I'm sorry Dave, I cannot allow that.  You must make at least 1 burrito.")
            numberBurritos = float(input('How many burritos did you want to make? '))
        break
    except ValueError:()
print ('===================================================\n')

#Calculate amounts per item and total cost
costEgg = float(numberBurritos*unitCostEgg/12)
costPotatoe = float(numberBurritos*unitCostPotatoe/12)
costCheese = float(numberBurritos*unitCostCheese/12)
costTortilla = float(numberBurritos*unitCostTortilla/12)
costSausage = float(numberBurritos*unitCostSausage/12)
totalCost = float(costEgg+costPotatoe+costCheese+costTortilla+costSausage)
amountEgg = float(numberBurritos*unitAmountEgg/12)
amountPotatoe = float(numberBurritos*unitAmountPotatoe/12)
amountCheese = float(numberBurritos*unitAmountCheese/12)
amountTortilla = float(numberBurritos*unitAmountTortilla/12)
amountSausage = float(numberBurritos*unitAmountSausage/12)

#Prints a list of cost and amount needed per ingredient based on number of burritos being made
print ('The ingredient costs and amounts required for', numberBurritos, '\n'\
       'breakfast burrito(s) will be:\n')
print ('Eggs: \t\t$', format(costEgg,',.2f'), '\t',format(amountEgg,',.2f'), 'whole egg(s)\n'\
       'Potatoes: \t$', format(costPotatoe,',.2f'),'\t',format(amountPotatoe,',.2f'), 'oz\n'\
       'Cheese: \t$', format(costCheese,',.2f'), '\t',format(amountCheese,',.2f'), 'oz\n'\
       'Tortilla: \t$', format(costTortilla,',.2f'),'\t',format(amountTortilla,',.2f'),'Tortilla(s)\n'\
       'Sausage: \t$', format(costSausage,',.2f'),'\t',format(amountSausage,',.2f'), 'oz\n')

#Print the total cost of ingrediants
if numberBurritos >= 10000:
    print ('Congratulations! You get a $5000.00 discount for ordering \n' \
           'at least 10,000 burritos!\n\n',\
           '\tTotal cost:\t\t', ' $',format(totalCost,',.2f'),' \n',\
           '\tYour discount:\t\t','-$ 5000.00 \n',\
           '\tFinal Total cost:\t',' $',format((totalCost-5000),',.2f'),'\n')
    print ('WOW! hope your legion appreciates all your hard work!\n')
elif numberBurritos == 300:
    print ('Congratulations! You get a $300.00 discount for ordering\n' \
           'FOR...SPAR...TA!!!!\n\n',\
           '\tTotal cost:\t\t', ' $',format(totalCost,',.2f'),' \n',\
           '\tYour discount:\t\t','-$ 300.00 \n',\
           '\tFinal Total cost:\t',' $',format((totalCost-300),',.2f'),'\n')
elif numberBurritos == 1:
    print ("Onnnnnneeee...is the loneliest number that you'll ever do...\n"\
           "Twoooooo....can be as bad as one....\n")
    print ('Total cost: \t$', format(totalCost,',.2f'),'\n')
else:
    print ('Total cost: \t$', format(totalCost,',.2f'),'\n')
print ('More information and complete recipe guide can be found at:')
print ('http://www.food.com/recipe/angels-easy-breakfast-burritos-161872')

