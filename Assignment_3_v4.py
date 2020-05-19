#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd

### dataframe1 intake and clean

with open('output.json', 'r') as f:
    df1 = f.readlines()
#print(df1)

df1 = str(df1)
df1 = df1.replace('", "purpose": "', ';')
df1 = df1.replace('"}, {"name": "', ';')
#counter = df1.count("'")
#print(str(counter))
df1 = df1.replace("'", "")
df1 = df1.replace('[[{"name": "', '')
df1 = df1.replace('"}]]', ';')
#print(df1)


### dataframe2 intake and clean

with open('myfile.txt', 'r') as f:
    df2 = f.readlines()

    #mystr = '\n'.join([line.strip() for line in lines])
#my_string = my_string.replace(r"\n", "\t")
df2 = str(df2)
df2 = df2.replace(r"\n", " ")
#print(df2)

df2 = str(df2)
#df2 = df2.replace("\n',", ";")
df2 = df2.replace("['Name: ", "")
df2 = df2.replace(" ', 'Name: ", ";")
df2 = df2.replace(" ', 'Purpose: ", ";")
df2 = df2.replace("']", ";")


### dataframe3 intake and clean

with open('Webscrp_company.txt', 'r') as f:
    df3 = f.readlines()

df3 = str(df3)
df3 = df3.replace('":', ';')
df3 = df3.replace('",',';')
df3 = df3.replace('"','')
df3 = df3.replace("['{","")
df3 = df3.replace("}']",";")
#print(df3)
#counter = df3.count(";")
#print(str(counter))


### dataframe4 intake and clean

with open('result1.txt', 'r') as f:
    df4 = f.readlines()
    #mystr = '\n'.join([line.strip() for line in lines])
#my_string = my_string.replace(r"\n", "\t")
df4 = str(df4)
df4 = df4.replace(r"\n", " ")
#print(df4)

df4 = df4.replace("['Name: ","")
df4 = df4.replace(" ', 'Purpose:",";")
df4 = df4.replace(" ', 'Name:",";")
df4 = df4.replace("']",";")
#print(df4)



### references: 
### https://stackoverflow.com/questions/54588657/converting-multi-line-string-to-single-line-string-in-python
### https://textblob.readthedocs.io/en/dev/
### https://pypi.org/project/textblob/


# In[2]:


with open('output.json', 'r') as f:
    df1 = f.readlines()

print(df1)


# In[3]:


df1 = str(df1)
df1 = df1.replace('", "purpose": "', ';')
df1 = df1.replace('"}, {"name": "', ';')
#counter = df1.count("'")
#print(str(counter))
df1 = df1.replace("'", "")
df1 = df1.replace('[[{"name": "', '')
df1 = df1.replace('"}]]', ';')
#print(df1)


# In[4]:


with open('myfile.txt', 'r') as f:
    df2 = f.readlines()

    #mystr = '\n'.join([line.strip() for line in lines])
#my_string = my_string.replace(r"\n", "\t")
df2 = str(df2)
df2 = df2.replace(r"\n", " ")
print(df2)


# In[5]:


df2 = str(df2)
#df2 = df2.replace("\n',", ";")
df2 = df2.replace("['Name: ", "")
df2 = df2.replace(" ', 'Name: ", ";")
df2 = df2.replace(" ', 'Purpose: ", ";")
df2 = df2.replace("']", ";")


print(df2)


# In[6]:


with open('Webscrp_company.txt', 'r') as f:
    df3 = f.readlines()

print(df3)


# In[7]:


df3 = str(df3)
df3 = df3.replace('":', ';')
df3 = df3.replace('",',';')
df3 = df3.replace('"','')
df3 = df3.replace("['{","")
df3 = df3.replace("}']","; ")
print(df3)

#counter = df3.count(";")
#print(str(counter))


# In[8]:


counter = df3.count(";")
print(str(counter))


# In[9]:


with open('result1.txt', 'r') as f:
    df4 = f.readlines()
    #mystr = '\n'.join([line.strip() for line in lines])
#my_string = my_string.replace(r"\n", "\t")
df4 = str(df4)
df4 = df4.replace(r"\n", " ")
print(df4)


# In[10]:


df4 = df4.replace("['Name: ","")
df4 = df4.replace(" ', 'Purpose:",";")
df4 = df4.replace(" ', 'Name:",";")
df4 = df4.replace("']","; ")
print(df4)


# In[11]:


### dataframe5 intake and clean

with open('companys.csv', 'r') as f:
    df5 = f.readlines()

    #mystr = '\n'.join([line.strip() for line in lines])
#my_string = my_string.replace(r"\n", "\t")
#df5 = str(df5)
#df5 = df5.replace(r"\n", "")
print(df5)


# In[12]:


df5 = str(df5)
#df5 = df5.replace("\n',", ";")
df5 = df5.replace("['Name,Purpose', '", "")
df5 = df5.replace(" ', 'Name: ", ";")
df5 = df5.replace(" ', 'Purpose: ", ";")
df5 = df5.replace("']", ";")


# In[13]:


### dataframe6 intake and clean

with open('napu (1).csv', 'r') as f:
    df6 = f.readlines()

#df6 = str(df6)
#df6 = df6.replace(r"\n", "")
print(df6)


# In[14]:


### dataframe7 intake and clean

with open('result.csv', 'r') as f:
    df7 = f.readlines()

#df7 = str(df7)
#df7 = df7.replace(r"\n", "")
print(df7)


# In[16]:


## Combine dataframes

df_all = df3+df4
df_all = df_all.replace("; ",";")
print(df_all)


# In[26]:


Combo1 = df_all.split(';',199)
#Combo1 = Combo1.replace("' ","'")
#Combo1 = [sub.replace(" ' "," '") for sub in Combo1]
print(Combo1)


# In[27]:


Name_cols = Combo1[0::2]
Name_cols


# In[28]:


print(len(Name_cols))


# In[29]:


#Combo1 = df_all.split(';',300)
#print(Combo1)
#Name_cols = Combo1[0::2]
Purpose_cols = Combo1[1::2]
print(Purpose_cols)


# In[30]:


print(len(Purpose_cols))


# In[31]:


type(Purpose_cols)


# In[32]:


def listToString(Purpose_cols):
    purpose_string = ""
    for element in Purpose_cols:
        purpose_string += element + "; "
    return purpose_string

print(listToString(Purpose_cols))


# In[33]:


b = listToString(Purpose_cols)
from textblob import TextBlob
s = ""
blob = TextBlob(b)
for sentence in blob.sentences:
        s += str(sentence.sentiment.polarity) + "; "


s = s[:-2]
s = s.split(';',)


# In[34]:


print(s)


# In[35]:


for sentence in blob.sentences:
    print(sentence.sentiment.polarity)


# In[36]:


top10 = sorted(range(len(s)), key=lambda i: s[i], reverse=True)[0:9]


# In[37]:


print(type(top10))


# In[38]:


print(s)


# In[39]:


top10


# In[ ]:




