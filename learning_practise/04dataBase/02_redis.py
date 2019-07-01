import redis

# 1.打开命令行cmd，在redis目录下启动redis-server，再运行redis.exe

# 2.创建链接
client = redis.StrictRedis(host='127.0.0.1', port=6379)

# 2.设置key
key = 'pyone'

# 3. 设置value
result = client.set(key, "1")

# 4.删 1, 0
result = client.delete(key)

# 5.改
result = client.set(key, '2')

# 6.查--bytes
result = client.get(key)

# 查看所有的键
result = client.keys()

print(result)
