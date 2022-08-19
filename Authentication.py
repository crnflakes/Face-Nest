
import re
class Authenticate(object):
    def __init__(self, password = ''):
        self.password = password
    def __lower(self):
        lower = any(c.islower() for c in self.password)
        return lower
    def __upper(self):
        upper = any(c.isupper() for c in self.password)
        return upper
    def __digit(self):
        digit = any(c.isdigit() for c in  self.password)
        return digit
    def validate(self):
        lower = self.__lower()
        upper = self.__upper()
        digit = self.__digit()
        special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        length = len(self.password)
        report =  lower and upper and digit and length >= 8

        if report:
            print("Password passed strong password policy")
            return True

        elif not lower:
            print("You didnt use Lower case letter")
            return False
        
        elif (special_char.search(self.password) == None):
            print("Please include special characters")
            return False

        elif not upper:
            print("You didnt Upper case letter")
            return False

        elif length <8:
            print("Password should Atleast have 8 character")
            return False

        elif not digit:
            print("You didnt use Digit")
            return False
        else:
            pass