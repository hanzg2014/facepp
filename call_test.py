#-*- coding: utf-8 -*-


# 您需要先注册一个App，并将得到的API key和API secret写在这里。
# You need to register your App first, and enter you API key/secret.
API_KEY = "a0xuYL30nQOFVXwSa1TlmD15-lSIpcMp"
API_SECRET = "IGxjLRu7IUc53gA-4_XpbpXj8662F4gz"

# 网络图片的URL地址,调用demo前请填上内容
# The url of network picture, please fill in the contents before calling demo
face_one = 'http://bj-mc-prod-asset.oss-cn-beijing.aliyuncs.com/mc-official/images/face/demo-pic11.jpg'
# 本地图片的地址,调用demo前请填上内容
# Local picture location, please fill in the contents before calling demo
face_two = './demo.jpeg'
# 本地图片的地址,调用demo前请填上内容
# Local picture location, please fill in the contents before calling demo
face_search = './demo.jpeg'

# Import system libraries and define helper functions
# 导入系统库并定义辅助函数
from pprint import pformat

def print_result(hit, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(v): encode(k) for (v, k) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj
    print hit
    result = encode(result)
    print '\n'.join("  " + i for i in pformat(result, width=75).split('\n'))


# First import the API class from the SDK
# 首先，导入SDK中的API类
from facepp import API, File

api = API(API_KEY, API_SECRET)

#return_attributes=[gender, age, smiling, glass, headpose,facequality,blur]
res = api.detect(image_url=face_one, return_landmark = 1)
print res[u'faces']

res1 = api.detectsceneandobject(image_url=face_one)

