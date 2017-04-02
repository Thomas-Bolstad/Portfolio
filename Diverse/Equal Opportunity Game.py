#Equal opportunity game
import random, string, time

class Match:

    def __init__(self, players):
        self.money = [20 for i in range(players)]

    def Game(self):
        money = self.money
        notplayed = range(len(money))
        for i in range(len(money) / 2):
            player2 = int((random.random() - 1)*(len(notplayed) - 1))
            notplayed.pop(0)
            notplayed.pop(player2 - 1)
            totmoney = money[0] + money[player2]
            money[0] = int((1 -random.random())*totmoney)
            money[player2] = totmoney - money[0]

    def _Format(self, distr, money):
        newformat = []
        maxD = len(str(max(distr)))
        for element in range(len(distr)):
            value = distr[element]
            amount = money[element]
            white1 = maxD - len(str(value))
            new = "% 0.4s %0.2s: % 4.5s" % (value, " "*white1, amount)
            newformat.append(new)
        return newformat

    def GetMoney(self, steps):
        newlist = [0 for i in range(steps)]
        moneylist, tresh2 = [], 0
        money = self.money
        biggest = float(max(money))
        for i in range(len(newlist)):
            tresh1 = biggest*(i + 1) / steps
            for element in money:
                if element <= tresh1 and element >= tresh2:
                    newlist[i] += 1
            tresh2 = tresh1
            str_tresh1 = string.split(str(tresh1), ".")
            str_tresh1[1] = str_tresh1[1][0:2] + "0"*(2 - len(str_tresh1[1]))
            str_tresh1 = string.join(str_tresh1, ".")
            moneylist.append(str_tresh1)
        formatted = self._Format(newlist, moneylist)
        return formatted


    
players = 5000
matches = 1000
steps = 25
tid_1 = time.time()
def main():
    game = Match(players)
    for i in range(matches):
        game.Game()
    formatted = game.GetMoney(steps)
    for element in formatted:
        print element
    tid_2 = time.time()
    print "tid:", tid_2 - tid_1

if __name__ == "__main__":
    main()
