
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 04:28:58 2021

@author: karani
"""
import pandas as pd
import pandas.plotting
import numpy as np

# excel dosyasını  okuduk
df = pd.read_excel('C:\\Users\\karani\\Desktop\\kafamısikeyim\\Categorig.xlsx')

#tüm colonlerımda yapılan işlemlerin sonucunu  aynı  anda çağıran methodum
def entropi_display():
        workclassGroup = df.groupby(['workclass']).income.value_counts()
        print("workclass Entropi Hesabı : ",calculate_entropy(workclassGroup))
        
        educationGroup = df.groupby(['education']).income.value_counts()
        print("education Entropi Hesabı  : ",calculate_entropy(educationGroup))
        
        marital_statusGroup = df.groupby(['marital_status']).income.value_counts()
        print("marital_status Entropi Hesabı : ",calculate_entropy(marital_statusGroup))
        
        occupationGroup = df.groupby(['occupation']).income.value_counts()
        print("occupation Entropi Hesabı : ",calculate_entropy(occupationGroup))
        
        relationshipGroup = df.groupby(['relationship']).income.value_counts()
        print("relationship Entropi Hesabı : ", calculate_entropy(relationshipGroup))
        
        raceGrpup = df.groupby(['race']).income.value_counts()
        print("race Entropi Hesabı : ",calculate_entropy(raceGrpup))
        
        genderGroup = df.groupby(['gender']).income.value_counts()
        print("gender Entropi Hesabı : ",calculate_entropy(genderGroup))
        
        native_countryGroup = df.groupby(['native_country']).income.value_counts()
        print("native_country Entropi Hesabı : ",calculate_entropy(native_countryGroup))

#Entropi hesabını  yapan methodum
def calculate_entropy(frequency: list):
        entropy=0
        sum_freq = sum(frequency)# tüm değerli topluyor
        for i, x in enumerate(frequency):
            p_x = float(frequency[i] / sum_freq)#oranı  buluyor
            if p_x > 0:
                entropy +=  p_x * (-np.log(p_x))#entropiyi hesaplıyor
        else:
            return entropy
 
entropi_display()


