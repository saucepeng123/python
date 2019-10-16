#!/usr/bin/env python
# coding: utf-8

# ## 實作練習一

# In[28]:


score = input("請輸入成績:")
if(int(score)>= 90):
    print("優等")
elif(int(score)>= 80):
    print("甲等")
elif(int(score)>= 70):
    print("乙等")
elif(int(score)>= 60):
    print("丙等")
else:
    print("丁等")


# ## 實作練習二

# In[48]:


score = int (input("請輸入正整數:"))
sum=0
i=1
for n in range(score):
    sum=sum+i
    i=i+1
print(sum, end=" ")              


# ## 實作練習五

# In[47]:


n=int(input("請輸入正整數:"))
for i in range(1, n+1):
    if i % 5 ==0:
        continue
    print(i, end=",")    


# ## 實作練習六

# In[46]:


n=int(input("請輸入正整數:"))
output =n

if n==1:
        print(n)
else:
    while(n>=2):
        output=output*(n-1)
        n=n-1
    print(output)


# In[ ]:




