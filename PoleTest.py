#Make 10 sample Move objects, or however many you see fit in order to test,
# probably 10 is enough. Populate their properties with some straightforward values, that make the moves different.
# Make moves that have different values which make it clear which move a pole should eliminate,
# and which move a pole would leave (ie risk pole would eliminate super risky moves (depending on the value)).
#Put the above moves in a list.
#Initialize the pole objects that you are testing with some values and weights.
#Feed in the list of moves to pole.actOnList() (let actor just be None for now,
# that should be alright for some cases) and verify that behavior is as expected according to the pseudocode and design doc.
# The moves left in the list after the method returns should indicate whether this is true or not.
#Next, make an MST object from the list of moves. This will also require you to input a current state and a desired state.
# Again create these state objects purposely in order for testing clarity.
#Feed the MST into the actOnMST method of the Pole and see that the moves (paths) that are left after the method returns
# is as expected.
#Note any inconsistencies where methods don't work/don't return what is expected.

class sampleMove1(Move):
    def __init__(self, resources, infrastructure, ioParams, probability, risk):
        super().__init__(resources, infrastructure)
        self.ioParams = ioParams
        self.probability = probability
        self.risk = risk
        self.category = "" #category #need to make sure that we add this from somewhere

class sampleMove2(Move):
    def __init__(self, resources, infrastructure, ioParams, probability, risk):
        super().__init__(resources, infrastructure)
        self.ioParams = ioParams
        self.probability = probability
        self.risk = risk
        self.category = "" #category #need to make sure that we add this from somewhere

class sampleMove3(Move):
    def __init__(self, resources, infrastructure, ioParams, probability, risk):
        super().__init__(resources, infrastructure)
        self.ioParams = ioParams
        self.probability = probability
        self.risk = risk
        self.category = "" #category #need to make sure that we add this from somewhere

class sampleMove4(Move):
    def __init__(self, resources, infrastructure, ioParams, probability, risk):
        super().__init__(resources, infrastructure)
        self.ioParams = ioParams
        self.probability = probability
        self.risk = risk
        self.category = "" #category #need to make sure that we add this from somewhere

class sampleMove5(Move):
    def __init__(self, resources, infrastructure, ioParams, probability, risk):
        super().__init__(resources, infrastructure)
        self.ioParams = ioParams
        self.probability = probability
        self.risk = risk
        self.category = "" #category #need to make sure that we add this from somewhere

class sampleMove6(Move):
    def __init__(self, resources, infrastructure, ioParams, probability, risk):
        super().__init__(resources, infrastructure)
        self.ioParams = ioParams
        self.probability = probability
        self.risk = risk
        self.category = "" #category #need to make sure that we add this from somewhere

class sampleMove7(Move):
    def __init__(self, resources, infrastructure, ioParams, probability, risk):
        super().__init__(resources, infrastructure)
        self.ioParams = ioParams
        self.probability = probability
        self.risk = risk
        self.category = "" #category #need to make sure that we add this from somewhere

class sampleMove8(Move):
    def __init__(self, resources, infrastructure, ioParams, probability, risk):
        super().__init__(resources, infrastructure)
        self.ioParams = ioParams
        self.probability = probability
        self.risk = risk
        self.category = "" #category #need to make sure that we add this from somewhere

class sampleMove9(Move):
    def __init__(self, resources, infrastructure, ioParams, probability, risk):
        super().__init__(resources, infrastructure)
        self.ioParams = ioParams
        self.probability = probability
        self.risk = risk
        self.category = "" #category #need to make sure that we add this from somewhere

class sampleMove10(Move):
    def __init__(self, resources, infrastructure, ioParams, probability, risk):
        super().__init__(resources, infrastructure)
        self.ioParams = ioParams
        self.probability = probability
        self.risk = risk
        self.category = "" #category #need to make sure that we add this from somewhere

list = []
list.append(sampleMove1,sampleMove2,sampleMove3,sampleMove4,sampleMove5,sampleMove6,sampleMove7,sampleMove8,sampleMove9,sampleMove10)