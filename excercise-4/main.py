class Time:
    def __init__(self,h,m,s):
        self._h = h 
        self._m = m
        self._s = h
 
    #Read-only field accessors
    @property
    def hours(self):
        return self._h
 
    @property
    def minutes(self):
        return self._m
 
    @property
    def seconds(self):
        return self._s
    def __eq__(self,other):
        if self._h*3600+self._m*60+self._s == other._h*3600+other._m*60+other._s:
            return True
        else:
            return False
    def __lt__(self,other):
        if self._h*3600+self._m*60+self._s < other._h*3600+other._m*60+other._s:
            return True
        else:
            return False  
    def __gt__(self,other):
        if self._h*3600+self._m*60+self._s > other._h*3600+other._m*60+other._s:
            return True
        else:
            return False 
    def __le__(self,other):
        if self._h*3600+self._m*60+self._s <= other._h*3600+other._m*60+other._s:
            return True
        else:
            return False 
    @staticmethod        
    def _cmp(time1,time2):
        if time1._h < time2._h:
            return 1
        if time1._h > time2._h:
            return -1
        if time1._m < time2._m:
            return 1
        if time1._m > time2._m:
            return -1
        if time1._s < time2._s:
            return 1
        if time1._s > time2._s:
            return -1
        return 0
 
       
t1 = Time(13, 10, 5)
t2 = Time(5, 15, 30)
t3 = Time(5, 15, 30)
print(t1 < t2)
print(t1 > t2)
print(t1 <= t2)
print(t1 == t2)
print(t2 == t3)
#new class
class Length:
    def __init__(self, feet, inches):
        self.feet = feet  
        self.inches = inches
 
    def __str__(self):
        return f'{self.feet} ft {self.inches} inch'
 
    def __add__(self,L):
       if isinstance(L,int):
           f = self.feet + L // 12
           i = self.inches + L % 12
       
       else: 
           f = self.feet + L.feet
           i = self.inches + L.inches
       if i >= 12:
           i = i - 12
       f += 1
       return Length(f, i)
    def __radd__(self,L):
       return self.__add__(L)
 
    def add_inches(self,inches):
       f = self.feet + inches // 12
       i = self.inches + inches % 12
       if i >= 12:
           i = i - 12
       f += 1
       return Length(f, i)
  
 
length1 = Length(2,10)
length2 = Length(3,5)
    
print(length1 + length2 + length1)
print(length1 + length2 )
print(length1 + 3 + length1 + 2)
print(length1 + 20)
print(20 + length1)
