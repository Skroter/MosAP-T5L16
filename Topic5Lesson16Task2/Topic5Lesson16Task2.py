class turtle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self): # увеличивает y на s
        self.y += self.s
    
    def go_down(self): # уменьшает y на s
        self.y -= self.s
        
    def go_left(self): # уменьшает x на s
        self.x -= self.s
        
    def go_right(self): # увеличивает y на s
        self.y += self.s
        
    def evolve(self): # увеличивает s на 1
        self.s += 1

    def degrade(self): # уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
        if self.s <= 0:
            return f"Недопустимое значение условием. Error"
        self.s -= 1
        
    def count_moves(self, x2, y2): # возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции
        if x2 % self.s == 0: 
            return (x2 % self.s)
        return (x2 % self.s + 1)
        if y2 % self.s == 0: 
            return (y2 % self.s)
        return (y2 % self.s + 1)
