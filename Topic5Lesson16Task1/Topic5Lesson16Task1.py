class boxOffice:
    def __init__(self, money):
        self.money = money
 
    def top_up(self, x):
        self.money += x
        return f'Внесена сумма в кассу {x} рублей, в кассе сейчас {self.money} рублей.'
    
    def count_1000(self):
        return f'В кассе сейчас {self.money // 1000} купюр(-ра/-ры) по тысяче рублей.'
 
    def take_away(self, x):
        if x <= self.money:
            self.money -= x
            return f'Из кассы выдано {x} рублей, в кассе осталось {self.money} рублей.'
        else:
            return f'Не достаточно денег.'
        

boxOffice1 = boxOffice(1000)
print(boxOffice1.top_up(1000))
print(boxOffice1.count_1000())
print(boxOffice1.take_away(900))
