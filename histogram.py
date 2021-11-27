# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 04:28:58 2021

@author: karani
"""

import pandas as pd
import pandas.plotting

 
# excel dosyasını  okuduk
df = pd.read_excel('C:\\Users\\karani\\Desktop\\kafamısikeyim\\Categorig.xlsx')
print(df.head())#excel dosyamın içini gördüm

workclassGroupCountInfo = pd.DataFrame(df.workclass.value_counts())#colonu  gruplamaya  yarıyor
workclassGroupCountInfo.plot(kind='bar', stacked=True)
print(workclassGroupCountInfo)

educationGroupCountInfo = pd.DataFrame(df.education.value_counts())
educationGroupCountInfo.plot(kind='bar', stacked=True)
print(educationGroupCountInfo)

marital_statusGroupCountInfo = pd.DataFrame(df.marital_status.value_counts())
marital_statusGroupCountInfo.plot(kind='bar', stacked=True)
print(marital_statusGroupCountInfo)

occupationGroupCountInfo =  pd.DataFrame(df.occupation.value_counts())
occupationGroupCountInfo.plot(kind='bar', stacked=True)
print(occupationGroupCountInfo)

relationshipGroupCountInfo =  pd.DataFrame(df.relationship.value_counts())
relationshipGroupCountInfo.plot(kind='bar', stacked=True)
print(relationshipGroupCountInfo)

raceGrpupCountInfo =  pd.DataFrame(df.race.value_counts())
raceGrpupCountInfo.plot(kind='bar', stacked=True)
print(raceGrpupCountInfo)
 
genderGroupCountInfo =  pd.DataFrame(df.gender.value_counts())
genderGroupCountInfo.plot(kind='bar', stacked=True)
print(genderGroupCountInfo)

native_countryGroupCountInfo = pd.DataFrame(df.native_country.value_counts())
native_countryGroupCountInfo.plot(kind='bar', stacked=True)
print(native_countryGroupCountInfo)


 