import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
from scipy import stats

url = "C:\\Users\\karani\\Desktop\\kafamısikeyim\\Numeric.xlsx"
# load dataset into Pandas DataFrame
df = pd.read_excel(url, names=['age','education-num','hours-per-week','income'])
features = ['age','education-num','hours-per-week']
x = df.loc[:, features].values
y = df.loc[:,['income']].values
x = StandardScaler().fit_transform(x)
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents ).to_numpy()
#iki vekor arasindaki oklid uzakligi
def oklid_uzaklik(v1,v2):
    col_sayi=len(v1) #v1 vektörünün uzunluğu
    t=0
    for i in range(col_sayi):
        t+=(v1[i]-v2[i])*(v1[i]-v2[i])
        
    return np.sqrt(t) #toplamin karaköküne dönüyor
def ozellik_normallestir(col):
    the_max=np.max(col)
    the_min=np.min(col)
    for i in range(len(col)):
        col[i]=(col[i]-the_min)/(the_max-the_min)#istenirse buraya the_max-the_min'in 0 olma exception'i eklenebilir
    return col
satir_sayisi=10854
sutun_sayisi=2
wine_shuffled=principalDf  #satirlari kariyoruzki egitim seti, val seti ve test sinifina her siniftan ayni miktarda gelebilsin
for i in range(2):
    wine_shuffled[:,i]=ozellik_normallestir(wine_shuffled[:,i])
#######veri setinin parcalanmasi####
egitim_set=wine_shuffled[:5000,:]#ilk 90 satiri egitim setine ayiriyoruz (bu yaklasik %50'lik bir kisim)
egitim_X=egitim_set[:,:sutun_sayisi-1]
egitim_Y=egitim_set[:,sutun_sayisi-1]
egitim_num=egitim_X.shape[0]
val_set=wine_shuffled[5000:7000,:] #44 satiri validasyon setine ayiriyoruz (bu yaklasik %25'lik bir kisim)
val_X=val_set[:,:sutun_sayisi-1]
val_Y=val_set[:,sutun_sayisi-1]
val_num=val_X.shape[0]
test_set=wine_shuffled[7000:,:]  #44 satiri test setine ayiriyoruz (bu yaklasik %25'lik bir kisim)
test_X=test_set[:,:sutun_sayisi-1]
test_Y=test_set[:,sutun_sayisi-1]
test_num=test_X.shape[0]
###############################
#en ideal k degerine karar verebilmek icin validasyon seti uzerinde farkli k degerleri icin 
#en yakin komsu algoritmasini calistiyoruz, hangi k icin en yuksek performansi alacaksak o k degerini 
#test setinde kullanmak uzere sabitliyoruz
aday_k=[1,3,5,7,9,11]
performanslar=[] #her bir k degerinden elde edilcek performans degeri bu listede tutalacak
for k in aday_k: #aday_k listesinin icini geziyor
    tahminler=[]# her bir validasyon ornegiicin urettigimiz sinif tahminini bu listede tutacagiz.
    for v in range(val_num):
        sinifi_merak_edilen=val_X[v,:] #bunu siniflandiracagiz
        uzakliklar=[]#bu liste sinifini merak ettigimiz validasyon orneginin tüm egitim örneklerine olan uzakliklarini tutacak
        for e in range(egitim_num): #her bir egitim ornegi icin
            test_edilen=egitim_X[e,:]
            uzaklik=oklid_uzaklik(sinifi_merak_edilen,test_edilen)
            uzakliklar.append(uzaklik) # e. siradaki egitim ornegi ile v. siradaki validasyon ornegi arasiu uzaklik
        en_yakin_komsular=np.argsort(uzakliklar)#egitim örneklerinin sinif merak edilenvalidasyon ornegine yakinliklarina göre siralanmasi
        en_yakin_komsular_siniflar=egitim_Y[en_yakin_komsular[:k]] #egitim örneklerinin ilk k tanesini aliyoruz
        en_cok_gorulen_sinif=stats.mode(en_yakin_komsular_siniflar)[0][0]#en yakin k egitim orneginde en cok gorulen sinif
        tahminler.append(en_cok_gorulen_sinif)
    #bu noktada tum validasyon orneklerini siniflandirmis oluyoruz, simdi bu tahminleri
    #validasyon örneklerinin gercek siniflari ile karsilastiriyoruz
    basari=0   
    for v in range(val_num):
        if tahminler[v]==val_Y[v]:#dogru tahmin ettigimiz her validasyon ornegi icin basari sayimizi bir artiriyoruz.
            basari+=1
    performans=(basari/val_num)*100 #dikkat edersek burda en disardaki for loop'unun icindeyiz, elde edilen bu performans  belirli bir k degeri icin elde edilen performanstir
    performanslar.append(performans)
best_k=aday_k[np.argmax(performanslar)] #np.argmax(performanslar kacinci k degerinde en yuksek performans alindigini verir
####################################
#bundan sonra validasyon setini kullanarak öğrendigimiz k degeri icin test örneklerini yine ayni validasyon setinde oldugu gibi siniflandiriyoruz.
tahminler=[]
for t in range(test_num):
    sinifi_merak_edilen=test_X[t,:]
    uzakliklar=[]
    for e in range(egitim_num):
        test_edilen=egitim_X[e,:]
        uzaklik=oklid_uzaklik(sinifi_merak_edilen,test_edilen)
        uzakliklar.append(uzaklik)
    en_yakin_komsular=np.argsort(uzakliklar)
    en_yakin_komsular_siniflar=egitim_Y[en_yakin_komsular[:best_k]]
    en_cok_gorulen_sinif=stats.mode(en_yakin_komsular_siniflar)[0][0]
    tahminler.append(en_cok_gorulen_sinif)
basari=0   
for t in range(test_num):
    if tahminler[t]==test_Y[t]:
        basari+=1
performans=(basari/test_num)*100     
print("k-En yakin Komsu siniflandirma performansi: {}".format(performans))




