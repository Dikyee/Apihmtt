# 接口host
from tools.read_yaml import read_yaml

host = "http://api-toutiao-web.itheima.net"

# 请求头
headers = {"Content-Type":"application/json"}

# 文章id
artical_id = None

# 读取发表文章内容
data_artical = read_yaml("data_zmt_artical.yaml")

# 发表文章标题
title = data_artical[0][0]
# 发表文章内容
content = data_artical[0][1]
# 频道id
channal_id = data_artical[0][2]