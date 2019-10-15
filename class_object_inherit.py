#1-->class and object concept in python
#2-->inheritance

class postfix:
  animal_ytpe='fish'  #class variable
  def fun(self):
  	self.exp=exp
  	print(exp)
  	print('vikram sarabhai')

  def fun2(self,name):
  	self.name=name
  	print(name)
  	

  def __init__(self,exp):
  	self.exp=exp
  	print(exp,'this constructer method intialized when object is created')
exp="234*+"
ob=postfix(exp)
ob.fun()
ob.fun2('vikram singh')
print(ob.animal_ytpe) #class variable
print(ob.name)        #local variable

#child class or class inheritance in python
class sub_child(postfix):                           #inherit parent class--->> sub_class(parent_class_name)
	print('sub class use property')
	def __init__(self):
		print('child class constructer')
ob=sub_child()
print(ob.animal_ytpe) #parent class varible
ob.fun2('hare krishna')   #parent class function inherit

class sub_2(sub_child):  #inherit sub_child in sub_2
	pass
ob=sub_2()
ob.fun()	



