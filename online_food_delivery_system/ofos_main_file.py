# Importing all the files
from ofos_payment_management import *
from ofos_validation import *


#User defined function
def display_features_page():

    print("-----------------------------------------------------")
    print("|            ONLINE FOOD ORDERING SYSTEM            |")
    print("-----------------------------------------------------")
    display_features = ("Register(New User / Update profile)", "Restaurants (only for Admin Usage)", "Order Food", "Exit")

    for i,j in enumerate(display_features):
        print(f"{i+1}.{j}")

    return len(display_features)


def display_register_feature_page():

    register_features = ("New User","Existing User(Update Profile)")

    for i,j in enumerate(register_features):
        print(f"{i+1}.{j}")

    return len(register_features)


def display_admin_page():

    admin_page = ("Sign Up(New User)", "Log in(for edit options)")

    for i,j in enumerate(admin_page):
        print(f"{i+1}.{j}")

    return len(admin_page)


def display_admin_features():

    admin_features = ("Add Restaurant", "Update Restaurant", "Delete Restaurant")

    for i,j in enumerate(admin_features):
        print(f"{i+1}.{j}")

    return len(admin_features)


def display_order_food():

    order_features = ("Full Menu", "Filter by restaurant", "Filter by Veg", "Filter by Non veg", "Place Order/View Cart", "Track Oder", "Cancel Order", "Payment's History")
    for i,j in enumerate(order_features):
        print(f"{i+1}.{j}")
    return len(order_features)

   
class Main_module:
    
    #instance method 
    def execute_code(self):

        swiggy_user = Discount_and_offers_management() #object creation
        features_page_flag = 0

        while features_page_flag == 0:            
            list_length = display_features_page()
            name_choice = "Enter your choice"
            choice = Validation.validate_choice(name_choice, list_length)
        
            if choice == 1: # User Purpose
                one_choice_flag = 0
                while one_choice_flag == 0:
                    print("--------------------------------------------")
                    print("|          Only For User Purpose           |")
                    print("--------------------------------------------")
                    reg_list_len = display_register_feature_page()
                    n_choice = "Enter your choice or press ('q' to 'quit')"
                    reg_choice = Validation.validate_quit_choice(n_choice, reg_list_len)
                    if reg_choice == 1:
                        swiggy_user.register()
                    elif reg_choice == 2:
                        swiggy_user.profile_view_update()
                    else:
                        one_choice_flag = 1
                    
            elif choice == 2: # Restaurant purpose
                restaurant_flag = 0
                while restaurant_flag == 0:
                    print("--------------------------------------------")
                    print("|          Only For Admin Purpose          |")
                    print("--------------------------------------------")
                    admin_len = display_admin_page()
                    name_choice = "Enter your choice or press ('q' to 'quit')"
                    admin_choice = Validation.validate_quit_choice(name_choice, admin_len)
                    
                    if admin_choice == 1:
                        swiggy_user.restaurant_admin_register()
                    elif admin_choice == 2:
                        admin_feature_flag = 0
                        while admin_feature_flag == 0:
                            if swiggy_user.restaurant_admin_login():
                                inside_option = 0
                                while inside_option == 0:
                                    print("******************************************")
                                    print("*  Choose the option you want to change  *")
                                    print("******************************************")
                                    choice_len = display_admin_features()
                                    name_choice = "Enter your choice or press ('q' to 'quit')"
                                    admin_login_choice = Validation.validate_quit_choice(name_choice, choice_len)

                                    if admin_login_choice == 1: # add restaurant
                                        inside_option = swiggy_user.add_restaurant()
                                    elif admin_login_choice == 2: # update restaurant
                                        inside_option = swiggy_user.update_restaurant()
                                    elif admin_login_choice == 3: # delete restaurant
                                        inside_option = swiggy_user.delete_restaurant()
                                    else: # quit
                                        admin_feature_flag = 1
                                        inside_option = 1
                            else: # quit
                                admin_feature_flag = 1

                    else: # quit
                        restaurant_flag = 1

            elif choice == 3: # food ordering
                print("Please Log in to continue")
                logged_in_not = swiggy_user.user_login()
                if logged_in_not[0]:
                    print(f"Hello {swiggy_user.user_database[logged_in_not[1]][1].upper()}")
                    order_flag = 0
                    while order_flag == 0:
                        swiggy_user.mail_id = logged_in_not[1]
                        print("******************************************")
                        print("*           Choose the option            *")
                        print("******************************************")
                        order_len = display_order_food()
                        order_choice = "Enter your choice or press ('q' to 'quit')"
                        order_page_choice = Validation.validate_quit_choice(order_choice, order_len)
                        order_item_flag = 0
                        while order_item_flag == 0:

                            if order_page_choice == 1: # Full Menu
                                items_len = swiggy_user.all_items()
                                items_choice = "Enter item no to add cart or press ('q' to 'quit')"
                                item_order_choice = Validation.validate_quit_choice(items_choice, items_len)

                                if str(item_order_choice).isnumeric():
                                        print(swiggy_user.add_item_to_cart(item_order_choice, logged_in_not[1]))
                                else:
                                    order_item_flag = 1

                            elif order_page_choice == 2:# Filter by restaurant
                                order_item_flag = swiggy_user.items_by_restaurant(logged_in_not[1])

                            elif order_page_choice == 3:# Filter by Veg
                                order_item_flag = swiggy_user.add_veg_items(logged_in_not[1])
                                
                            elif order_page_choice == 4:# Filter by Non veg
                                order_item_flag = swiggy_user.add_veg_items(logged_in_not[1], veg=False)
                                
                            elif order_page_choice == 5:# Place Order/View cart
                                order_item_flag = swiggy_user.place_order(logged_in_not[1])
                            
                            elif order_page_choice == 6:# Track Oder
                                order_item_flag = swiggy_user.track_order(logged_in_not[1])
                            
                            elif order_page_choice == 7:# Cancel Order
                                order_item_flag = swiggy_user.cancel_order(logged_in_not[1])

                            elif order_page_choice == 8: # Payment's History
                                order_item_flag = swiggy_user.view_payment_history(logged_in_not[1])
                                
                            else: #Quit
                                order_flag = 1
                                order_item_flag = 1
                                
            else: # Exiting the program 
                features_page_flag = 1
                print("Exiting the program....")
                


obj = Main_module()  # Object Creation/ Object Instantiation
obj.execute_code()   # Calling method using object


