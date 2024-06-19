
class complex_number:
    calc = ''
    
    def __init__(self,realnum,imagnum):
        self.realnum = realnum
        self.imagnum = imagnum

    def product(self,num):
        self.calc = f'{((self.realnum * num.realnum)- (self.imagnum * num.imagnum))} + {((self.realnum * num.imagnum) + (self.imagnum * num.realnum))}'
        print(self.calc)
         
    def printme(self):
        print(f'{'complex number of the given numer is :'} {self.calc}i')     
complex1 = complex_number(5,3)
complex2 = complex_number(3,4)
complex1.product(complex2)
complex1.printme()

'''
(a + ib) (c + id) ⇒ (ac - bd) + i(ad + bc)  
(1,2i)(3,5i)
===>((1*3)-(2*5)) + i((1*5)+(2*3))
===>3+11i-10
-7+11i


'''
