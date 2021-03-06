class ClassB():
    def __init__(self, instantA, instantB=0xBEEF):
        '''!@brief Creates a ClassB object

        This ClassX object is being used as a DoxyGen/Docstring/Python example

        @param instantA An integer value
        @param instantB An integer value: default of 0x8BAD
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