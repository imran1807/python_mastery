class utility:
    @staticmethod
    def check_even(a):
        if a%2==0:
            print("its a even number")
        else :
            print("its a odd")
    @staticmethod
    def check_odd(a):
        if a%2!=0:
            print("its a odd number")
        else :
            print("its a even")
    @staticmethod
    def find_factorial(a):
        if a<=1:
            return 1
        else:
            return a* utility.find_factorial(a-1)
    @staticmethod
    def is_prime(a):
        if a<=3 and a>0:
            print("its a prime")
        for i in range(2,a-1):
            if a%i==0:
                print("its not a prime")
                return
        else:
            print("it a prime")

if __name__ == "__main__":
    u1=utility()
    utility.check_even(4)
    utility.is_prime(7)

        