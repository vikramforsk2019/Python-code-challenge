#overriding method 
class Fish:
	def __init__(self,f_name,l_name='fish'):
		self.f_name=f_name
		self.l_name=l_name
	def fun_fish(self):
		print('parent class method')
class sub_fish(Fish):    
	def fun_fish(self):
		print('child class override method')
		super().fun_fish()
ob=sub_fish('sark')	
print(ob.f_name)
print(ob.l_name)
ob.fun_fish()




#multiple inheritance
class Coral:

    def community(self):
        print("Coral lives in a community.")


class Anemone:

    def protect_clownfish(self):
        print("The anemone is protecting the clownfish.")


class CoralReef(Coral, Anemone):
    pass
great_barrier = CoralReef()
great_barrier.community()
great_barrier.protect_clownfish()