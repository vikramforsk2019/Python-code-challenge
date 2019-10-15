#1-->class and object concept in python
#2-->inheritance

class postfix:
  def  __init__(self):
    self.stack_list= []
    print('this constructer method intialized when object is created')
  def exp(self,exp):
    self.exp=exp
    for i in range(len(exp)):
      #print(exp[i])
      if exp[i].isdigit():
        self.stack_list.append(exp[i])
        #print(stack_list)
      else:     
       print(self.stack_list)
    
exp="2@34*+"
ob=postfix()
ob.exp(exp)




