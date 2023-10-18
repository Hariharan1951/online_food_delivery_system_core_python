from ofos_user_management import *
from ofos_restaurant_management import *
from redmail import gmail

# Importing random and datetime module.
import random
import datetime as dt 

delivery_charges_list = [10, 15, 20, 25 , 30, 35, 40, 35, 50]
delivery_timing = list(range(5,11))

def display_edit():

        edit_display = ("Edit cart", "Proceed to Checkout")

        for i, j in enumerate(edit_display):
            print(f"{i+1}.{j}")

        return len(edit_display)


def display_delete():
    
    del_display = ("Delete item", "Delete Quantity")
    for i,j in enumerate(del_display):
        print(f"{i+1}.{j}")

    return len(del_display)


def display_types():

    del_edit = ("Add Cart", "Delete Cart")
    for i,j in enumerate(del_edit):
        print(f"{i+1}.{j}")

    return len(del_edit)


def display_address():

    address_menu = ("Existing address", "New Address")

    for i,j in enumerate(address_menu):
        print(f"{i+1}.{j}")

    return len(address_menu)

    
class Order_management(Restaurant_management, User_management):

    def __init__(self,mail_id = None):
        Restaurant_management.__init__(self)
        User_management.__init__(self)
        if mail_id != None:
            self.__mail_id = mail_id
            self.name = self.user_database[mail_id][1]
        #self.cart = {"hari98ts@gmail.com":[["BIRYANI",2,220.0,"NON VEG","HOTEL BUHARI"],["VEG BIRYANI",3,450.0,"VEG","HOTEL FARUZI"],["GOBI RICE",6,1230.0,"VEG","HOTEL BUHARI"]]} #{"mail_id": [[item, quantity, price,Food type, resturant_name],[item, quantity, price, resturant_name]]}
        #self.restaurants = []
        self.cart = {}
        self.delivery_persons = [("Vignesh","6758768987"), ("Muthu","9873425465"), ("Raj", "8768576457"), ("Magesh","7987564754")]
        self.delivery_timing_details = {} #{mail_id:[["YYYY", "MM", "DD", "HH", "MM", "SS"], delivery_time, (delivery_person_name, delivery_person_ph_no), amount_to_pay]}


    def all_items(self):

        print("--------------------------------------------------------------------------")
        print("|         Item         |   Price   |    Type    |       Restaurant       |")
        print("--------------------------------------------------------------------------")
        index = 1
        for i in self.restaurant_menu_database:
            for item, (price,f_type) in self.restaurant_menu_database[i][2].items():
                print(f"|{index:>3}.{item:<18}|{price:^11}|{f_type:^12}|{self.restaurant_menu_database[i][0]:^24}|")

                index += 1
        print("--------------------------------------------------------------------------")

        return index-1



    @property
    def mail_id(self):
        return self.__mail_id

    @mail_id.setter
    def mail_id(self, mail):
        self.__mail_id = mail


    def add_item_to_cart(self,value,mail_id, restaurant = (0,)):

        index = 1
        if restaurant[0] != 0:
            i= restaurant[1]
            for item, (price, f_type) in self.restaurant_menu_database[i][2].items():
                    if index == value:
                        quantity = Validation.validate_integer_input("Enter quantity")

                        if mail_id not in self.cart:
                            self.cart[mail_id] = [[item, quantity, price*quantity, f_type, self.restaurant_menu_database[i][0]]]
                            return f"{item} added to your cart successfully"
                        else:
                            find = 1
                            length = len(self.cart[mail_id])
                            while find <= length:
                                if item == self.cart[mail_id][find-1][0] and self.restaurant_menu_database[i][0] == self.cart[mail_id][find-1][4]:
                                    self.cart[mail_id][find-1][1] += quantity
                                    self.cart[mail_id][find-1][2] += quantity * price
                                    return f"{item} added to your cart succesfully."
                                else:
                                    find += 1
                            else:
                                self.cart[mail_id].append([item, quantity, price*quantity, f_type, self.restaurant_menu_database[i][0]])
                                return f"{item} added to your cart successfully"
                                
                    index += 1
        else:
            for i in self.restaurant_menu_database:

                for item, (price, f_type) in self.restaurant_menu_database[i][2].items():
                    if index == value:
                        quantity = Validation.validate_integer_input("Enter quantity")

                        if mail_id not in self.cart:
                            self.cart[mail_id] = [[item, quantity, price*quantity, f_type, self.restaurant_menu_database[i][0]]]
                            return f"{item} added to your cart successfully"
                        else:
                            find = 1
                            length = len(self.cart[mail_id])
                            while find <= length:
                                if item == self.cart[mail_id][find-1][0] and self.restaurant_menu_database[i][0] == self.cart[mail_id][find-1][4]:
                                    self.cart[mail_id][find-1][1] += quantity
                                    self.cart[mail_id][find-1][2] += quantity * price
                                    return f"{item} added to your cart succesfully."
                                else:
                                    find += 1
                            else:
                                self.cart[mail_id].append([item, quantity, price*quantity, f_type, self.restaurant_menu_database[i][0]])
                                return f"{item} added to your cart successfully"
                    index += 1
        

    def display_items_restaurant(self, ph_no):

        print("----------------------------------------------")
        print(f"|{self.restaurant_menu_database[ph_no][0]:^44}|")
        print("----------------------------------------------")
        print("|         Item         |   Price   |   Type  |")
        print("----------------------------------------------")        
        index = 1
        for item, (price, f_type) in self.restaurant_menu_database[ph_no][2].items():
                print(f"|{index:>3}.{item:<18}|{price:^11}|{f_type:^9}|")

                index += 1
        print("-----------------------------------------------")
        return index-1


    def items_by_restaurant(self, mail_id):

        hotel_flag = 0
        while hotel_flag == 0:

            print("--------------------------------------------")
            print("|           Choose the Restaurant          |")
            print("--------------------------------------------")
            hotel_len = self.restaurant_list()
            hotel_name = "Enter your choice or press ('q' to 'quit')"
            hotel_choice = Validation.validate_quit_choice(hotel_name, hotel_len)
            if str(hotel_choice).isnumeric():
                self.restaurant_filter_key_add_to_cart(hotel_choice, mail_id)
            else:
                return 1
                
    def restaurant_filter_key_add_to_cart(self, choice, mail_id):
                
        if choice:
            key_find = list(self.restaurant_menu_database.keys())
            for i,j in enumerate(key_find):
                if (choice-1) == i:
                    ph_no = j
                    break
                
            update_flag = 0
            while update_flag == 0:
                len_display = self.display_items_restaurant(ph_no)
                name_choice = "Enter item no. to add to cart or press ('q' to 'quit')"
                update_choice = Validation.validate_quit_choice(name_choice, len_display)

                if str(update_choice).isnumeric():
                    print(self.add_item_to_cart(update_choice, mail_id,(1, ph_no)))
                else:
                    update_flag = 1


    def veg_items(self):

        print("-------------------------------------------------------------")
        print("|                          VEG MENU                         |")
        print("-------------------------------------------------------------")
        print("|         Item         |   Price   |       Restaurant       |")
        print("-------------------------------------------------------------")
        index = 1
        for i in self.restaurant_menu_database:
            for item, (price,f_type) in self.restaurant_menu_database[i][2].items():
                if f_type == "VEG":
                    print(f"|{index:>3}.{item:<18}|{price:^11}|{self.restaurant_menu_database[i][0]:^24}|")
                    index += 1
        print("-------------------------------------------------------------")
        return index-1


    def add_veg_items(self,mail_id, veg=True):

        veg_flag = 0
        while veg_flag == 0:
            if veg:
                f_type_len = self.veg_items()
            else:
                f_type_len = self.non_veg_items()
            name = "Enter item no. to add to cart or press ('q' to 'quit')"
            choice = Validation.validate_quit_choice(name, f_type_len)

            if str(choice).isnumeric():
                index = 1
                for i in self.restaurant_menu_database:
                    for item, (price,f_type) in self.restaurant_menu_database[i][2].items():
                        if veg:
                            if f_type == "VEG":
                                if choice == index:
                                    print(self.add_item_to_cart(choice, mail_id,(1, i)))
                                index += 1
                        else:
                            if f_type == "NON VEG":
                                if choice == index:
                                    print(self.add_item_to_cart(choice, mail_id,(1, i)))
                                index += 1    
            else:
                return 1


    def non_veg_items(self):
        
        print("-------------------------------------------------------------")
        print("|                        NON VEG MENU                       |")
        print("-------------------------------------------------------------")
        print("|         Item         |   Price   |       Restaurant       |")
        print("-------------------------------------------------------------")
        index = 1
        for i in self.restaurant_menu_database:
            for item, (price,f_type) in self.restaurant_menu_database[i][2].items():
                if f_type == "NON VEG":
                    print(f"|{index:>3}.{item:<18}|{price:^11}|{self.restaurant_menu_database[i][0]:^24}|")
                    index += 1
        print("-------------------------------------------------------------")
        return index-1


    def display_cart_items(self, mail_id):

        if self.cart:
                if self.cart.get(mail_id):
                    print("==============================================================================")
                    print(f"|       {self.user_database[mail_id][1]:>30}'s Cart                                |")
                    print("|----------------------------------------------------------------------------|")
                    print("|       Item       | quantity |   Price   |    Type    |       Restaurant    |")
                    print("|============================================================================|")

                    amount = 0
                    index = 1
                    for i in self.cart[mail_id]:
                        print(f"|{index:>3}.{i[0]:<14}|{i[1]:^10}|{i[2]:^11}|{i[3]:^12}|{i[4]:^21}|")
                        amount += i[2]
                        index += 1
                    print("|----------------------------------------------------------------------------|")
                    print(f"|           Total Amount           |             Rs.{amount:<6}                   |")
                    print("==============================================================================")
                else:
                    print("Your cart is empty")
                    return 0
        else:
            print("Your cart is empty")
            return 0

        return len(self.cart[mail_id])
        

    def display_delivery_address(self, mail_id):

        print("Choose delivery address")
        print("-----------------------------------------------------------------------------")
        print("|    D.No    |       Street       |      Area      |    City    |  Pincode  |")
        print("-----------------------------------------------------------------------------")
        for i, j in enumerate(self.user_database[mail_id][3]):
            print(f"|{i+1:>1}.{j[0]:^10}|{j[1]:^20}|{j[2]:^16}|{j[3]:^12}|{j[4]:^11s}|")
                              
        print("-----------------------------------------------------------------------------")
        return len(self.user_database[mail_id][3])
    

    def display_final_billing(self, mail_id, delivery_amount = 0):

        print("==============================================================================")
        print("|                            Customer Invoice                                |")
        print("|----------------------------------------------------------------------------|")
        print("|       Item       | quantity |   Price   |    Type    |       Restaurant    |")
        print("|============================================================================|")

        amount = 0
        index = 1
        for i in self.cart[mail_id]:
            print(f"|{index:>3}.{i[0]:<14}|{i[1]:^10}|{i[2]:^11}|{i[3]:^12}|{i[4]:^21}|")
            amount += i[2]
            index += 1
        print("|----------------------------------------------------------------------------|")
        print(f"|           Amount            |               Rs.{amount:<6}                      |")
        print("|----------------------------------------------------------------------------|")
        total_amount = self.check_discount(amount) # It checks whether the food delivery app give any discounts.
        if amount > total_amount: 
            print(f"|      Discount Amount        |               Rs.{total_amount:<6}                      |")
            print("|----------------------------------------------------------------------------|")
        print(f"|       Delivery Fee          |               Rs.{delivery_amount:<6}                      |")
        print("|----------------------------------------------------------------------------|")
        print(f"|        Total Amount         |               Rs.{int(total_amount)+delivery_amount:<6}                      |")
        print("==============================================================================")
        
        return int(total_amount+delivery_amount)
    

    def delivery_discount_amount(self, mail_id):
        
        delivery_charge = random.choice(delivery_charges_list) # Delivery Charge based on random, not based on address
        amount_to_pay = self.display_final_billing(mail_id, delivery_charge)
        #use if condition to pay after getting the place of address
        pay_flag = 0
        while pay_flag == 0:
            len_pay = 2
            print("Note: Food cancel within 60 sec of order confirmation will get 100% refund.\nYou Can't cancel order after 60 sec.")
            print("Proceed to pay")
            print("1.Yes")
            print("2.No")
            len_choice = Validation.validate_choice("Enter your choice",len_pay)
            if len_choice == 1: # payment procedure
                payment = self.payment_gateway_integration(mail_id, amount_to_pay)
                if payment[0]:
                    print("Order Confirmed") 
                    gmail.username = "hariharant998@gmail.com"  # Notification mail sent to registered mail of customer
                    gmail.password = "ucnk enny kwnk kxsb"
                    gmail.send(subject = "Message from Online Food Delivery App",
                               receivers = [mail_id],
                               html = "<h1>Your order is confirmed!</h1>")
                    print(f"Order confirmation sent to {mail_id} mail.")
                    if payment[1]:
                        print(f"Your total amount to be paid during delivery time is Rs.{amount_to_pay}")
                    order_time = dt.datetime.now().strftime("%Y,%m,%d,%H,%M,%S")
                    delivery_time = random.choice(delivery_timing)
                    print(f"Your order will reach you in {delivery_time} minutes.")
                    self.delivery_timing_details[mail_id] = [order_time.split(","), delivery_time, random.choice(self.delivery_persons), amount_to_pay] 
                    break
                else:
                    print("Payment Unsuccesful")
                    
                    
            else: # payment loop exit
                pay_flag = 1


    
    def place_order(self,mail_id): #{"mail_id": [[item, quantity, price, Food type, resturant_name],[item, quantity, price, resturant_name]]}

        cart_flag = 0
        while cart_flag == 0:
            self.display_cart_items(mail_id)
            length = display_edit()
            name = "Enter your choice or press ('q' to 'quit')"
            choice = Validation.validate_quit_choice(name, length)
        
            if str(choice).isnumeric():
                if choice == 1: # Edit cart
                    edit_flag = 0
                    while edit_flag == 0:
                        dis_len = display_types()
                        dis_name = "Enter your choice or press ('q' to 'quit')"
                        dis_choice = Validation.validate_quit_choice(dis_name, dis_len)
                        if str(dis_choice).isnumeric():
                            if dis_choice == 1: # Add cart
                                return 1 # order_item_flag
                            else: #delete cart
                                del_flag = 0
                                while del_flag == 0:
                                    del_len = display_delete()
                                    del_name = "Enter your choice or press ('q' to 'quit')"
                                    del_choice = Validation.validate_quit_choice(del_name, del_len)

                                    if str(del_choice).isnumeric():
                                        if del_choice == 1: # Delete item
                                            del_item_flag = 0
                                            while del_item_flag == 0:
                                                    del_item_len = self.display_cart_items(mail_id)
                                                    if del_item_len != 0:
                                                        del_item_choice = Validation.validate_quit_choice("Enter item no. to delete in cart or press ('q' to 'quit')", del_item_len)
                                                        if str(del_item_choice).isnumeric():
                                                            removed_item = self.cart[mail_id].pop(del_item_choice-1)
                                                            print(f"{removed_item[0]} removed from your cart")
                                                        else:
                                                            del_item_flag = 1
                                                    else:
                                                        del_item_flag = 1
                                                        edit_flag = 1
                                        else: # Delete quantity
                                            del_qty_flag = 0
                                            while del_qty_flag == 0:
                                                del_qty_len = self.display_cart_items(mail_id)
                                                if del_qty_len != 0:
                                                    del_qty_choice = Validation.validate_quit_choice("Enter item no. to delete quantity in cart or press ('q' to 'quit')", del_qty_len)

                                                    if str(del_qty_choice).isnumeric():
                                                        
                                                        while True:
                                                            quantity = Validation.validate_integer_input(f"Enter {self.cart[mail_id][del_qty_choice-1][0]} quantity to delete")
                                                            if quantity < self.cart[mail_id][del_qty_choice-1][1]:
                                                                """
                                                                This set of code will get the item's 1 quantity price from restaurant_menu_database and update it to self.cart.
                                                                But it will raise error if restaurant admin delete the particular item after adding to the user/customer's cart.
                                                                
                                                                self.cart[mail_id][del_qty_choice-1][1] -= quantity
                                                                for key, value in self.restaurant_menu_database.items():
                                                                    if value[0] == self.cart[mail_id][del_qty_choice-1][4]:
                                                                        for item_key, item_value in value[2].items():
                                                                            if item_key == self.cart[mail_id][del_qty_choice-1][0]:
                                                                                self.cart[mail_id][del_qty_choice-1][2] = self.cart[mail_id][del_qty_choice-1][1]*quantity
                                                                                print("Updated Successfully")
                                                                                break  # for loop
                                                                break # while loop
                                                                """
                                                                
                                                                # This code will get the price of single unit of item in self.cart and it will not get any error even the item is removed by restaurant admin.
                                                                one_qty_price = self.cart[mail_id][del_qty_choice-1][2] / self.cart[mail_id][del_qty_choice-1][1]
                                                                self.cart[mail_id][del_qty_choice-1][1] -= quantity
                                                                self.cart[mail_id][del_qty_choice-1][2] = self.cart[mail_id][del_qty_choice-1][1] * one_qty_price
                                                                print("Updated Successfully")
                                                                break
                                                                         
                                                            elif quantity == self.cart[mail_id][del_qty_choice-1][1]:
                                                                removed = self.cart[mail_id].pop(del_qty_choice-1)
                                                                print("Item removed from your cart")
                                                                break
                                                            else:
                                                                print(f"{self.cart[mail_id][del_qty_choice-1][0]} have only {self.cart[mail_id][del_qty_choice-1][1]} quantity in your cart")

                                                    else:
                                                        del_qty_flag = 1
                                                else:
                                                    del_qty_flag = 1
                                    else:
                                        del_flag = 1
                        else:
                            edit_flag = 1
                else: # check out

                    if self.cart.get(mail_id):
                        address_flag = 0
                        while address_flag == 0:
                            payment_proceed = 0
                            
                            address_len= display_address()
                            address_choice = Validation.validate_quit_choice("Enter your choice or press ('q' to 'quit')", address_len)
                            if str(address_choice).isnumeric():
                                if address_choice == 1: #display Existing Address
                                    exist_choice_flag = 0
                                    while exist_choice_flag == 0:
                                        exist_choice_len = self.display_delivery_address(mail_id)
                                        exist_choice = Validation.validate_quit_choice("Enter your choice or press ('q' to 'quit')", exist_choice_len)
                                        
                                        if str(exist_choice).isnumeric():
                                            exist_choice_flag = 1
                                            self.delivery_discount_amount(mail_id)
                                            return 1 # order_item_flag

                                        else:
                                            exist_choice_flag = 1
                                    
                                            
                            
                                else: #new address getting
                                    new_address = Validation.validate_address("Enter your new address")
                                    new_address_flag = 0
                                    while new_address_flag == 0:
                                        len_new_address = 2
                                        print("Save this address for our future use?")
                                        print("1.Yes")
                                        print("2.No")
                                        new_add_choice = Validation.validate_choice("Enter your choice",len_new_address)
                                        if new_add_choice == 1: # Saving address to self.user_database
                                            self.user_database[mail_id][3].append(new_address)
                                            print("Successfully Saved")
                                            new_address_flag = 1
                                        else: # 2.No option
                                            print("It's not saved for future use")
                                            new_address_flag = 1
                                    self.delivery_discount_amount(mail_id)
                                    return 1# order_item_flag
                            

                            else:
                                address_flag = 1
                    else:
                        print("Please add item to cart to move further")
                        
            else:
                cart_flag = 1
                return 1 # (order_item_flag,)


    def difference_finder(self,mail):

        otl = self.delivery_timing_details[mail][0] # olt = Ordered time list
        ordered_time = dt.datetime(int(otl[0]), int(otl[1]), int(otl[2]), int(otl[3]), int(otl[4]), int(otl[5]))
        difference = int(abs((dt.datetime.now() - ordered_time).total_seconds()))
        return difference
    

    def track_order(self, mail):

        if self.delivery_timing_details:
            if self.delivery_timing_details.get(mail):
                print(f"Your delivery person Name: {self.delivery_timing_details[mail][2][0]}")
                print(f"Contact Number           : {self.delivery_timing_details[mail][2][1]}")
                track_flag = 0
                while track_flag == 0:
                    choice = Validation.validate_quit()
                    if choice == "q":
                        return 1 # order_item_flag
                    else:
                        red_time = self.delivery_timing_details[mail][1]
                        difference = self.difference_finder(mail)
                        if difference >= 60:
                            
                            live_track = (self.delivery_timing_details[mail][1] * 60) // 4
                            if difference <= live_track:
                                print(f"Your order will reach you in {((red_time*60)-live_track)//60} minute(s).")
                                print("Order Status: Your order is getting prepared.")
                            elif live_track < difference <= live_track*2:
                                print(f"Your order will reach you in {((red_time*60)-(live_track*2))//60} minute(s).")
                                print("Order Status: Your order is being picked up.")
                            elif live_track*2 < difference <= live_track*4:
                                print(f"Your order will reach you in {((red_time*60)-(live_track*3))//60} minute(s).")
                                print("Order Status: Your order is on the way.")
                            else:
                                if self.payment_history.get(mail):
                                    self.payment_history[mail].append([self.delivery_timing_details[mail][3], self.delivery_timing_details[mail][0], self.cart[mail]])
                                else:
                                    self.payment_history[mail] = [[self.delivery_timing_details[mail][3], self.delivery_timing_details[mail][0],self.cart[mail]]]
                                gmail.username = "hariharant998@gmail.com"    # Notification mail sent to registered mail of customer
                                gmail.password = "ucnk enny kwnk kxsb"
                                gmail.send(subject = "Thank you for Choosing Online Food Delivery App",
                                           receivers = [mail],
                                           html = "<h1>Your Order is Delivered successfully.</h1>")
                                print(f"Order confirmation sent to {mail} mail.")
                                self.cart.pop(mail)
                                self.delivery_timing_details.pop(mail)
                                print("Order Status: Delivered")
                                return 1
                        else:
                            print(f"Your order will reach you in {self.delivery_timing_details[mail][1]} minute(s).")
                            print("Order Status: We are working on your order.")
                            
            else:
                print("There is no current order to track")
                return 1
        else:
            print("There is no current order to track")
            return 1

            
    def cancel_order(self, mail): # before packing

        cancel_order = 0
        while cancel_order == 0:
            if self.delivery_timing_details:
                if self.delivery_timing_details.get(mail):
                    print("Would you like to cancel Your order?")
                    print("1. Yes")
                    print("2. No")
                    choice = Validation.validate_choice("Enter your choice",2)
                    if choice == 1:
                        difference = self.difference_finder(mail)
                        if difference <= 60:
                            print("Oreder Cancelled")
                            print("You'll get 100% refund back")
                            gmail.username = "hariharant998@gmail.com"      # Notification mail sent to registered mail of customer
                            gmail.password = "ucnk enny kwnk kxsb"
                            gmail.send(subject = "Message from Online Food Delivery App",
                                       receivers = [mail],
                                       html = "<h1>Your order is cancelled!!</h1>")
                            print(f"Order cancellation notification is sent to {mail} mail.")
                            self.delivery_timing_details.pop(mail)
                            return 1
                        else:
                            print("You are not allowed to cancel the order")
                            live_track = (self.delivery_timing_details[mail][1] * 60) // 4
                            if difference <= live_track:
                                print("Because, Your order is getting prepared.")
                            elif live_track < difference <= live_track*2:
                                print("Because, Your order is being picked up.")
                            elif live_track*2 < difference <= live_track*4:
                                print("Because, Your order is on the way.")
                            else:
                                print("Because, Your order is delivered")
                            return 1
                    else:
                        return 1
                else:
                    print("There is no current order to cancel")
                    return 1
            else:
                print("There is no current order to cancel")
                return 1

