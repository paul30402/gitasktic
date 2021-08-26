#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 12:45:05 2021

@author: new
"""
import pandas as pd
from pandas import read_csv
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy import stats

#data directory
data_dir= '/Users/new/Documents/practice_git /nick/gProject/assignment/wiv/cs000-rd/group/ses-001/beh/'
dt_dir= '/Users/new/Documents/practice_git /nick/gProject/assignment/wiv/cs000-rd/sub-001/ses-001/beh/'
data= data_dir+'group_ses-001_task-colorpreference_beh.csv'

#read csv 
df= pd.read_csv(data, sep='\t')

df=df.filter(items=['participant', 'cond','acc','t2t']) 

#list of every participant df
sub = df.groupby('participant')

list_sub = [] 
for name, group in sub:
        #print(name)
        #print(group)
        list_sub.append(group)

list_sub_p = list_sub.copy()
list_sub_st = list_sub.copy()
list_sub_sw = list_sub.copy()


#filter data frame for pure similarity

o = []
l= []        
for i, df in enumerate(list_sub_p):    
    a = list_sub_p[i] = df.query('t2t == "pure_sim"')
    b = list_sub_p[i] = df.query('cond == "1" and acc == "1.0" and t2t == "pure_sim"')
    #print(a)
    #print(b)
    o.append(a)
    l.append(b)

sum_pure_sim= []
for k, len_df in enumerate(o):
        #print(len(len_df))
        sum_pure_sim.append(len(len_df))

sum_acc_pure_sim=[]
#sum acc for each participant
for k, len_df in enumerate(l):
    #print(len(len_df))
    sum_acc_pure_sim.append(len(len_df))

    
#acc
df0 = pd.DataFrame(sum_pure_sim, columns=['sum_pure_sim'])
df0.index += 1

df1 = pd.DataFrame(sum_acc_pure_sim, columns=['sum_accuracy'])
df1.index += 1
#sum trials
pure_similarity_accuracy = pd.concat([df0, df1], axis=1)
pure_similarity_accuracy['acc%_pure'] = pure_similarity_accuracy['sum_accuracy']/pure_similarity_accuracy['sum_pure_sim']*100



#🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒

#filter data frame for stay similarity
     
p= []        
o = []
for i, df in enumerate(list_sub_st):    
    a = list_sub_st[i] = df.query('t2t == "stay_sim"')
    b = list_sub_st[i] = df.query('cond == "1" and acc == "1.0" and t2t == "stay_sim"')
    #print(a)
    #print(b)
    p.append(b)
    o.append(a)

sum_stay_sim= []
for k, len_df in enumerate(o):
        #print(len(len_df))
        sum_stay_sim.append(len(len_df))

sum_acc_stay_sim= []
#sum acc for each participant
for k, len_df in enumerate(p):
    #print(len(len_df))
    sum_acc_stay_sim.append(len(len_df))


#sum trials
df1 = pd.DataFrame(sum_stay_sim, columns=['sum_stay_sim'])
df1.index += 1

#acc
df0 = pd.DataFrame(sum_acc_stay_sim, columns=['sum_accuracy'])
df0.index += 1


stay_similarity_accuracy = pd.concat([df0, df1], axis=1)
stay_similarity_accuracy['acc%_stay'] = stay_similarity_accuracy['sum_accuracy']/stay_similarity_accuracy['sum_stay_sim']*100

#🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒🗒

#filter data frame for switch similarity



q= []        
o = []
for i, df in enumerate(list_sub_sw):    
    a = list_sub_sw[i] = df.query('t2t == "switch_pref"')
    b = list_sub_sw[i] = df.query('cond == "1" and acc == "1.0" and t2t == "switch_pref"')
    #print(a)
    #print(b)
    q.append(b)
    o.append(a)

sum_switch_sim= []
for k, len_df in enumerate(o):
        #print(len(len_df))
        sum_switch_sim.append(len(len_df))

sum_acc_switch_sim= []
#sum acc for each participant
for k, len_df in enumerate(q):
        #print(len(len_df))
        sum_acc_switch_sim.append(len(len_df))

#sum trials
df0 = pd.DataFrame(sum_switch_sim, columns=['sum_switch_sim'])
df0.index += 1

#acc
df1 = pd.DataFrame(sum_acc_switch_sim, columns=['sum_switch_accuracy'])
df1.index += 1

switch_similarity_accuracy = pd.concat([df0, df1], axis=1)
switch_similarity_accuracy['acc%_switch'] = switch_similarity_accuracy['sum_switch_accuracy']/switch_similarity_accuracy['sum_switch_sim']*100

#statistic
accuracy = pd.concat([pure_similarity_accuracy['acc%_pure'],stay_similarity_accuracy['acc%_stay'], switch_similarity_accuracy['acc%_switch'], ], axis=1)

D= accuracy[['acc%_pure','acc%_stay','acc%_switch']].describe()
print('statistic descriptive for accuracy of each block conditions:')
print(D)
stay_Vs_switch= stats.ttest_rel(accuracy['acc%_stay'], accuracy['acc%_switch'])
print('paired t-test result between accuracy stay and switch')
print(stay_Vs_switch)




