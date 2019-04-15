# -*- coding: utf-8 -*-
'''
Module people
=============
Defines two classes, Pearson and Teacher.
'''


class Person:
    '''Class to store a general persons information. For example the name.'''
    def __init__(self, name):
        '''Create a person object by providing a name.
        For example:

        >>> from people import Person
        >>> me = Person('My Name')
        >>> print(me.name)
        My Name

        :param name: The Name of a person
        :type name: str
        '''
        self.name = name


class Teacher(Person):
    '''Class to store a teacher's information. It subclasses :class:`Person`
    .'''
    def __init__(self, name, course):
        '''Create a teacher object by providing a name and the course they
        teach.

        :param name: The name of the person
        :type name: str
        :param course: The Name of the course they teach
        :type course: str
        '''
        super().__init__(name)
        self.course = course

    def get_courses(self):
        '''Get the course they teach.

        :return: The Name of the course the person teaches
        :rtype: str
        '''
        return self.course

    def set_course(self, new_course):
        '''Set the course that they teach.

        :param new_course: The new course name that they teach
        :type new_course: str
        '''
        self.course = new_course
