
# coding: utf-8

# In[17]:



c=0
def moneychange(a):
    global c
    c1=1
    c2=5
    c3=10
    if a<c2:
        return a
    if c2<=a<c3:
        c=1+(a-5)
        return c
    else:
        c=c+1+ moneychange(a-10)
        return c
        
      
        
if __name__ == '__main__':
    input_n = int(input())
    print(moneychange(input_n))
        
    

