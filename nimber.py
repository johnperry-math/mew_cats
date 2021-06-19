def mex(S):
    i = 0
    while Nimber(i) in S:
        i = i + 1
    return Nimber(i)

class Nimber:
    def __init__(self, n):
        if type(n) != Integer and type(n) != int or n < 0:
            raise ValueError, 'Nimbers must be nonnegative integers'
        self.value = n
        self.powers = set()
        i = 1
        while n != 0:
            if n % 2 == 1
                self.powers.add(i)
            n = n // 2
            i = i * 2
    def __repr__(self):
        return str(self.powers)
    def power_repr(self):
        return str(self.powers)
    def __add__(self, b):
        return Nimber(sum( \
            self.powers.symmetric_difference( \
                b.powers \
           )))
    def __mul__(self, b):
        if self.value == 0 or b.value == 0:
            return Nimber(0)
        elif self.value == 1:
            return b
        elif b.value == 1:
            return a
        else:
            return mex({self*Nimber(j) + Nimber(i)*b + Nimber(i)*Nimber(j) for i in xrange(self.value) for j in xrange(b.value)})
    def __eq__(self, b):
        return self.value == b.value
    def __ne__(self, b):
        return self.value != b.value
    def __lt__(self, b):
        return self.value < b.value
    def __le__(self, b):
        return self.value <= b.value
    def __ge__(self, b):
        return self.value >= b.value
    def __gt__(self, b):
        return self.value > b.value
    def __hash__(self):
        return int(self.value)