import classA
import classB

class ClassC():
    def __init__(self):
        '''!@brief Creates a ClassC object

        This ClassX object is being used as a DoxyGen/Docstring/Python example. This class instantiates a ClassX and ClassY class
        and holds them internally.
        '''
        self.X = classA.ClassA(0xDEAD)
        self.Y = classB.ClassB(0xFEED)

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
        self.X.var_set_A(0x0)
        self.Y.var_set_B(0x0)

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