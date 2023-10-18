from ofos_validation import *
from ofos_user_management import *
import maskpass

def display_update_features():

    update_features = ("Add new item", "Update Existing item")

    for i, j in enumerate(update_features):
        print(f"{i+1}.{j}")
    return len(update_features)


# Parent Class
class Restaurant_management:

    def __init__(self):
        super().__init__()
        self.restaurant_admin_database = {"hari98ts@gmail.com": ["Hari@1234", "Hari"]} # single admin is enough and it can be inbuilt. #{mail_id:[password, name]}
        self.restaurant_menu_database = {"8526686604":["HOTEL BUHARI",["54/55", "Varadhapuram 2nd street", "Kotturpuram", "Chennai", "600044"],{"BIRYANI":[200.0, "NON VEG"],"VEG BIRYANI":[150.0, "VEG"],"VEG RICE":[135.0, "VEG"]}],
                                        "9876543234": ["KFC",
                                                       ["3A", "Gandhi street", "Anna nagar", "Chennai", "635307"],
                                                      {"VEG BURGER": [125.0, "VEG"],
                                                       "CHICKEN BURGER": [165.0, "NON VEG"],
                                                       "BUCKET CHICKEN": [700.0, "NON VEG"],
                                                       "HOT WINGS": [130.0, "NON VEG"]}],
                                        "7846573908": ["SARAVANA BHAVAN",
                                                      ["12B", "Naidu Street", "Tambaram", "Chennai", "634465"],
                                                      {"PANNER RICE": [100.0, "VEG"],
                                                       "PAROTTA(2 NOS)": [70.0, "VEG"],
                                                       "CHAPPATHI(2 NOS)": [65.0, "VEG"],
                                                       "PONGAL": [80.0, "VEG"],
                                                       "SAMBAR IDLI": [60.0, "VEG"]}],
                                        "9842648094": ["HOTEL FARUZI",
                                                      ["135/3", "Mg Road", "Velacherry", "Chennai", "657687"],
                                                      {"CHICKEN RICE": [160.0, "NON VEG"],
                                                       "VEG RICE": [130.0, "VEG"],
                                                       "GOBI RICE": [140.0, "VEG"],
                                                       "HALF GRILL": [280.0, "NON VEG"],
                                                       "FULL GRILL": [450.0, "NON VEG"]}],
                                        "6785697890": ["LAKSHMI BHAVAN",
                                                      ["13V/2", "AB street", "Porur", "Chennai", "668796"],
                                                      {"DOSA(2 NOS)": [60.0, "VEG"],
                                                       "IDLI(4 NOS)": [35.0, "VEG"],
                                                       "MEALS": [80.0, "VEG"],
                                                       "PONGAL": [60.0, "VEG"],
                                                       "MEALS": [110.0, "NON VEG"],
                                                       "POORI(2 NOS)": [35.0, "VEG"],
                                                       "VADA(1 NOS)": [10.0, "VEG"],}]}#{ph_no:[Hotel name, address, [{item1:[price1,Veg], item1:[price1,veg]}]]

    def restaurant_admin_register(self):

        print("--------------------------------------------")
        print("|      Create Account For Admin Usage      |")
        print("--------------------------------------------")

        name_string = "Enter Name"
        name = Validation.validate_name(name_string)

        mail_id = Validation.validate_mail()
        if mail_id not in self.restaurant_admin_database:
            password1_string = "Enter your Password"
            password1 = Validation.validate_password(password1_string)
            password_check_flag = 0
            while password_check_flag == 0:
                password2_string = "Re Enter your Password"
                password2 = Validation.validate_password(password2_string)
                if password1 == password2:
                    password_check_flag = 1
                    print("Registration Successful!!")
                else:
                    print("Password and Confirm Password are not matching properly")
            
            self.restaurant_admin_database[mail_id] = [password2, name]
        
        else:
            print(f"Hello {name}, Your account is already registerd.")
    
    
    def restaurant_admin_login(self):

        print("++++++++++++++++++++++++++++++++")
        print("|       Admin Login Page       |")
        print("++++++++++++++++++++++++++++++++")
        mail_id_flag = 1
        while mail_id_flag <= 3:
            mail_id = Validation.validate_mail()
            if mail_id in self.restaurant_admin_database:
                passw_flag = 1
                while passw_flag <= 3:
                    password1_string = "Enter your Password"
                    password1 = Validation.validate_password(password1_string)
                    #password1 = maskpass.askpass() # ------> Use anyone.(Not work with python IDLE)
                    #password1 = maskpass.advpass() # ------->(Not work with python IDLE)
                    if password1 == self.restaurant_admin_database[mail_id][0]:
                        print("Login Success!!")
                        return True
                    else:
                        print("Your given password is wrong. TRY AGAIN!!!")
                        if not(passw_flag == 3):
                            print(f"You have {3-passw_flag} attempt(s) remaining")
                        passw_flag += 1
                else:
                    print("You exceed the limit")
                    return False
                    
            else:
                print("Entered mail id is wrong")
                if not(mail_id_flag == 3):
                    print(f"You have {3-mail_id_flag} attempt(s) remaining")
                mail_id_flag += 1
        else:
            print("You are not registerd as an admin account. SIGNUP First!!!") 
            return False

            
    def add_restaurant(self):

            name_string = "Enter Restaurant Name"
            name = Validation.validate_name(name_string).upper()

            ph_no = Validation.validate_ph_no()

            
            if ph_no not in self.restaurant_menu_database:
                address_string = "Enter Restaurant Address"
                address = Validation.validate_address(address_string)
                self.restaurant_menu_database[ph_no] = [name, address,{}]
                
                add_menu_flag = 0
                while add_menu_flag == 0:
                    menu_choice = Validation.validate_add_menu()
                    if menu_choice == 1:
                        self.add_menu(ph_no)
                    else:
                        print("Exiting the menu adding page...") 
                        add_menu_flag = 1
                        return 0
                    
            else:
                print("This restaurant is already registered")
                print("If you want to update the menu use 'update restaurant' option") 
                return 0
            

    def add_menu(self,ph_no):

        print("++++++++++++++++++++++++++++++++++")
        print("+        Menu Adding Page        +")
        print("++++++++++++++++++++++++++++++++++")
        
        name_string = "Enter item name"
        name = Validation.validate_item_name(name_string)

        

        if name not in self.restaurant_menu_database[ph_no][2]:

            item_price = f"Enter {name} price"
            price = Validation.validate_float_input(item_price)

            food_type = Validation.validate_veg("Choose food type")
            
            self.restaurant_menu_database[ph_no][2][name] = [price, food_type]
            print(f"Success!! {name} added to the menu with Rs. {price} ")

        else:
            print(f"The {name} is already exists") 
        

    
    def restaurant_list(self):
        
        item = 0
        for i in self.restaurant_menu_database:
            print(f"*{item+1:>14}.{self.restaurant_menu_database[i][0]:<27}*")
            item += 1
        print("--------------------------------------------")

        return len(self.restaurant_menu_database)


    def restaurant_menu_list(self,ph_no):
        
        item = 0
        for key, (value, f_type) in self.restaurant_menu_database[ph_no][2].items():
            print(f"|  {item+1}.{key:<16}|{value:^11}|{f_type:^9}|")
            item += 1
        print("--------------------------------------------")

        return len(self.restaurant_menu_database[ph_no][2])


    def delete_restaurant_menu(self):

        delete_menu = ("Delete restaurant","Delete item")

        print("******************************************")
        print("*  Choose the option you want to delete  *")
        print("******************************************")

        for i, j in enumerate(delete_menu):
            print(f"{i+1}.{j}")

        return len(delete_menu)
            
            
    def update_restaurant(self):

        hotel_flag = 0
        while hotel_flag == 0:

            print("--------------------------------------------")
            print("| Choose the Restaurant you want to change |")
            print("--------------------------------------------")
            hotel_len = self.restaurant_list()
            hotel_name = "Enter your choice or press ('q' to 'quit')"
            hotel_choice = Validation.validate_quit_choice(hotel_name, hotel_len)
        
            
            if str(hotel_choice).isnumeric():
                if hotel_choice <= hotel_len:
                    key_find = list(self.restaurant_menu_database.keys())
                    for i,j in enumerate(key_find):
                        if (hotel_choice-1) == i:
                            ph_no = j
                            break
                        
                    update_flag = 0
                    while update_flag == 0:
                        print("******************************************")
                        print("*  Choose the option you want to change  *")
                        print("******************************************")
                        len_display = display_update_features()
                        name_choice = "Enter your choice or press ('q' to 'quit')"
                        update_choice = Validation.validate_quit_choice(name_choice, len_display)

                        if update_choice == 1: # Add new item
                            name_string = "Enter item name"
                            name = Validation.validate_item_name(name_string)
                            if name not in self.restaurant_menu_database[ph_no][2]:
                                item_price = f"Enter {name} price"
                                price = Validation.validate_float_input(item_price)
                                food_type = Validation.validate_veg("Choose food type")
                                self.restaurant_menu_database[ph_no][2][name] = [price, food_type]
                                print(f"Success!! {name} added to the menu with Rs. {price} ")
                            else:
                                print(f"{name} already exists in this restaurant. To change the price use 'Update Existing Item' menu")
                                
                        elif update_choice == 2: # Update Existing item
                            
                            print("--------------------------------------------")
                            print(f"|{self.restaurant_menu_database[ph_no][0]:^42}|")
                            print("--------------------------------------------")
                            print("|    Choose the item you want to change    |")
                            print("--------------------------------------------")
                            print("|        Item        |   Price   |   Type  |")
                            print("--------------------------------------------")
                            upd_len = self.restaurant_menu_list(ph_no)
                            upd_choice = "Enter your choice or press ('q' to 'quit')"
                            upd_in_choice = Validation.validate_quit_choice(upd_choice, upd_len)
                            if str(upd_in_choice).isnumeric():
                                if upd_in_choice <= upd_len:
                                    key_find_upd = list(self.restaurant_menu_database[ph_no][2].keys())
                                    for i,j in enumerate(key_find_upd):
                                        if (upd_in_choice-1) == i:
                                            item_key = j
                                            break
                                    item_price = f"Enter {item_key} price"
                                    price = Validation.validate_float_input(item_price)
                                    food_type = Validation.validate_veg("Choose food type")
                                    self.restaurant_menu_database[ph_no][2][item_key] = [price, food_type]
                                    print(f"Success!! {item_key} Updated to the menu with Rs. {price} ")
                            else:
                                return 0
                               
                        else:
                            update_flag = 1      
                else:
                    print("Invalid Input!!")
            else:
                return 0  



    @staticmethod
    def confirmation():
        options = ("Yes", "No")
        print("Are you confirm to delete?")

        for i,j in enumerate(options):
            print(f"{i+1}.{j}")

        return len(options)

    

    def delete_restaurant(self):

        delete_restaurant_flag = 0
        while delete_restaurant_flag == 0:
            choice_len = self.delete_restaurant_menu()
            name_choice = "Enter your choice or press ('q' to 'quit')"
            admin_del_choice = Validation.validate_quit_choice(name_choice, choice_len)


            if admin_del_choice == 1: # Delete Restaurant
                del_res_flag = 0
                while del_res_flag == 0:
                    print("--------------------------------------------")
                    print("| Choose the Restaurant you want to delete |")
                    print("--------------------------------------------")
                    del_len = self.restaurant_list()
                    del_name = "Enter your choice or press ('q' to 'quit')"
                    del_choice = Validation.validate_quit_choice(del_name, del_len)

                    if str(del_choice).isnumeric():
                        if del_choice <= del_len:
                            del_key_find = list(self.restaurant_menu_database.keys())
                            for i, j in enumerate(del_key_find):
                                if (del_choice-1) == i:
                                    key = j
                                    break
                        len_value = Restaurant_management.confirmation()
                        name_string = "Enter your choice"
                        value = Validation.validate_choice(name_string,len_value)
                        if value == 1:
                            res_name = self.restaurant_menu_database.pop(key)
                            print(f"{res_name[0]} is deleted")
                        else:
                            print("This restaurant does not got any changes")
                            
                    else:
                        del_res_flag = 1

                    
                    

            elif admin_del_choice == 2: #Delete Item
                res_lis_flag = 0
                while res_lis_flag == 0:
                    
                    print("--------------------------------------------")
                    print("|          Choose the Restaurant           |")
                    print("--------------------------------------------")
                    del_it_len = self.restaurant_list()
                    del_it_name = "Enter your choice or press ('q' to 'quit')"
                    del_it_choice = Validation.validate_quit_choice(del_it_name, del_it_len)

                    if str(del_it_choice).isnumeric():
                        if del_it_choice <= del_it_len:
                            del_it_key_find = list(self.restaurant_menu_database.keys())
                            for i, j in enumerate(del_it_key_find):
                                if (del_it_choice-1) == i:
                                    del_it_key = j
                                    break
                                
                        del_item_flag = 0
                        while del_item_flag == 0:
                            print("--------------------------------------------")
                            print(f"|{self.restaurant_menu_database[del_it_key][0]:^42}|")
                            print("--------------------------------------------")
                            print("|    Choose the item you want to delete    |")
                            print("--------------------------------------------")
                            print("|        Item        |   Price   |   Type  |")
                            print("--------------------------------------------")
                            upd_len = self.restaurant_menu_list(del_it_key)
                            del_choice = "Enter your choice or press ('q' to 'quit')"
                            del_in_choice = Validation.validate_quit_choice(del_choice, upd_len)
                            if str(del_in_choice).isnumeric():
                                if del_in_choice <= upd_len:
                                    key_find_del = list(self.restaurant_menu_database[del_it_key][2].keys())
                                    for i,j in enumerate(key_find_del):
                                        if (del_in_choice-1) == i:
                                            item_key = j
                                            break
                                    delIt_value = Restaurant_management.confirmation()
                                    name_del_it_string = "Enter your choice"
                                    del_it_value = Validation.validate_choice(name_del_it_string,delIt_value)
                                    if del_it_value == 1:
                                        res_name = self.restaurant_menu_database[del_it_key][2].pop(item_key)
                                        print(f"Successfully deleted")
                                    else:
                                        print("This restaurant does not got any item changes")
                                        del_item_flag = 1
                            else:
                                del_item_flag = 1
                    else:
                        res_lis_flag = 1
            else:
                delete_restaurant_flag = 1
                return 0
