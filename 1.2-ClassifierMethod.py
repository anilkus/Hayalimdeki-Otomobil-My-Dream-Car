import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Excel dosyasını oku
veri_df = pd.read_excel('C:/Users/LENOVO/Desktop/arac_veri2.xlsx')  # 'veri.xlsx' dosya adını ve yolunu güncelleyin

# Veriyi hazırla
features = ['Adana', 'Ankara', 'Antalya', 'Bodrum', 'Bursa', 'Denizli', 'Diyarbakir', 'Gaziantep', 'İstanbul',
            'İzmir', 'Kayseri', 'Kocaeli', 'Sakarya', 'Samsun', 'Tekirdağ', 'Trabzon', 'Kırmızı', 'Beyaz', 'Siyah',
            'Benzin', 'Dizel', 'Hatchback', 'Sedan', 'Spor']

X = veri_df[features]
y = veri_df['Model İsmi']

# Veriyi eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli oluştur
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Kullanıcıdan girdileri al
aranan_sehir = int(input("Hangi şehirdeki modellerin en yüksek olasılıklarını görmek istiyorsunuz? (1: Adana, 2: Ankara, ...): "))
aranan_renk = int(input("Hangi renk? (1: Kırmızı, 2: Beyaz, ...): "))
aranan_yakit = int(input("Hangi yakıt tercihiniz? (1: Benzin, 2: Dizel, ...): "))
aranan_tip = int(input("Sedan Hatchback mi yoksa spor model mi? (1: Hatchback, 2: Sedan, 3: Spor): "))

# Kullanıcının girdilerini modele uygun formata getir
girdiler = [0] * len(features)
girdiler[aranan_sehir - 1] = 1
girdiler[aranan_renk + 17] = 1
girdiler[aranan_yakit + 20] = 1
girdiler[aranan_tip + 22] = 1

# Tahmin yap
tahmin = model.predict([girdiler])[0]

# Tahmini ekrana yazdır
print(f"{veri_df.columns[aranan_sehir]} şehrinde, {veri_df.columns[aranan_renk + 17]} renkli, "
      f"{veri_df.columns[aranan_yakit + 20]} yakıtlı, {veri_df.columns[aranan_tip + 22]} modeli için en yüksek "
      f"olasılığa sahip model: {tahmin}")
