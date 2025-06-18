calorie_data = {
    "egg": 70,
    "carrot": 20,
    "peanut butter": 1.0,           
    "toast": 80,
    "banana": 90,
    "chicken breast": 1.65,   
    "rice": 200,
    "pineapple": 95,
    "milk": 120,
    "yogurt": 1.0             
}


per_gram_items = ["peanut butter", "chicken breast", "yogurt"]

def parse_input(item_input):
    try:
        parts = item_input.strip().split(' ', 1)
        quantity = parts[0].lower().replace("g", "")
        food = parts[1].lower()

        quantity = float(quantity)

        
        if food.endswith("s") and food[:-1] in calorie_data:
            food = food[:-1]

        return quantity, food
    except:
        print("⚠️ Invalid input. Use format like: 2 eggs OR 100g peanut butter")
        return None, None

def get_meal_calories(meal_name):
    print(f"\n🍽️ Enter items for {meal_name} (type 'done' to finish):")
    total = 0
    while True:
        entry = input("-> ").lower()
        if entry == "done":
            break
        quantity, food = parse_input(entry)
        if food in calorie_data:
            if food in per_gram_items:
                calories = quantity * calorie_data[food]
            else:
                calories = quantity * calorie_data[food]
            print(f"✅ {quantity} {food} = {calories:.1f} kcal")
            total += calories
        else:
            print("❌ Unknown food item.")
    return total


print("🥗 Welcome to the Calorie Tracker!")

breakfast = get_meal_calories("Breakfast")
lunch = get_meal_calories("Lunch")
dinner = get_meal_calories("Dinner")

daily_total = breakfast + lunch + dinner

print("\n📊 Calorie Summary:")
print(f"Breakfast: {breakfast:.1f} kcal")
print(f"Lunch:     {lunch:.1f} kcal")
print(f"Dinner:    {dinner:.1f} kcal")
print(f"Total:     {daily_total:.1f} kcal")