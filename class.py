class Mobile:
    def __init__(self,Brand,battery,ram,camera,price):
        self.Brand= Brand
        self.battery = battery
        self.ram = ram
        self.camera = camera
        self.price = price

    def display(self):
        print("Brand", self.Brand)
        print("Brand", self.battery)
        print("Brand", self.ram)
        print("Brand", self.camera)
        print("Brand", self.price)
obj=Mobile("Apple","4000mah","8gb","48mp","90000")
obj.display()
obj2=Mobile("ONE+","4000mah","8gb","48mp","90000")
obj2.display()