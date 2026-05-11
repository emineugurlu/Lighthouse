import os
import redis
import json
import time

# 1. Ambarın adresini alıyoruz
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=REDIS_HOST, port=6379, db=0)

def start_worker():
    print("--- İŞÇİ ÇALIŞMAYA BAŞLADI ---")
    
    while True:
        data = r.rpop("log_queue")
        if data:
            log = json.loads(data)
            
            # Ekrana basma (zaten yapıyorsun)
            print(f"[*] İŞLENDİ: {log['message']}")
            
            # --- YENİ KISIM: DOSYAYA YAZ ---
            with open("logs.txt", "a", encoding="utf-8") as f:
                f.write(f"{log['timestamp']} | {log['level']} | {log['service_name']} | {log['message']}\n")
            # -------------------------------
            
        else:
            time.sleep(1)

if __name__ == "__main__":
    start_worker()