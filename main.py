import random #Random module

userDB = { "id": "hello" }; #login -> dictionary

FoodDB = [["low fat milk 200ml", 100], ["egg", 75], ["cabbage salad 50g", 70], ["grapefruit", 100], ["rice 2/3 bowl", 200], ["apple", 150], ["chicken breast", 150], ["soy milk", 90], ["cucumber", 18], ["sweet potato", 180], ["plain yoghurt", 130], ["wheat bread", 80], ["salmon", 180], ["bell pepper", 33], ["tomato", 18], ["granola 1/2cup", 250], ["peanut butter 2Tbsp", 180], ["almond 1/4cup", 170], ["avocado", 240], ["tofu", 63], ["steak 100g", 179], ["banana", 105], ["cottage cheese", 84], ["oat meal", 140], ["dark chocolate bar", 216]];
# Food&Calories Matrix
print("Welcome to our diet assistant. Please type in 'hello' to check if you are robot or not!");
Id = input(""); #type in hello to log in
if(userDB["id"] == Id): #If hello is typed in(userDB["id"]), it's success, and if not, it's failed. If failed, program ends. 
  print("Login Success");
else:
  print("Login Failed");
  exit(0);

Age = int(input("Enter your age: ")); # input age
Weight = float(input("Enter your Weight(kg): ")); # input weight(kg), float
Height = float(input("Enter your Height(cm): "));
# input height(cm, float)
Sex = bool(input("Select your sex(men is 1, women is 0): ")); # true is men, false is women

print();
BMI = Weight / (Height/100 * Height/100);
# BMI equation
if(BMI <= 18.5):
  print("You are UnderWeight");
elif(BMI < 25):
  print("You are Average");
elif(BMI < 30):
  print("You are Overweight");
else:
  print("You are Obese");
# conditional statements to tell you if you're average, under, over, etc.

if(Sex): #Recommend Weight calcuation for men and women - if(sex) means sex=true, which is men, so first equation is men. second equation is women since it is 'else'
  Recommend = (Height/100 * Height/100) * 22;
else:
  Recommend = (Height/100 * Height/100) * 21;

print("Your Recommend Weight is: " + str(int(Recommend)));

print("-------------------------");
print();
print("Selectable Menu");
print("1 - Maintain weight");
print("2 - Mild weight loss(0.25kg/week)");
print("3 - Weight loss(0.5kg/week)");
print("4 - Extreme weight loss(1kg/week)");

def calcBMR(Weight, Height, Age, Sex): #BMR calcuation
  if(Sex):
    BMR = 13.397 * Weight + 4.799 * Height + 5.677 * Age + 88.362; #men
  else:
    BMR = 9.247 * Weight + 3.098 * Height + 4.330 * Age + 447.593; #women
  return BMR; #BMR return

print();
Selected = int(input("Select menu: ")); #input selected menu
print();

MyBMR = calcBMR(Weight, Height, Age, Sex); #for each selected menu of weight loss goal, there are certain percentage fitting for the amount of calories to eat
if(Selected == 1): #BMR set for each menu
  MyBMR = MyBMR;
elif(Selected == 2):
  MyBMR = MyBMR * 0.87;
elif(Selected == 3):
  MyBMR = MyBMR * 0.75;
else:
  MyBMR = MyBMR * 0.49;


print("You should eat " +  str(int(MyBMR)) + " Calories per day");
print("Your recommended diet plan is: ")

NowCalories = 0; #start from 0 calroies
RecommendFoodList = [];  # recommended diet list
while(NowCalories < MyBMR): # Add calroies until the number of Nowcalroies don't get bigger than MyBMR
  randomIndex = random.randrange(0, len(FoodDB) - 1); # Get Random Food Element(food&calorie)
  randomAmount = random.randrange(1, 3);
  # Get Random Amount of Food

  NowCalories = NowCalories + randomAmount * FoodDB[randomIndex][1];
  # Random amount of food x calroies
  RecommendFoodList.append(FoodDB[randomIndex][0] + " " + str(randomAmount));
  # add randomIndex food from FoodDB to the list

for i in range(len(RecommendFoodList)): #repeat over list and print the recommended food list
  print(RecommendFoodList[i]);
