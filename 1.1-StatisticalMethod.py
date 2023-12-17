import pandas as pd

# Excel dosyasını oku
veri_df = pd.read_excel('C:/Users/LENOVO/Desktop/arac_veri2.xlsx')  # 'veri.xlsx' dosya adını ve yolunu güncelleyin

# Veriyi sözlüğe çevir
veriler = {
    'Model İsmi': veri_df['Model İsmi'].tolist(),
    'Adana': veri_df['Adana'].tolist(),
    'Ankara': veri_df['Ankara'].tolist(),
    'Antalya':veri_df['Antalya'].tolist(),
    'Bodrum':veri_df['Bodrum'].tolist(),
    'Bursa':veri_df['Bursa'].tolist(),
    'Denizli':veri_df['Denizli'].tolist(),
    'Diyarbakir':veri_df['Diyarbakir'].tolist(),
    'Gaziantep':veri_df['Gaziantep'].tolist(),
    'İstanbul':veri_df['İstanbul'].tolist(),
    'İzmir':veri_df['İzmir'].tolist(),
    'Kayseri':veri_df['Kayseri'].tolist(),
    'Kocaeli':veri_df['Kocaeli'].tolist(),
    'Sakarya':veri_df['Sakarya'].tolist(),
    'Samsun':veri_df['Samsun'].tolist(),
    'Tekirdağ':veri_df['Tekirdağ'].tolist(),
    'Trabzon':veri_df['Trabzon'].tolist(),
    'Kırmızı':veri_df['Kırmızı'].tolist(),
    'Beyaz':veri_df['Beyaz'].tolist(),
    'Siyah':veri_df['Siyah'].tolist(),
    'Benzin':veri_df['Benzin'].tolist(),
    'Dizel':veri_df['Dizel'].tolist(),
    'Hatchback':veri_df['Hatchback'].tolist(),
    'Sedan':veri_df['Sedan'].tolist(),
    'Spor':veri_df['Spor'].tolist(),
}

# Kullanıcıdan şehir ismi alalım
aranan_sehir = input("Hangi şehirdeki modellerin en yüksek olasılıklarını görmek istiyorsunuz? ")
aranan_renk = input("Hangi renk? ")
aranan_yakit = input("Hangi yakıt tercihiniz? ")
aranan_tip = input("Sedan Hatchback mi yoksa spor model mi? ")
# Verilen şehirdeki toplam satış sayısını bulalım
toplam_satis = sum(veriler[aranan_sehir])
toplam_satis_2 = sum(veriler[aranan_renk])
toplam_satis_3 = sum(veriler[aranan_yakit])
toplam_satis_4 = sum(veriler[aranan_tip])



# Her bir modelin olasılığını bir listeye ekleyelim
olasiliklar = [(model, satis / toplam_satis) for model, satis in zip(veriler['Model İsmi'], veriler[aranan_sehir])]
olasiliklar_2 = [(model, satis / toplam_satis_2) for model, satis in zip(veriler['Model İsmi'], veriler[aranan_renk])]
olasiliklar_3 = [(model, satis / toplam_satis_3) for model, satis in zip(veriler['Model İsmi'], veriler[aranan_yakit])]
olasiliklar_4 = [(model, satis / toplam_satis_4) for model, satis in zip(veriler['Model İsmi'], veriler[aranan_tip])]

# En yüksek üç olasılığı bulalım
en_yuksek_olasiliklar = sorted(olasiliklar, key=lambda x: x[1], reverse=True)[:3]
en_yuksek_olasiliklar_2 = sorted(olasiliklar_2, key=lambda x: x[1], reverse=True)[:1]
en_yuksek_olasiliklar_3 = sorted(olasiliklar_3, key=lambda x: x[1], reverse=True)[:1]
en_yuksek_olasiliklar_4 = sorted(olasiliklar_4, key=lambda x: x[1], reverse=True)[:1]

# Sonuçları ekrana yazdıralım
print(f"{aranan_sehir}'deki en yüksek 3 model ve olasılıkları:")
for model, olasilik in en_yuksek_olasiliklar:
    print(f"{model}: {olasilik:.2%}")
for model, olasilik_2 in en_yuksek_olasiliklar_2:
    print(f"{model}: {olasilik_2:.2%}") 
for model, olasilik_3 in en_yuksek_olasiliklar_3:
    print(f"{model}: {olasilik_3:.2%}")  
for model, olasilik_4 in en_yuksek_olasiliklar_4:
    print(f"{model}: {olasilik_4:.2%}") 
