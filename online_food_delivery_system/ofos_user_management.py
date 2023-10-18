import maskpass # To make the password asterisk while entering the password
from ofos_validation import *

#Parent Class
class User_management:

    
    def __init__(self):
        self.user_database = {'hariharan98ts@gmail.com': ['Hari@1234', 'Hariharan', '8526686604', [['54/55', 'Varadhapuram', 'Kotturpuram', 'Chennai', '600044']]],
                              "raj@gmail.com":["Raj@1998", "Raj kumar", "9842648094",[["1/45", "MG street", "Guindy", "Chennai", "600034"]]]}
        #self.user_database = {"mail_id":[password,name,ph_no,[[door_no, street, area, city, pincode]]}

        
    @staticmethod
    def display_contents_in_userdatabase():

        contents = ("Name", "Phone Number", "Address", "Password")

        for i,j in enumerate(contents):
            print(f"{i+1}.{j}")

        return len(contents)


    @staticmethod
    def confirmation():

        options = ("Yes", "No")
        print("Are you confirm to save your change?")

        for i,j in enumerate(options):
            print(f"{i+1}.{j}")

        return len(options)    
        
        
    def register(self):

        print("---------------------------------------------")
        print("|            Create Your Account            |")
        print("---------------------------------------------")
        name_string = "Enter Your Name"
        name = Validation.validate_name(name_string)
         
        mail_id = Validation.validate_mail()
        if mail_id not in self.user_database:
            
            ph_no = Validation.validate_ph_no()
            for i in self.user_database:
                if ph_no in self.user_database[i]:
                    print("You are already an customer")
                    break
                else:
                    continue
            else:

                address_string = "Enter your Address"
                address = Validation.validate_address(address_string)

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
                
                self.user_database[mail_id] = [password2, name, ph_no, [address]]
            
        else:
            print(f"Hello {name}, Your account is already registerd.")

            
    def user_login(self):  # Used while entering order menu
        """
        print("++++++++++++++++++++++++++++++++")
        print("|          Login Page          |")
        print("++++++++++++++++++++++++++++++++")
        """
        mail_flag = 0
        while mail_flag == 0:
            mail_id = Validation.validate_mail()
            if mail_id in self.user_database:
                pass_flag = 1
                while pass_flag <= 3:
                    password1_string = "Enter your Password"
                    password1 = Validation.validate_password(password1_string)
                    #password1 = maskpass.askpass() # ------> Use anyone.(Not work with python IDLE)
                    #password1 = maskpass.advpass() # ------->(Not work with python IDLE)
                    if password1 == self.user_database[mail_id][0]:
                        pass_flag = 4
                        mail_flag = 1
                        print("Login Success!!")
                        return (True, mail_id)
                    else:
                        print("Your given password is wrong. TRY AGAIN!!!")
                        if not(pass_flag == 3):
                            print(f"You have only {3-pass_flag} attempts left.")
                        pass_flag += 1

                else:
                    print("You have exceed the limit")
                    return False,
            else:
                print("You have not registered as an user. First (SIGNUP in New User)")
                return False, # it returns tuple object (value,)
            
    
    def profile_view_update(self):
        print("---------------------------------------------")
        print("|            Update Your Account            |")
        print("---------------------------------------------")
        log_in = self.user_login()    # Implemented polymorphism
        if log_in[0]:
            while True:
                print(f"Hello {self.user_database[log_in[1]][1]}")
                print("******************************************")
                print("*  Choose the option you want to change  *")
                print("******************************************")
                tuple_length = User_management.display_contents_in_userdatabase()
                name_choice = "Enter your choice or press ('q' to 'quit')"
                choice = Validation.validate_quit_choice(name_choice, tuple_length)
                if choice == 1:
                    name_string = "Enter Your Name"
                    name = Validation.validate_name(name_string)
                    length_find = User_management.confirmation()
                    choice_name = "Enter your choice"
                    name_choice = Validation.validate_choice(choice_name, length_find)
                    if name_choice == 1:
                        self.user_database[log_in[1]][1] = name
                        print("Success!! Your name is updated")
                    else:
                        print("Your name is not updated")

                elif choice == 2: # phone number change
                    ph_no = Validation.validate_ph_no()
                    length_find = User_management.confirmation()
                    ph_no_name = "Enter your choice"
                    ph_choice = Validation.validate_choice(ph_no_name, length_find)
                    if ph_choice == 1:
                        self.user_database[log_in[1]][2] = ph_no
                        print("Success!! Your Phone Number is updated")
                    else:
                        print("Your Phone Number is not updated")
                    
                elif choice == 3: #address change
                    address_string = "Enter your Address"
                    address = Validation.validate_address(address_string)
                    length_find = User_management.confirmation()
                    address_name = "Enter your choice"
                    address_choice = Validation.validate_choice(address_name, length_find)
                    if address_choice == 1:
                        self.user_database[log_in[1]][3][0] = address
                        print("Success!! Your address is updated")
                    else:
                        print("Your address is not updated")
                                            
                elif choice == 4: # password change
                    new_password = self.change_password(mail_id)
                    if new_password[0]:
                        length_find = User_management.confirmation()
                        pass_name = "Enter your choice"
                        pass_choice = Validation.validate_choice(pass_name, length_find)
                        if pass_choice == 1:
                            self.user_database[log_in[1]][0] = new_password[1]
                            print("Success!! Your Password is updated")
                        else:
                            print("Your Password is not updated")
                    else:
                        print(new_password[1])

                else:
                    break
        else:
            return False


    def change_password(self,mail_id):
        
        old_pass_flag = 1
        while old_pass_flag <= 3:
            old_password_string = "Enter your old Password"
            old_password = Validation.validate_password(old_password_string)
            if old_password == self.user_database[mail_id][0]:
                old_pass_flag = 4

                password1_string = "Enter your New Password"
                password1 = Validation.validate_password(password1_string)
                password_check_flag = 0
                while password_check_flag == 0:
                    password2_string = "Re Enter your Password"
                    password2 = Validation.validate_password(password2_string)
                    if password1 == password2:
                        password_check_flag = 1
                        return (True, password2)
                    else:
                        print("Password and Confirm Password are not matching properly")
            else:
                print("Your given password does not match with existing password. TRY AGAIN!!!")
                if not(old_pass_flag == 3):
                    print(f"You have only {3-old_pass_flag} attempts left.")
                old_pass_flag += 1
        else:
            return (False, "You exceed the limit")
            
        
    
