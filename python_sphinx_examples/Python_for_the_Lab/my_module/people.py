'''
Module people
=============
Defines two classes, Pearson and Teacher.
You define a person by supplying a name, for example:

>>> me = Person('My Name')
>>>print(me.name)
My Name

'''


class Person:
    '''Class to store a general person information. For example the name.'''
    def __init__(self, name):
        '''Create a person object by providing a name.'''
        self.name = name
    

class Teacher(Person):
    '''Class to store a teacher's information. It subclasses :class:`Person`
    .'''
    def __init__(self, name, course):
        '''Create a teacher object by providing a name and the course they 
        teach.'''
        super().__init__(name)
        self.course = course

    def get_courses(self):
        '''Get the course they teach.'''
        return self.course

    def set_course(self, new_course):
        '''Set the course that they teach.'''
        self.course = new_course
    
