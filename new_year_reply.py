import threading
import itchat
import random

replies = [
    '二郎神找不到他的神犬啦，原来是跑到你的身边，在你看不见的地方守护着你，陪伴你度过平安吉祥如意的狗年。',
    '狗新年天气预报：你将会遇到金钱雨、幸运风、友情雾、爱情露、健康霞、幸福云、顺利霜、美满雷、安全雹、开心闪、请注意它们将会缠绕着你整一年。',
    '金犬纷纷滚滚来，开门迎犬纳大财。吉祥如意银光闪，大好河山锦绣程。银光大道在眼前，扬帆起航冲险浪。奋勇前进达彼岸，福汪滚滚多多赚。愿你狗年财运亨通! ',
    '狗儿欢声叫，腊梅开怀笑。白雪迎春到，幸福身旁绕。狗年乐淘陶，祝福不能少。阳光暖暖照，心情无限好。事业步步高，容颜永娇俏。幸福指数高，爱情永不老。狗年快乐!',
    '金鸡辞岁千家乐，神犬迎春喜事多。齐心合力谋发展，大展宏图抢争先。新年团圆合家欢，亲朋好友尽开颜。',
    '幸福卫星跟踪你，快乐导弹瞄准你，财富墙支指向你，祝福子弹围剿你，幸福新年向你开炮：狗年吉祥! ',
    '万象更新狗儿喜，喜气盈门狗儿乐，平安狗儿乐淘淘，福禄寿泰财各路狗儿报春到，给您拜年送吉兆!',
    '白雪迎狗年，祥瑞降人间。欢乐太平年，幸福不间断。美丽丰收年，万户笑开颜。甜蜜美满年，家家乐翩翩。喜气庆狗年，祝福满心田。愿你狗年大吉大利，万事如意!',
    '感谢您的新春祝福， 我在此也祝福您和您的家人，狗年吉祥， 阖家幸福，身体健康，好运连连。 崔原敬上!'
]
user = []
AUTO_SEND_TIME = 60

@itchat.msg_register(itchat.content.TEXT)
def newyear_reply(msg):
    receive = msg['Text']
    if '狗年' in receive or '祝' in receive or '大吉' in receive or '幸福' in receive or '身体健康' in receive \
            or '阖家' in receive or '新年' in receive or '拜年' in receive:
        n = random.randint(0, 8)
        if msg['FromUserName'] in user:
            return
        else:
            user.append(msg['FromUserName'])
            return replies[n]

class ThreadJob(threading.Thread):
    def __init__(self, callback, event, interval):
        self.callback = callback
        self.event = event
        self.interval = interval
        super(ThreadJob, self).__init__()
        self.is_running = False

    def run(self):
        while not self.event.wait(self.interval):
            self.callback()
            self.is_running = True

def heartbeat():
    itchat.send('Heartbeat', 'filehelper')

k = ThreadJob(heartbeat, threading.Event(), AUTO_SEND_TIME)
if not k.is_running:
    k.start()
itchat.auto_login(hotReload=True)
itchat.run()


