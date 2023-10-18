import re # Importing RegEx module to validate the given inputs.
import maskpass # To make the password asterisk while entering the password
 

#Class  Validation - To validate all the user input.
class Validation:

    @staticmethod
    def validate_choice(name, length):

        while True:
            try:
                choice = input(f"{name}: ")
                if 1 <= len(choice) <= 2:
                    if choice.isnumeric():
                        if 1 <= int(choice) <= length:
                            return int(choice)
                        else:
                            raise Exception(f"The given option start from 1 and must not exceed {length}")
                    else:
                        raise Exception("The choice must be numeric")
                else:
                    raise Exception("The length of the character must b/w 1 to 2")
            except Exception as e:
                print(e)


    @staticmethod
    def validate_quit():

        while True:
            try:
                choice = input("Press Enter to view live tracking or press ('q' to quit): ").lower()
                if 0 <= len(choice) <= 1:
                    if choice == "q" or choice == "":
                        return choice
                    else:
                        raise Exception(f"It accepts only 'q' or empty string")
                else:
                    raise Exception("The length of the character 0 or 1")
            except Exception as e:
                print(e)

                
    @staticmethod
    def validate_quit_choice(name, length):

        while True:
            try:
                choice = input(f"{name}: ").lower()
                if 1 <= len(choice) <= 2:
                    if choice.isalnum():
                        if choice.isnumeric():
                            if 1 <= int(choice) <= length:
                                return int(choice)
                            else:
                                raise Exception(f"The given option start from 1 and must not exceed {length}")
                        else:
                            if choice == "q":
                                return choice
                            else:
                                raise Exception("It accepts only 'q'")
                    else:
                        raise Exception("The choice must be numeric or 'q' character")
                else:
                    raise Exception("The length of the character must b/w 1 to 2")
            except Exception as e:
                print(e)


    @staticmethod
    def validate_quit_res_choice(name, length):

        while True:
            try:
                choice = input(f"{name}: ").lower()
                if 1 <= len(choice) <= 2:
                    if choice.isalnum():
                        if choice.isnumeric():
                            if 1 <= int(choice) <= length:
                                return int(choice)
                            else:
                                raise Exception(f"The given option start from 1 and must not exceed {length}")
                        else:
                            if choice == "q" or choice == "h":
                                return choice
                            else:
                                raise Exception("It accepts only 'q' or 'h'")
                    else:
                        raise Exception("The choice must be numeric or 'q' character")
                else:
                    raise Exception("The length of the character must b/w 1 to 2")
            except Exception as e:
                print(e)


    @staticmethod
    def validate_mail():

        while True:
            try:
                mail_id = input("Enter your mail id: ")
                if 1 <= len(mail_id) <= 25:
                    if not(re.findall("\.\.",mail_id)):
                        if not(re.findall("^\.",mail_id)):
                            if not(re.findall("\.@",mail_id)):
                                pattern_1 = "^[0-9A-Za-z\.]+@[a-zA-z]+[\.]com$"
                                pattern_2 = "^[0-9A-Za-z\.]+@[a-zA-z]+[\.]in$"
                                if re.match(pattern_1,mail_id) or re.match(pattern_2, mail_id) :
                                    return mail_id
                                else:
                                    raise Exception("Mail id does not contain spaces and in (username@domain.com/in) format.")
                            else:
                                raise Exception("Last character of username must be ascii characters") 
                        else:
                            raise Exception("The mail id does not start with period(.)")
                    else:
                        raise Exception("The mail id does not have consecutive periods(.)")
                else:
                    raise Exception("The length of mail id should b/w 1 to 25 characters")
            except Exception as e:
                print(e)


    @staticmethod
    def validate_password(name): # password and confirm password are checked.

        while True:
            try:
                password = input(f"{name}: ")
                #password = maskpass.advpass() # ------->(Not work with python IDLE)
                if 6 <= len(password) <= 15:
                    if re.findall("[A-Z]",password):
                        if re.findall("[a-z]",password):
                            if re.findall("[0-9]",password):
                                if re.findall("[\@\!\#\$\_]",password):
                                    if re.match("^[A-Za-z0-9\@\!\#\$\_]",password):
                                        return password
                                    else:
                                        raise Exception("Invalid password")
                                else:
                                    raise Exception("Atleast any 1 special character is mandatory and Only(! @ # $ _) special characters are allowed")
                            else:
                                raise Exception("Atleast 1 numeric(0-9) is mandatory")
                        else:
                            raise Exception("Atleast 1 Lowercase letter is mandatory")
                    else:
                        raise Exception("Atleast 1 Uppercase letter is mandatory")
                else:
                    raise Exception("The length of password should be 6 to 15 characters")
            except Exception as e:
                    print(e)

                
    @staticmethod
    def validate_name(name_given): #validation for name, restaurant name

        while True:
            try:
                name = input(f"{name_given}: ").capitalize()
                if 1 <= len(name) <= 20:
                    if name.replace(" ","").isalpha():
                        if re.match("^[a-zA-Z]+[\s]?[a-zA-Z]*[\s]?[a-zA-Z]*$",name):
                            return name
                        else:
                            raise Exception("The name contains extra white spaces.")
                    else:
                        raise Exception("The name must be string and does not contain period(.)")
                else:
                    raise Exception("The length should be 1 to 15 characters")
            except Exception as e:
                print(e)


    @staticmethod
    def validate_ph_no():

        while True:
            try:
                ph_no = input("Enter your phone number: ")
                if len(ph_no) == 10:
                    if ph_no.isnumeric():
                        if re.match("^[6-9][0-9]{9}",ph_no):
                            if ph_no[0:5:1] != ph_no[9:4:-1]:
                                return ph_no
                            else:
                                raise Exception("The phone number must not be same numbers")
                        else:
                            raise Exception("The phone number must start with 6/7/8/9")
                    else:
                        raise Exception("The phone number must be numberic")
                else:
                    raise Exception("The length of phone number should be 10 characters")
            except Exception as e:
                print(e)

        
    @staticmethod
    def validate_float_input(name):

        while True:
            try:
                price = input(f"{name}: ")
                if price.replace(".","").isnumeric():
                    if 1 <= float(price) <= 1000:
                        return float(price)
                    else:
                        raise Exception("The value must b/w 1 to 1000")
                else:
                    raise Exception("The value must be numeric or float")
            except Exception as e:
                print(e)


    """
    @staticmethod
    def validate_pay_amount():

        while True:
            try:
                price = input(f"Enter Amount: ")
                if price.replace(".","").isnumeric():
                    if 1 <= float(price) <= 10000:
                        return float(price)
                    else:
                        raise Exception("The value must b/w 1 to 10000")
                else:
                    raise Exception("The value must be numeric or float")
            except Exception as e:
                print(e)
    """

    
    @staticmethod
    def validate_item_name(name_given):

        while True:
            try:
                name = input(f"{name_given}: ").upper()
                if 1 <= len(name) <= 20:
                    if not(name.isnumeric()):
                        return name
                    else:
                        raise Exception("The name should not be numeric")
                else:
                    raise Exception("The length should be 1 to 15 characters")
            except Exception as e:
                print(e)


    @staticmethod
    def validate_integer_input(name):

        while True:
            try:
                int_input = input(f"{name}: ")
                if int_input.isnumeric():
                    if 1 <= int(int_input) <= 10:
                        return int(int_input)
                    else:
                        raise Exception("The value must b/w 1 to 10")
                else:
                    raise Exception("The value must be integer")
            except Exception as e:
                print(e)


    @staticmethod
    def validate_address(name): #restaurant address and customer address

        address_storage = []   # [door_no, street, area, city, pincode]
        print(f"{name}")
        while True:
            door_no_flag = 0
            while door_no_flag == 0:
                try:
                    door_no = input("Enter door no: ")
                    if 1 <= len(door_no) <= 6:
                        if door_no.replace("/","").isalnum():
                            if re.match("^[A-Za-z0-9]+[/]?[0-9A-Za-z]*$",door_no):
                                door_no_flag = 1
                                address_storage.append(door_no)
                            else:
                                raise Exception("The door number is invalid")
                        else:
                            raise Exception("The door number contains only integers,characters and /")
                    else:
                        raise Exception("The door number allows 1 to 6 characters")
                except Exception as e:
                    print(e)

            street_flag = 0
            while street_flag == 0:
                try:
                    street = input("Enter the street: ").capitalize()
                    if 3 <= len(street) <= 25:
                        if street.replace(" ","").isalnum():
                            if re.match("^[0-9A-Za-z\s]+$", street):
                                street_flag = 1
                                address_storage.extend([street])
                            else:
                                raise Exception("Invalid street name!!!!")
                        else:
                            raise Exception("The street name contains only characters,integers and white space")
                    else:
                        raise Exception("The length should b/w 3 to 25 characters") 
                except Exception as e:
                    print(e)

            area_flag = 0
            while area_flag == 0:
                try:
                    area = input("Enter your area: ").capitalize()
                    if 3 <= len(area) <= 20:
                        if area.replace(" ","").isalpha():
                            if re.match("^[a-zA-Z]+[\s]?[a-zA-Z]*[\s]?[a-zA-Z]*$",area):
                                area_flag = 1
                                address_storage.extend([area])
                            else:
                                raise Exception("The address contains extra white spaces.")
                        else:
                            raise Exception("The address must be string and does not contain period(.)")
                    else:
                        raise Exception("The length should be 3 to 15 characters")
                except Exception as e:
                    print(e)

            city_flag = 0
            while city_flag == 0:
                try:
                    city = input("Enter your city: ").capitalize()
                    if 3 <= len(city) <= 20:
                        if city.replace(" ","").isalpha():
                            if re.match("^[a-zA-Z]+[\s]?[a-zA-Z]*[\s]?[a-zA-Z]*$",city):
                                city_flag = 1
                                address_storage.extend([city])
                            else:
                                raise Exception("The city contains extra white spaces.")
                        else:
                            raise Exception("The city must be string and does not contain period(.)")
                    else:
                        raise Exception("The length should be 3 to 15 characters")
                except Exception as e:
                    print(e)


            pin_code_flag = 0
            while pin_code_flag == 0:
                try:
                    pin_code = input("Enter the Pincode: ")
                    if len(pin_code) == 6:
                        if pin_code.isnumeric():
                            if re.match("^[6][0-9]{5}$",pin_code):
                                pin_code_flag = 1
                                address_storage.extend([pin_code])
                            else:
                                raise Exception("The pincode must start with 6")
                        else:
                            raise Exception("The pincode must be numeric")
                    else:
                        raise Exception("The pincode contains only 6 digits")
                except Exception as e:
                    print(e)

            
            return address_storage


    @staticmethod
    def validate_upi_id():

        while True:
            try:
                upi_id = input("Enter your upi id: ")
                if 8 <= len(upi_id) <= 20:
                    if re.match("^[0-9A-Za-z]+[@][a-z]{2,8}$",upi_id):
                        return upi_id
                    else:
                        raise Exception("UPI id must end with [@ok{bank name} or @{bank name}] format")
                else:
                    raise Exception("The length should b/w 8 to 20 characters")
            except Exception as e:
                print(e)


    @staticmethod
    def validate_card(card_type): #debit/credit card

        card_details = [] #[card_number, card_holder_name, expiry_date, cvv]
        while True:
            card_no_flag = 0
            while card_no_flag == 0:
                try:
                    card_no = input(f"Enter the {card_type} Card no: ")
                    if card_no.isnumeric():
                        if len(card_no) == 16:
                            if re.match("^[^1-3][0-9]{15}$",card_no):
                                if card_no[0:9] != card_no[7:16]:
                                    card_no_flag = 1
                                    card_details.append(card_no)
                                else:
                                    raise Exception(f"The {card_type} card must not have same numbers")
                            else:
                                raise Exception(f"The {card_type} card must not start with 1/2/3") 
                        else:
                            raise Exception(f"The {card_type} card must contain 16 digits")
                    else:
                        raise Exception(f"The {card_type} card number must be in numeric")  
                except Exception as e:
                    print(e)

            card_holder_flag = 0
            while card_holder_flag == 0:
                try:
                    name = input("Enter card holder name: ").upper()
                    if 1 <= len(name) <= 20:
                        if name.replace(" ","").isalpha():
                            if re.match("^[a-zA-Z]+[\s]?[a-zA-Z]*[\s]?[a-zA-Z]*$",name):
                                card_holder_flag = 1
                                card_details.extend([name])
                            else:
                                raise Exception("The name contains extra white spaces.")
                        else:
                            raise Exception("The name must be string and does not contain period(.)")
                    else:
                        raise Exception("The length should be 1 to 15 characters")
                except Exception as e:
                    print(e)

            expiry_date_flag = 0
            while expiry_date_flag == 0:
                try:
                    expiry_month = input("Enter the expiry date(month) in MM format: ")
                    if expiry_month.isnumeric():
                        if len(expiry_month) == 2:
                            if int(expiry_month) <= 12:
                                expiry_date_flag = 1
                                expiry_year_flag = 0
                                while expiry_year_flag == 0:
                                    try:
                                        expiry_year = input("Enter the expiry date(year) in YYYY format: ")
                                        if expiry_year.isnumeric():
                                            if len(expiry_year) == 4:
                                                if 2043 >= int(expiry_year) >= 2023:
                                                    expiry_year_flag = 1
                                                    expiry_detail = f"{expiry_month}/{expiry_year}"
                                                    card_details.extend([expiry_detail])
                                                else:
                                                    raise Exception("Invalid Year!!!(Year must 2023 b/w 2043 )")
                                            else:
                                                raise Exception("The length must be 4 characters")
                                        else:
                                            raise Exception("The value must be numeric")
                                    except Exception as e:
                                        print(e)
                            else:
                                raise Exception("The are only 12 months")
                        else:
                            raise Exception("The length must be 2 characters")
                    else:
                        raise Exception("The value must be numeric")
                except Exception as e:
                    print(e)

            cvv_flag = 0
            while cvv_flag == 0:
                try:
                    cvv = input("Enter the CVV number: ")
                    if cvv.isnumeric():
                        if len(cvv) == 3:
                            if cvv[0] != cvv[1] or cvv[1] !=  cvv[2]:
                                cvv_flag = 1
                                card_details.extend([cvv])
                            else:
                                raise Exception("All CVV number will not be same numbers")
                        else:
                            raise Exception("The lenght of CVV number is 3 digit")
                    else:
                        raise Exception("The CVV must be numeric.")
                except Exception as e:
                    print(e)

            return card_details


    @staticmethod
    def validate_net_banking():
        choose_bank_flag = 0
        while choose_bank_flag == 0:
            print("Choose your Bank")
            print("1.SBI")
            print("2.Indian Bank")
            print("3.IOB")
            print("4.KVB")
            print("5.HDFC")
            print("6.Canara Bank")
            print("7.ICICI")
            print("8.Others")
            choice = Validation.validate_quit_choice("Enter your choice or press ('q' to 'quit')", 8)
            if str(choice).isnumeric():
                while True:
                    try:
                        user_name = input("Enter Username: ")
                        if 1 <= len(user_name) <= 20:
                            password = Validation.validate_password("Enter Your Password: ")
                            return (user_name, password)
                        else:
                            raise Exception("The length should be 1 to 15 characters")
                    except Exception as e:
                        print(e)
            else:
                return


    @staticmethod
    def validate_add_menu():

        while True:
            try:
                choice = input("Enter 1 to add menu item in hotel or press('q' to 'quit'): ").lower()
                if len(choice) == 1:
                    if choice.isnumeric():
                        if int(choice) == 1:
                            return int(choice)
                        else:
                            raise Exception("It accepts 1 only")
                    else:
                        if choice == "q":
                            return choice
                        else:
                            raise Exception("It accepts 'q' only")
                else:
                    raise Exception("It only accepts only one character")
            except Exception as e:
                print(e)


    @staticmethod
    def validate_veg(name):

        while True:
            print("Press '1' for Veg or '2' for Non veg")
            try:
                choice = input(f"{name}: ")
                if choice.isnumeric():
                    if 1 <= int(choice) <= 2:
                        if int(choice) == 1:
                            return "VEG"
                        else:
                            return "NON VEG"
                    else:
                        raise Exception("The chocie must be 1 or 2")
                else:
                    raise Exception("The choice must be numeric")
            except Exception as e:
                print(e)


