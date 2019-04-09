
class ClassX():
    def __init__(self, instantA, instantB=0x8BAD):
        '''!@brief Creates a Class X object

        This ClassX object is being used as a DoxyGen/Docstring/Python example

        @param instantA An integer value
        @param instantB An integer value with a default of 0x8BAD
        '''
        self.instA = instantA
        self.instB = instantB

    def var_print(self):
        '''
        !@brief Method that prints the current value of the two internal variables
        
        This method prints to the console the current value of all internal variables with no formatting
        '''
        print(self.instA)
        print(self.instB)

    def var_reset(self):
        '''
        !@brief Method resets all internal variables to zero 
        '''
        self.var_set_A(0)
        self.var_set_B(0)

    def var_set_A(self, variable):
        '''
        !@brief Set the vale of the internal variable instA

        This method will set the value of the internal variable, instA, to the value passed in to this method

        @param variable Interger value that instA will be set to
        '''
        self.instA = variable

    def var_set_B(self, variable):
        '''
        !@brief Set the vale of the internal variable instB

        This method will set the value of the internal variable, instB, to the value passed in to this method

        @param variable Interger value that instB will be set to
        '''
        self.instB = variable


class ClassY():
    def __init__(self, instantA, instantB=0xBEEF):
        '''!@brief Creates a Class Y object

        This ClassY object is being used as a DoxyGen/Docstring/Python example

        @param instantA An integer value
        @param instantB An integer value with a default of 0xBEEF
        '''
        self.instA = instantA
        self.instB = instantB

    def var_print(self):
        '''
        !@brief Method that prints the current value of the two internal variables
        
        This method prints to the console the current value of all internal variables with no formatting
        '''
        print(self.instA)
        print(self.instB)

    def var_reset(self):
        '''
        !@brief Method resets all internal variables to zero 
        '''
        self.var_set_A(0x0)
        self.var_set_B(0x0)

    def var_set_A(self, variable):
        '''
        !@brief Set the vale of the internal variable instA

        This method will set the value of the internal variable, instA, to the value passed in to this method

        @param variable Interger value that instA will be set to
        '''
        self.instA = variable

    def var_set_B(self, variable):
        '''
        !@brief Set the vale of the internal variable instB

        This method will set the value of the internal variable, instB, to the value passed in to this method

        @param variable Interger value that instB will be set to
        '''
        self.instB = variable

    def var_increment(self, increment):
        '''
        !@brief Incremenmt the internal values by Incrememnt 

        Increment both internal variables, instA and instB by the value of increment

        @param increment Interger value that will be added to instA and instB
        '''
        self.instA += increment
        self.instB += increment


class ClassZ():
    def __init__(self):
        '''!@brief Creates a Class Z object

        This ClassX object is being used as a DoxyGen/Docstring/Python example. This class instantiates a ClassX and ClassY class
        and holds them internally.
        '''
        self.X = ClassX(0xDEAD)
        self.Y = ClassY(0xFEED)

    def var_print(self):
        '''
        !@brief Method that prints the current value all internal classes
        
        This method prints to the console the current value of all internal variables with no formatting
        '''
        self.X.var_print()
        self.Y.var_print()

    def var_reset(self):
        '''
        !@brief Method resets all internal variables of both classes
        '''
        self.X.var_reset()
        self.Y.var_reset()

    def var_set(self, var0, var1):
        '''
        !@brief Method resets all internal variables of both classes

        This method sets the internal variables of the two classes in some form or another
            Below are how internal variables are set:

                self.X.var_set_A(var0 - var1)
                self.X.var_set_B(var1 - var0)
                self.Y.var_set_A(var0 + var1)
                self.Y.var_set_B(var0 * var1) 

        @param var0 First variable, integer please
        @param var1 Second variable, integer please
        '''
        self.X.var_set_A(var0 - var1)
        self.X.var_set_B(var1 - var0)
        self.Y.var_set_A(var0 + var1)
        self.Y.var_set_B(var0 * var1)        

    def var_incrementA(self, increment):
        '''
        !@brief Incrememnts instA of both internal classes

        @param increment Value to increment instA by
        '''
        self.X.instA += increment
        self.Y.instA += increment

    def var_incrementB(self, increment):
        '''
        !@brief Incrememnts instB of both internal classes

        @param increment Value to increment instB by
        '''
        self.X.instB += increment
        self.Y.instB += increment

    def sum_all(self):
        '''
        !@brief sums all internal instA and instB and then returns

        This methods grabs all of the internal variables from each class and then sums them

        @return summation The total value of all internal variables
        '''
        summation = self.X.instA
        summation += self.X.instB
        summation += self.Y.instA
        summation += self.Y.instB
        return summation
        