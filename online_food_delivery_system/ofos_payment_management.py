from ofos_restaurant_management import *
from ofos_order_management import *
from redmail import gmail   # `redmail` module is used to sent email to the regitered mail id 


def display_payment_options():

    print("Payment Mode:")
    payment_options = ("Upi id", "Credit and Debit cards", "Net Banking", "Pay on delivery")
    for i,j in enumerate(payment_options):
        print(f"{i+1}. {j}")
    return len(payment_options)


# Single Inheritance
class Payment_management(Order_management):

    # Constructor
    def __init__(self):
        self.card = {'hari98ts@gmail.com': [['CREDIT CARD', ['7234567890123456', 'Hariharan', '07', '2023', '234']],
                                            ['DEBIT CARD', ['5234567890123457', 'Hariharan', '07', '2023', '234']]]}
        #self.card = {mail_id:[[card_type,[card no, name, Exp date, Expyear, CVV ],[card_type,[card no, name, Exp date, Expyear, CVV]]}
        super().__init__()
        self.payment_history = {}
        #self.payment_history = {mail_id:[[amount_to_pay, ["YYYY", "MM", "DD", "HH", "MM", "SS"], [["BIRYANI",2,220.0,"NON VEG","HOTEL BUHARI"],["VEG BIRYANI",3,450.0,"VEG","HOTEL FARUZI"]]]]}


    # Instance method
    def payment_gateway_integration(self,mail_id, amount_to_pay):

        pay_mode_flag = 0
        while pay_mode_flag == 0:
            len_pay_mode = display_payment_options()
            pay_mode_choice = Validation.validate_quit_choice("Enter your choice or press ('q' to 'quit')", len_pay_mode)

            if str(pay_mode_choice).isnumeric():
                if pay_mode_choice == 1: # upi
                    get_upi = Validation.validate_upi_id()
                    return (self.payment_pay_page(mail_id, amount_to_pay), False) # (online_payment_success or not, Cash on delivery)

                elif pay_mode_choice == 2: # credit and debit cars
                    card_type_flag = 0
                    while card_type_flag == 0:
                        print("Card Type:")
                        print("1. Credit Card")
                        print("2. Debit Card")
                        card_choice = Validation.validate_quit_choice("Enter your choice or press ('q' to 'quit')", 2)

                        if str(card_choice).isnumeric():
                            if card_choice == 1: # Credit card details
                                card_inputs = Validation.validate_card("Credit")
                                print("Save this card for our future use?")
                                print("1.Yes")
                                print("2.No")
                                new_card_choice = Validation.validate_choice("Enter your choice",2)
                                if new_card_choice == 1:
                                    print(self.save_card_details(card_inputs, mail_id))
                                card_type_flag = 1 # to exit card loop

                            else: # Debit card details
                                card_inputs = Validation.validate_card("Debit")
                                print("Save this card for our future use?")
                                print("1.Yes")
                                print("2.No")
                                new_card_choice = Validation.validate_choice("Enter your choice",2)

                                if new_card_choice == 1:
                                    print(self.save_card_details(card_inputs, mail_id, True))
                                card_type_flag = 1 # to exit card loop

                            return (self.payment_pay_page(mail_id, amount_to_pay), False ) # (onlie_payment_success or not, Cash on delivery)

                        else:
                            card_type_flag = 1

                elif  pay_mode_choice == 3: # Net Banking
                    net_banking_inputs = Validation.validate_net_banking() # Its check with banks and gives authentication.
                    return (self.payment_pay_page(mail_id, amount_to_pay),False) # (online_payment_success or not, Cash on delivery)

                else: # Pay on delivery
                    return (True, True) # (online_payment_success or not, Cash on delivery)
            
            else:
                pay_mode_flag = 1
                return (False,)


    def save_card_details(self, card_details, mail_id, credit_card = False): # Saving card details in self.card

        if credit_card:
            card_type = "DEBIT CARD"
        else:
            card_type = "CREDIT CARD"

        if self.card:
            if self.card.get(mail_id):
                for i in self.card[mail_id]:
                    if i[1][0] ==  card_details[0]:
                        return "Already saved in your account"
                else:
                    self.card[mail_id].append([card_type,card_details])
                    return "Saved in your account"
            else:
                self.card[mail_id] = [[card_type,card_details]]
                return "Saved in your account"
        else:
            self.card[mail_id] = [[card_type, card_details]]
            return "Saved in your account"
    
    def payment_pay_page(self,mail_id, amount_to_pay): # After giving the payment details

        print("Redirecting.............")
        pay_choice = Validation.validate_choice(f"Press '1' to pay Rs.{amount_to_pay} to confirm your order or '2' to 'exit'", 2)
        
        if pay_choice == 1:
            return True
        else:
            return False


    def view_payment_history(self,mail):
        if self.payment_history.get(mail):
            for i, values in enumerate(self.payment_history[mail]):
                print()
                print(f"                              Order Number:{i+1}                             ")
                print("==============================================================================")
                print(f"|                             Date:{values[1][0]}:{values[1][1]}:{values[1][2]}                                |")
                print("|----------------------------------------------------------------------------|")
                print("|       Item       | quantity |   Price   |    Type    |       Restaurant    |")
                print("|============================================================================|")
                for index,items in enumerate(values[2]):
                    print(f"|{index+1:>3}.{items[0]:<14}|{items[1]:^10}|{items[2]:^11}|{items[3]:^12}|{items[4]:^21}|")
                print("|----------------------------------------------------------------------------|")
                print(f"|           Amount            |               Rs.{values[0]:<6}                      |")
                print("==============================================================================")
                print()
                print()
        else:
            print("You haven't ordered anything yet.")

        return 1 # order_item_flag

# Class Discount_and_offers_management inherits Payment_management:     
class Discount_and_offers_management(Payment_management):

    def __init__(self):
        super().__init__()

        
    def check_discount(self, amount):

        if amount >= 350:
            discount_amount = amount - ((25/100)*amount) # 25% discount when orderd above is due to given requirement.
            return discount_amount
        else:
            return amount
            
    def check_offers(self): # Future use when restaurants gave offers.
        pass
        

