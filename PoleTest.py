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

sampleMove1 = Move(ioParams = , probability = , risk = )
sampleMove2 = Move(ioParams = , probability = , risk = )
sampleMove3 = Move(ioParams = , probability = , risk = )
sampleMove4 = Move(ioParams = , probability = , risk = )
sampleMove5 = Move(ioParams = , probability = , risk = )
sampleMove6 = Move(ioParams = , probability = , risk = )
sampleMove7 = Move(ioParams = , probability = , risk = )
sampleMove8 = Move(ioParams = , probability = , risk = )
sampleMove10 = Move(ioParams = , probability = , risk = )

list = []
list.append(sampleMove1,sampleMove2,sampleMove3,sampleMove4,sampleMove5,sampleMove6,sampleMove7,sampleMove8,sampleMove9,sampleMove10)

mst = MST(currentState = , desiredState = ,moves = list, maxTime = )

RationalityPole = RationalityPole( , )
RiskPole = RiskPole( , )
ParticularHolisticPole = ParticularHolisticPole( , )
PrimacyRecencyPole = PrimacyRecencyPole( , )
RoutineCreativePole = RoutineCreativePole( , )
EmotionalPole = EmotionalPole( , )

print(RationalityPole.actonList(list))
print(RationalityPole.actonMST(mst))

print(RiskPole.actonList(list))
print(RiskPole.actonMST(mst))

print(ParticularHolisticPole.actonList(list))
print(ParticularHolisticPole.actonMST(mst))

print(PrimacyRecencyPole.actonList(list))
print(PrimacyRecencyPole.actonMST(mst))

print(RoutineCreativePole.actonList(list))
print(RoutineCreativePole.actonMST(mst))

print(EmotionalPole.actonList(list))
print(EmotionalPole.actonMST(mst))