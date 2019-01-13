class Prime:
    'This class having method which return number is prime or not'
    number = 0

    def __init__ (self, num):
        Prime.number = num

    def isPrime (self):
        halfOfNum = (int)(self.number / 2)
        for i in range (2, halfOfNum+1):
            if (self.number % i == 0):
                return "false"
        return "true"
