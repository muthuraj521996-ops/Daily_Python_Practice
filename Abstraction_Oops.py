'''from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("Car Started")
c=car()
c.start()'''

from abc import ABC, abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class creditcard(payment):
    def pay(self):
        print("Credit card payment")
class upi(payment):
    def pay(self):
        print("upi payment")
c=creditcard()
c.pay()
u=upi()
u.pay()

