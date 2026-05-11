# 1. Temel imaj: İçinde Python 3.11 yüklü hazır bir mini bilgisayar alıyoruz.
FROM python:3.11-slim

# 2. Çalışma klasörü: Konteynerin içinde kodlarımız nerede dursun?
WORKDIR /code

# 3. Kütüphaneleri kopyala ve kur:
# Önce sadece gereksinimleri kopyalarız ki Docker bunları önbelleğe (cache) alsın.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Kalan tüm kodlarımızı içeriye kopyalıyoruz.
COPY . .

# 5. Başlangıç komutu: Konteyner açılınca otomatik olarak API'yi başlat.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]