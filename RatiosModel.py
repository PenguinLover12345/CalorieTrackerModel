def main():
    #Each user profile ---- need to add to database or app directly later
    
    mealRatios = [0.2, 0.3, 0.4, 0.1]; #Breakfast, Lunch, Dinner, Snack
    calorieGoal = 2000 #Calorie goal
    calorieCurrent = 0 #Current amount of calories
    mealCalories = [0, 0, 0, 0] #calorie allocation
    mealCurrent = [0, 0, 0, 0] #current meals
    
    updateMealCalories(mealRatios, calorieGoal, mealCalories)
    printInformation(mealRatios, mealCalories)
    
    updateMealRatios(mealRatios)
    updateMealCalories(mealRatios, calorieGoal, mealCalories)
    printInformation(mealRatios, mealCalories)
    
    inputFood(mealRatios, calorieCurrent, mealCurrent, 300, 0)
    calculateNewRatios(mealRatios, calorieGoal, mealCalories, mealCurrent)

def calculateNewRatios(mealRatios, calorieGoal, mealCalories, mealCurrent): #find the different calorie intake and multiply them by a weight
    #after each meal  assume 0s are intential skips
    
    weight = 0.5;
    diff = [0, 0, 0, 0]
    sum = 0;
    for i in xrange(0, len(mealCalories)):
        diff[i] = mealCurrent[i] - mealCalories[i]
        sum += mealCalories[i] + (diff[i] * weight)
    
    for i in xrange(0, len(mealCalories)):
        mealRatios[i] = (mealCalories[i] + (diff[i] * weight)) / sum
    updateMealCalories(mealRatios, calorieGoal, mealCalories)
    
    
def updateMealCalories(mealRatios, calorieGoal, mealCalories):
    for i in xrange(0, len(mealRatios)):
        mealCalories[i] = calorieGoal * mealRatios[i]
       
    return mealCalories #return unneeded since pass by reference

def updateMealRatios(mealRatios):#, newMealRatios) #How are we going to update the meal ratios
    for i in xrange(0, len(mealRatios)):
        mealRatios[i] = 0.25
    
    return mealRatios #return unneeded since pass by reference

def inputFood(mealRatios, calorieGoal, calorieCurrent, mealCurrent, calorieInput, meal): #0 = breakfast, 1 = lunch, 2 = dinner, 3 = snack
    calorieCurrent += calorieInput
    mealCurrent[meal] = calorieInput
    calculateNewRatios()
    

def printInformation(mealRatios, mealCalories):
    print mealRatios
    print mealCalories
    
def getCalorieGoal(calorieGoal):
    calorieGoal = 2000;
    #GET TDEE FORMULA

main()