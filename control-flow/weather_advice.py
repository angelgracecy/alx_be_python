weather = input("What's the weather like today? (sunny/rainy/cold):.")
if\s+weather\s*==\s*['\"]sunny['\"]\s*:\s*print\s*\(\s*['\"]Wear a t-shirt and sunglasses\.['\"]\s*\)
    print("wear a t-shirt and sunglassses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
