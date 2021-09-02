class Duck:
    def talk(self):
        print("quack quack")
class Human:
    def talk(self):
        print("Hello, how are you?")
def callTalk(obj):
    obj.talk()
d=Duck()
callTalk(d)
h=Human()
callTalk(h)