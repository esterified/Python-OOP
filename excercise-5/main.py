class Course:
    def __init__(self,title, instructor, price, lectures, users, ratings, avg_rating):
        self.title=title
        self.instructor=instructor
        self.price=price
        self.lectures=lectures
        self.users=users
        self.ratings=ratings
        self.avg_rating=avg_rating
        
    def __str__(self):
        ##test
        return f'{self.title}\n{self.price}'
        
    def new_user_enrolled(self,name): 
        if name not in users:
            return(True)
        else:
            return(False)

    def received_a_rating(self):
        pass
    def _show_details(self):
        print(self.title)
        print(self.instructor)
        print(self.price)
        print(self.lectures)
        print(self.users)
        print(self.ratings)
        print(self.avg_rating)
        

class VideoCourse(Course):

    def __init__(self,title, instructor, price, lectures, users, ratings, avg_rating, length_video):
        Course.__init__(self,title, instructor, price, lectures, users, ratings, avg_rating)    
        self.length_video=length_video
     

class PdfCourse(Course):
    def __init__(self,title, instructor, price, lectures, users, ratings, avg_rating,pages):
        super().__init__(title, instructor, price, lectures, users, ratings, avg_rating)    
        self.pages=pages
p=VideoCourse("a","b","c","d",["fayed","ishtar"],"f","g","h") 
p1=PdfCourse("a","b","c","d",["fayed","ishtar"],"f","g","h")
print(p1)
##new
class Mother:
        def cook(self):
           print('Can cook pasta')
 
class Father:
        def cook(self):
             print('Can cook noodles')
 
class Daughter(Father, Mother):
          pass
 
class Son(Mother, Father):
         def cook(self):
             super().cook()
             print('Can cook butter chicken') 
 
d = Daughter()  
s = Son()
 
d.cook()
print()
s.cook()


### to see the MRO help(Son) 
class Person:
    def greet(self):
        print('I am a Person')
 
class Teacher(Person):
    def greet(self):
        Person.greet(self)    
        print('I am a Teacher')
 
class Student(Person):
    def greet(self):
        Person.greet(self)    
        print('I am a Student')
 
class TeachingAssistant(Student, Teacher):
     def greet(self):
         super().greet()
         print('I am a Teaching Assistant')
       
x = TeachingAssistant()
x.greet()
##IMPORTANT problem

##########     my solution #################
class Person:
    def __init__(self,id):
        self.id = id
        
class Teacher(Person):
    def __init__(self,id):
        Person.__init__(self,id)
        #print('beforeT '+self.id)
        self.id += 'T'
        #print('afterT '+self.id)
class Student(Person):
    def __init__(self,id):
        Person.__init__(self,id)
        #print('beforeS '+self.id)
        self.id += 'S'
        #print('afterS '+self.id)
class TeachingAssistant(Student, Teacher):
     def __init__(self,id):
        Student.__init__(self,id)
        Teacher.__init__(self,self.id)###############change in  this line ##############
       
x = TeachingAssistant('2675')
print(x.id)
y = Student('4567')
print(y.id)
z = Teacher('3421')
print(z.id)
p = Person('5749')
print(p.id)
#########    alternate soln using     super()           ##############
class Person:
    def __init__(self,id):
        self.id = id
        
class Teacher(Person):
    def __init__(self,id):
        super().__init__(id)
        self.id += 'T'
    
class Student(Person):
    def __init__(self,id):
        super().__init__(id)
        self.id += 'S'
   
class TeachingAssistant(Student, Teacher):
     def __init__(self,id):
        super().__init__(id)
        
   
x = TeachingAssistant('2675')
print(x.id)
y = Student('4567')
print(y.id)
z = Teacher('3421')
print(z.id)
p = Person('5749')
print(p.id)

