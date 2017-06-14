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

from MST import MST
import Pole
from Move import Move

#ioParams is None, category None for now, probability 0 to 1
sampleMove1 = Move(ioParams = None, probability = 0.1, category = None)
sampleMove2 = Move(ioParams = None, probability = 0.2, category = None)
sampleMove3 = Move(ioParams = None, probability = 0.3, category = None)
sampleMove4 = Move(ioParams = None, probability = 0.4, category = None)
sampleMove5 = Move(ioParams = None, probability = 0.5, category = None)
sampleMove6 = Move(ioParams = None, probability = 0.6, category = None)
sampleMove7 = Move(ioParams = None, probability = 0.7, category = None)
sampleMove8 = Move(ioParams = None, probability = 0.8, category = None)
sampleMove10 = Move(ioParams = None, probability = 0.9, category = None)

list = []
list.append(sampleMove1,sampleMove2,sampleMove3,sampleMove4,sampleMove5,sampleMove6,sampleMove7,sampleMove8,sampleMove9,sampleMove10)

#mst = MST(currentState = ({"A": 4}, {"B": 5}), desiredState = ({"A": 6}, {"B": 9}), moves = list, maxTime = 7)

#value = (-1,1), weight = (0,1)? (Tony says 0-1 for weight might not be enough)
RationalityPole = RationalityPole(-.5, .5)
RiskPole = RiskPole(-.3, .3)
ParticularHolisticPole = ParticularHolisticPole(-.4, .4)
PrimacyRecencyPole = PrimacyRecencyPole(-.2, .2)
RoutineCreativePole = RoutineCreativePole(-.1, .1)

print(RationalityPole.actonList(list))
print(RiskPole.actonList(list))
print(ParticularHolisticPole.actonList(list))
print(PrimacyRecencyPole.actonList(list))
print(RoutineCreativePole.actonList(list))

#print(RationalityPole.actonMST(mst))
#print(RiskPole.actonMST(mst))
#print(ParticularHolisticPole.actonMST(mst))
#print(PrimacyRecencyPole.actonMST(mst))
#print(RoutineCreativePole.actonMST(mst))