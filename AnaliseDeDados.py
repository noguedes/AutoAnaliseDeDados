#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv(r"C:\Users\User\Desktop\curso fiap\Projeto final - Tokio Marine\Automação Docs - Python\Aula 2\Aula 2\telecom_users.csv")


# In[4]:


df = df.drop(['Unnamed: 0'], axis=1)
display(df)


# In[7]:


#transformar coluna para tipo numérico
df['TotalGasto'] = pd.to_numeric(df['TotalGasto'], errors="coerce")


# In[9]:


#remover colunas que estão 100% vazias
df = df.dropna(how='all', axis=1)
display(df)


# In[10]:


#remover linhas que estão 100% vazias
df = df.dropna()


# In[11]:


#calculando encerramentos de contratos
display(df['Churn'].value_counts())


# In[13]:


display(df['Churn'].value_counts(normalize=True).map('{:.1%}'.format))


# In[17]:


#análise gráfica - importando Plotly
import plotly.express as px


# In[22]:


#criando gráficos automaticamente 
for coluna in df:
    if coluna != "IDCliente":
        #criar figura
        fig = px.histogram(df, x=coluna, color="Churn")


# In[24]:


#exibir a figura
fig.show()
display(df.pivot_table(index="Genero", columns=coluna, aggfunc='count')['IDCliente'])


# In[ ]:




