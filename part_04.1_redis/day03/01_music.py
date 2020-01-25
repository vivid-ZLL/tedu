"""
网易音乐排行榜 前三名
"""

import redis

r = redis.Redis()

# 有序集合 - song:rank


r.zadd('song:rank', {'song1': 1, 'song2': 1, 'song3': 1, 'song4': 1, 'song5': 1, 'song6': 1})
# 增加分值
r.zincrby('song:rank', 50, 'song1')
r.zincrby('song:rank', 60, 'song6')
r.zincrby('song:rank', 20, 'song5')
# 查看排名 - 前3名
rank_list = r.zrevrange("song:rank", 0, 2, True)
print(rank_list)  # [(b'song6', 61.0), (b'song1', 51.0), (b'song5', 21.0)]

# 第一名:song6 播放次数:61
# 第二名: ....
i = 1
for rank in rank_list:
    print('第{}名:{} 播放次数:{}'.format(
        i,
        rank[0].decode(),
        int(rank[1])
    ))
    i += 1






