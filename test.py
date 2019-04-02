print ("Hello World\n")

print ("あなたは仕事が辛いですか？\n")
print ("はい：いいえ")

death = input()

if (death == "はい") :
    print ("明日は有給取って休んでください")

elif (death == "いいえ") :
    print ("そんな事を言っていられるのも今のうちだ")

else :
    print ("はい　か　いいえで答えろよくそ")


class test():
    def __init__ (self, message):
        self.message = message

print ("あなたのグチをどうぞ！")
message = input()
print (test(message).message)
print ("\nそうですか分かりました")