class MyAccoun():
    def __init__(self, current_balance, pin_code, attempts):
        self.current_balance = current_balance
        self.pin_code = pin_code
        self.attempts = attempts

    def add_money(self, cash):
        return self.current_balance + cash

    def my_pin(self):
        return self.pin_code

    def my_attempts(self, pin):
        correct_pin = 777
        if self.attempts == 0:
            print "You have not attempts!"

        if pin != correct_pin:
            self.attempts = self.attempts - 1


monobank = MyAccoun(current_balance=1000, pin_code=777, attempts=2)

#print (monobank.add_money(500))