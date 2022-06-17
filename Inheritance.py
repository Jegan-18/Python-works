class A:
    def feature1(self):
        print("Feature 1 is in Class A Working")

    def feature2(self):
        print("Feature 2 is in Class A Working")


class B:
    def feature3(self):
        print("Feature 3 in Class B is Working")

    def feature4(self):
        print("Feature 4 in Class B is Working")

class C(A, B):
    def feature5(self):
        print("Feature 5 in Class 5 is Working")


a1 = A()
b1 = B()
c1 = C()

c1.feature3()