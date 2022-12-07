import random

# from pizza_app import new_price
from app import Total_price_delivery

new_price = 0


def discount_game():
    global new_price
    game = input("\nDo you want to Play a Game and get discount? yes/no: ")
    while True:
        if game == "yes" or game == "y":
            play1_value = random.randint(1, 9)
            play2_value = random.randint(1, 9)
            play_value = play1_value * play2_value
            print("Your Game Discount Percentage is: ", play_value, "%")
            new_price = Total_price_delivery * (1 - (play_value / 100))
            print("\n\t\t\t\t\tYour Final Price with Discount Game is", round(new_price, 2), "$")
            print("\n\t\t\t\t\t\t\t\t 'BON APPETIT!!!' Enjoy your Pizza!!! \n\t\t\t\t\t\t\t\t\tHave a Nice Day!!!")
            break

        else:
            print("\n\t\t\t\tThe Total Price with Delivery for your Order will be: ", Total_price_delivery, "$")
            print("\n\t\t\t\t\t\t\t\t 'BON APPETIT!!!' Enjoy your Pizza!!! \n\t\t\t\t\t\t\t\t\t\tHave a Nice Day!!!")
            break


