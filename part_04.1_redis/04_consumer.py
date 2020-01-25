import redis

r = redis.Redis(host="localhost", port=6379, db=0)

while True:
    url = r.brpop('xiaomi:spider', 4)
    # brpop 返回的是元组
    
    if url:
        print("我正在抓取:", url[1].decode())
    else:
        print("抓取结束")
        break
