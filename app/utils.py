#Utility functionsimport redis
import json
import redis

# 'host' normalde localhost olur ama Docker kullanınca servis adını yazacağız.
r = redis.Redis(host='localhost', port=6373, db=0)

def send_to_queue(log_data):
    dict_data = log_data.dict()
    
    json_data = json.dumps(dict_data, default=str)
    
    r.lpush("log_queue", json_data)
    
    print("Log başarıyla kuyruğa fırlatıldı!")