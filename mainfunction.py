from app import welcome_text
from app import exit_message


def customer_order():
    print("\n**************************** 'Pizza.io' House of Pizza  ****************************\n")
    age = int(input("\t\tTo continue your order Please enter your age: "))
    # welcome_text()
    while age < 18:
        exit_message()
    else:
        welcome_text()
        while True:
            # Ordering a pizza size
            from app import pizaa_firstorder
            pizaa_firstorder()
            # Asking for extra cheese
            from app import add_extra_menu
            add_extra_menu()
            # Asking to order another
            from app import next_order_req
            next_order_req()


customer_order()
