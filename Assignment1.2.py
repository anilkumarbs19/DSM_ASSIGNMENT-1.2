
# coding: utf-8

# In[1]:


i =[]
for x in range(2000, 3201):
    if (x%7)==0:          #check if the number is divisible by 7
        if (x%5)!=0:      #check if the number is not multiple of 5
            i.append(x)
            
print(i)

