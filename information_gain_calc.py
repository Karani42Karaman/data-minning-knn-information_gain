import pandas as pd
import numpy as np
# excel dosyasını  okuduk
df = pd.read_excel('C:\\Users\\karani\\Desktop\\kafamısikeyim\\Categorig.xlsx')
def compute_impurity(feature, impurity_criterion):
    """
  bir özelliğin saflığını hesaplar.
    """
    probs = feature.value_counts(normalize=True)   
    if impurity_criterion == 'entropy':
        impurity = -1 * np.sum(np.log2(probs) * probs)
    elif impurity_criterion == 'gini':
        impurity = 1 - np.sum(np.square(probs))
    else:
        raise ValueError('Bilinmeyen kirlilik kriteri')        
    return(round(impurity, 3))

def comp_feature_information_gain(df, target, descriptive_feature, split_criterion):
    """
    Bu işlev, bölme için bilgi kazancını hesaplar.
    """
    print('tanımlayıcı özellik:', descriptive_feature)          
    target_entropy = compute_impurity(df[target], split_criterion)
    entropy_list = list()
    weight_list = list()
    for level in df[descriptive_feature].unique():
        df_feature_level = df[df[descriptive_feature] == level]
        entropy_level = compute_impurity(df_feature_level[target], split_criterion)
        entropy_list.append(round(entropy_level, 3))
        weight_level = len(df_feature_level) / len(df)
        weight_list.append(round(weight_level, 3))
 
    feature_remaining_impurity = np.sum(np.array(entropy_list) * np.array(weight_list))
    information_gain = target_entropy - feature_remaining_impurity
    print('information gain:', information_gain)
    print('*********************************')
    return(information_gain)

print("information_gain Calculate")
split_criterion = 'entropy'
for feature in df.drop(columns='income').columns:
    feature_info_gain = comp_feature_information_gain(df, 'income', feature, split_criterion)