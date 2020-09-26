from BankAccount import BankAccount
class Fraction:
  def __init__(self,nr,dr=1):

    if(nr<0 and dr<0)or(nr>-1 and dr<0):
      self.nr=-nr
      self.dr=-dr
    else:
      self.nr=nr
      self.dr=dr 
  def show(self):
    print(f'{self.nr}/{self.dr}')
  def multiply(self,nd):
    if isinstance(nd,int):
      nd=Fraction(nd)
    nr=self.nr*nd.nr
    dr=self.dr*nd.dr
    return Fraction(nr,dr)
  def add(self,nd):
    if isinstance(nd,int):
      nd=Fraction(nd)

    nr=(self.nr*nd.dr+ nd.nr*self.dr)
    dr=self.dr*nd.dr
    return Fraction(nr,dr)

class Book:
  def __init__(self,isbn,title,author,publisher,pages,price,copies):
    self.isbn=isbn
    self.title=title
    self.author=author
    self.publisher=publisher
    self.pages=pages
    self.price=price
    self.copies=copies
    
  def display(self):
    print(self.isbn)
    print(self.title)  
    print(self.author)
    print(self.publisher)
    print(self.pages)
    print(self.price)
    print(self._price)
    print(self.copies)
  def in_stock(self):
    if(self.copies>0):
      return True
    else:
      return False
  def sell(self):
    if(self.in_stock()):
      self.copies-=1
      print('copies available',self.copies)
    else:
      print('out of stock')
  
  @property
  def price(self):
    return self._price
    
  @price.setter
  def price(self,x):
    if 50 < x < 1000:
      self._price = x
    else:
      raise ValueError('asdasd')
  

a=BankAccount('fayed',200)
a.display()
book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)
book1.display()
book1.sell()
books=[book1,book2,book3,book4]
for i in range (4):
  books[i].display()
book_title_list=[books[i].title for i in range (4)]
print(book_title_list)
a = Fraction(-2)
a.show()
f1 = Fraction(2,3)
f1.show()
f2 = Fraction(3,4)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5) 
f3.show()
f3 = f1.multiply(5) 
f3.show()
class Product():
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self.discount = discount
    
    def display(self):
        print(self.id,  self.marked_price,  self.discount)
    @property
    def selling_price(self):
      return self.marked_price-(self.discount*self.marked_price/100)
    @property
    def discount(self):
      return self._discount
    @discount.setter
    def discount(self,d):
      if self.marked_price>500:
        self._discount=d+2
      else:
        self._discount=d
      
      
p1 = Product('X879', 400, 6)
p2 = Product('A234', 100, 5)
p3 = Product('B987', 990, 4)
p4 = Product('H456', 800, 6)
print(p3.selling_price)
class Circle:
  
  def __init__(self,radius):
    self.radius=radius

  def area(self):
    return 3.14*self.radius*self.radius
  @property
  def circum(self):
    return 2*3.14*self.radius
  @property
  def diameter(self):
    return 2*self.radius
  @property
  def radius(self):
   return self._radius
  @radius.setter
  def radius(self,x):
    if(x<0):
      raise AttributeError("radius cannot be negative")
    else:
      self._radius=x
c1=Circle(4)
print(c1.area())
print(c1.diameter)
print(c1.circum)
