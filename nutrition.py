d={"Apple":130, "Avocado":50, "Banana":110, "Cantaloupe":50, "Grapefruit":60,
   "Grapes":90, "Honeydew Melon":50, "Kiwifruit":90, "Lemon":15, "Lime":20,
   "Nectarine":60, "Orange":80, "Peach":60, "Pear":100, "Pineapple":50, "Plums":70,
   "Strawberries":50, "Sweet Cherries":50, "Tangerine":50, "Watermelon":80}
a=input("Enter your fruit:\n")
if a in d:
    print("Calories:",d[a])
elif a not in d:   #or else:
    pass
#an unnecessary note
