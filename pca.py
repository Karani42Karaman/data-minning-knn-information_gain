import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

url = "C:\\Users\\karani\\Desktop\\kafamısikeyim\\Numeric.xlsx"
#excel dosyamı okudum
df = pd.read_excel(url, names=['age','education-num','hours-per-week','income'])
features = ['age','education-num','hours-per-week']
x = df.loc[:, features].values
y = df.loc[:,['income']].values
x = StandardScaler().fit_transform(x)
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])

finalDf = pd.concat([principalDf, df[['income']]], axis = 1)
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('P.C.A 1', fontsize = 15)
ax.set_ylabel('P.C.A 2', fontsize = 15)
ax.set_title('2 PCA', fontsize = 20)
targets = [' <=50K', ' >50K']
colors = ['r', 'b']
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['income'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()