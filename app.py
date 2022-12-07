pizza_size = {
    "s": 40,
    "m": 50,
    "l": 60,
    "xl": 75}
quantity = 0
qty_extra = 0
extra = 2
net_price = 0
total_price = 0
extra_cheese = 0
beersheva_delivery = 20
outside_delivery = 60
Total_price_delivery = 0
next_order = "yes"
add_extra = "no"
new_price = 0


def pizza_list():
    print("\t\t\t\t\t\t * Pizza size small (s) price = 40$"
          "\n\t\t\t\t\t\t * Pizza size medium (m) price = 50$"
          "\n\t\t\t\t\t\t * Pizza size large (L) price = 60$"
          "\n\t\t\t\t\t\t * Pizza size X-large (xl) price = 75$")


def exit_message():
    print("\n\t\t\t\t\t\tSorry your age must be greater than 18. "
          "\n\t\t\t\t\t\tyou are not permitted to buy.")
    print("\n\t\t\t\t\t\t\t\t Thank you For coming!!! "
          "\n\t\t\t\t\t\t\t\t Have a nice day!!!\n")
    exit()


def welcome_text():
    print()
    print(" =" * 50)
    print("\t\t\t\tWelcome to 'Pizza.io' House of Pizza!!! Please Make your order.")
    print(" =" * 50)


def pizaa_firstorder():
    global quantity, net_price
    # Ordering a pizza size
    pizza_list()
    choice_size = input("\n Please choose pizza size s/m/l/xl: ")
    quantity = int(input("\t\t\t\tHow much quantity you need?  "))
    net_price += pizza_size[choice_size] * quantity  # --------------------- using dictionary


def add_extra_menu():
    global extra_cheese, add_extra, qty_extra, total_price
    add_extra = input("\nWould you like an extra cheese? yes/no: ")
    if add_extra == "yes" or add_extra == "y":
        qty_extra = int(input("How many extra cheese you need? "))
        extra_cheese = extra_cheese + (extra * qty_extra)
    total_price = net_price + extra_cheese
    print("The Current price is  ", round(total_price, 2), "$")


def next_order_req():
    global next_order, Total_price_delivery
    next_order = input("\nDo you want to order another pizza yes/no: ")
    if next_order == "no" or next_order == "n":
        print("\nPlease conform your destination "
              "\n\t\t\t*for beersheva (b) or "
              "\n\t\t\t*for outside of the 'Negev Capital City' (o)")
        city = input("your delivery destination b/o: ")
        while city == "b" or city == "beersheva":
            Total_price_delivery = total_price + beersheva_delivery
            print("\n\t\t\t\tThe Total price with Delivery for your order will be: ", Total_price_delivery, "$")
            # discount game using function
            from utiles import discount_game
            discount_game()
            exit()
        else:
            Total_price_delivery = total_price + outside_delivery
            print("\n\t\t\t\tThe total price with Delivery for your order will be: ", Total_price_delivery, "$")
            # discount game using function
            from utiles import discount_game
            discount_game()
            exit()
