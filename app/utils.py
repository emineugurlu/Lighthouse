import redis
import json
import os

# Bağlantı ayarı
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=REDIS_HOST, port=6379, db=0)

def send_to_queue(log_data):
    try:
        # Pydantic nesnesini sözlüğe çevirip paketliyoruz
        dict_data = log_data.dict()
        json_data = json.dumps(dict_data, default=str)
        
        # Redis'e fırlatıyoruz
        r.lpush("log_queue", json_data)
        print("--- LOG REDIS'E GÖNDERİLDİ ---")
    except Exception as e:
        print(f"HATA OLUŞTU: {e}")