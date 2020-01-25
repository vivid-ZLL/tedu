import redis

r = redis.Redis()

# 有序集合中添加了8首歌曲
r.zadd('ranking', {'song1': 1, 'song2': 1, 'song3': 1, 'song4': 1})
r.zadd('ranking', {'song5': 1, 'song6': 1, 'song7': 1, 'song8': 1})
# 指定成员增加分值
r.zincrby('ranking', 50, 'song3')
r.zincrby('ranking', 60, 'song4')
r.zincrby('ranking', 70, 'song8')
# 获取前3名: [('song8',71),(),()]

#
rank_list = r.zrevrange('mobile:001-003', 0, 2, withscores=True)

i = 1
for rank in rank_list:
    print("第{}名:{} 销量".format(i, rank[0].decode(), int(rank[1])))
    i += 1
