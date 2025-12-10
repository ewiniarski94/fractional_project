from dataclasses import dataclass

@dataclass
class Fractional:
    x: int
    y: int

    def __add__(self, other: 'Fractional') -> 'Fractional':
        num = self.x * other.y + self.y * other.x
        denom = self.y * other.y
        return Fractional(num, denom)
    
    def __mul__(self, other: 'Fractional') -> 'Fractional':
        # return self.x * other.x, self.y * other.y
        num = self.x * other.x
        denom = self.y * other.y
        return Fractional(num, denom)
    
    def __sub__ (self, other: 'Fractional') -> 'Fractional':
        num = self.x * other.y - self.y * other.x
        denom = self.y * other.y
        return Fractional(num, denom)
    
    def __truediv__ (self, other: 'Fractional') -> 'Fractional':
        if other.y == 0:
            raise ZeroDivisionError("It's not possible to divide by zero!")
        num = self.x * other.y
        denom = self.y * other.x
        return Fractional(num, denom)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Fractional):
            return False
        return self.x * other.y == self.y * other.x
    
    def __lt__(self, other: 'Fractional') -> bool:
        return self.x * other.y < self.y * other.x
    
    def __le__(self, other: 'Fractional') -> bool:
        return self.x * other.y <= self.y * other.x
    
    def __gt__(self, other: 'Fractional') -> bool:
        return self.x * other.y > self.y * other.x

    def __ge__(self, other: 'Fractional') -> bool:
        return self.x * other.y >= self.y * other.x