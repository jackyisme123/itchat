import requests
import itchat

key = '8edce3ce905a4c1dbb965e6b35c3834d'
apiUrl = 'http://www.tuling123.com/openapi/api'

def get_response(msg):
    data = {
        'key'    : key, # 如果这个Tuling Key不能用，那就换一个
        'info'   : msg, # 这是我们发出去的消息
        'userid' : 'jacky', # 这里你想改什么都可以
    }
    # 我们通过如下命令发送一个post请求
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except Exception as e:
        print(e)
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'I received: ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
    reply = get_response(msg['Text'])
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
    return reply or defaultReply

itchat.auto_login(hotReload=True)
itchat.run()
