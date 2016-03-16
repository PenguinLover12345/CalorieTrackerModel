def main():
    mealRatios = [0.2, 0.3, 0.4, 0.1]; #Breakfast, Lunch, Dinner, Snack
    calorieGoal = 2000 #Calorie goal
    calorieCurrent = 0 #Current amount of calories
    mealCalories = [0, 0, 0, 0] #calorie allocation
    
    updateMealCalories(mealRatios, calorieGoal, mealCalories)
    printInformation(mealRatios, mealCalories)
    
    updateMealRatios(mealRatios)
    updateMealCalories(mealRatios, calorieGoal, mealCalories)
    printInformation(mealRatios, mealCalories)
    
    inputFood(calorieCurrent, 300, 0)


def updateMealCalories(mealRatios, calorieGoal, mealCalories):
    for i in xrange(0, len(mealRatios)):
        mealCalories[i] = calorieGoal * mealRatios[i]
       
    return mealCalories #return unneeded since pass by reference

def updateMealRatios(mealRatios):#, newMealRatios) #How are we going to update the meal ratios
    for i in xrange(0, len(mealRatios)):
        mealRatios[i] = 0.25
    
    return mealRatios #return unneeded since pass by reference

def inputFood(calorieCurrent, calorieInput, meal): #0 = breakfast, 1 = lunch, 2 = dinner, 3 = snack
    calorieCurrent += calorieInput
    

def printInformation(mealRatios, mealCalories):
    print mealRatios
    print mealCalories
    



main()