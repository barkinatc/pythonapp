# Python base image
FROM python:3.8-slim

# Çalışma dizinini belirle
WORKDIR /app

# Gereksinimleri yükle
COPY requirements.txt .
RUN pip install -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Flask uygulamasını başlat
CMD ["python", "run.py"]
