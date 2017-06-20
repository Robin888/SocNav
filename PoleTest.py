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
import unittest
import Pole

#ioParams is None, category None for now, probability 0 to 1
sampleMove1 = Move(ioParams = None, probability = 0.1, category = None,
    resources = resources.items((resource1, [1,3]), (resource2, [4,6]), (resource3, [7,9]), (resource4, [1,3])))
sampleMove2 = Move(ioParams = None, probability = 0.2, category = None,
    resources = resources.items((resource1, [4,6]), (resource2, [7,9]), (resource3, [1,3]), (resource4, [4,6])))
sampleMove3 = Move(ioParams = None, probability = 0.3, category = None,
    resources = resources.items((resource1, [7,9]), (resource2, [1,3]), (resource3, [4,6]), (resource4, [7,9])))
sampleMove4 = Move(ioParams = None, probability = 0.4, category = None,
    resources = resources.items((resource1, [4,6]), (resource2, [7,9]), (resource3, [7,9]), (resource4, [1,3])))
sampleMove5 = Move(ioParams = None, probability = 0.5, category = None,
    resources = resources.items((resource1, [4,6]), (resource2, [1,3]), (resource3, [1,3]), (resource4, [7,9])))
sampleMove6 = Move(ioParams = None, probability = 0.6, category = None,
    resources = resources.items((resource1, [1,3]), (resource2, [1,3]), (resource3, [4,6]), (resource4, [7,9])))
sampleMove7 = Move(ioParams = None, probability = 0.7, category = None,
    resources = resources.items((resource1, [1,3]), (resource2, [7,9]), (resource3, [4,6]), (resource4, [1,3])))
sampleMove8 = Move(ioParams = None, probability = 0.8, category = None,
    resources = resources.items((resource1, [4,6]), (resource2, [7,9]), (resource3, [4,6]), (resource4, [1,3])))
sampleMove10 = Move(ioParams = None, probability = 0.9, category = None,
    resources = resources.items((resource1, [7,9]), (resource2, [4,6]), (resource3, [7,9]), (resource4, [1,3])))

list = []
list.append(sampleMove1,sampleMove2,sampleMove3,sampleMove4,sampleMove5,sampleMove6,sampleMove7,sampleMove8,sampleMove9,sampleMove10

#mst = MST(currentState = ({"A": 4}, {"B": 5}), desiredState = ({"A": 6}, {"B": 9}), moves = list, maxTime = 7)

#value = (-1,1), weight = (0,1)? (Tony says 0-1 for weight might not be enough)
RationalityPole = RationalityPole(-.5, .5)
RiskPole = RiskPole(-.3, .3)
#ParticularHolisticPole = ParticularHolisticPole(-.4, .4)
#PrimacyRecencyPole = PrimacyRecencyPole(-.2, .2)
#RoutineCreativePole = RoutineCreativePole(-.1, .1)
#EmotionalPole = EmotionalPole(.6, .6)

print(RationalityPole.actonList(list))
print(RiskPole.actOnList(list))
#print(ParticularHolisticPole.actonList(list))
#print(PrimacyRecencyPole.actonList(list))
#print(RoutineCreativePole.actonList(list))
#print(EmotionalPole.actonList(list))

#print(RationalityPole.actOnMST(mst))
#print(RiskPole.actOnMST(mst))
#print(ParticularHolisticPole.actOnMST(mst))
#print(PrimacyRecencyPole.actonMST(mst))
#print(RoutineCreativePole.actonMST(mst))
#print(EmotionalPole.actonMST(mst))

#According to Tony: can test = RationalityPole-yes, RiskPole-yes, RoutineCreativePole-maybe, everything else-no

class TestPoleListMethod(unittest.TestCase):
    @patch(list)
    def test_RationalityList(list, actOnList):
        RationalityPole.actOnList(list)
        RationalityPole.actOnList.assert_called_with(list)
    def test_RiskList(list, actOnList):
        RiskPole.actOnList(list)
        RiskPole.actOnList.assert_called_with(list)
    def test_ParticularHolisticList(list, actOnList):
        ParticularHolisticPole.actOnList(list)
        ParticularHolisticPole.actOnList.assert_called_with(list)
    def test_PrimacyRecencyList(list, actOnList):
        PrimacyRecencyPole.actOnList(list)
        PrimacyRecencyPole.actOnList.assert_called_with(list)
    def test_RoutineCreativeList(list, actOnList):
        RoutineCreativePole.actOnList(list)
        RoutineCreativePole.actOnList.assert_called_with(list)
    def test_EmotionalList(list, actOnList):
        EmotionalPole.actOnList(list)
        RoutineCreativePole.actOnList.assert_called_with(list)

class TestPoleMSTMethod(unittest.TestCase):
    @patch(list)
    def test_RationalityMST(list, actOnMST):
        RationalityPole.actOnMST(list)
        RationalityPole.actOnMST.assert_called_with(list)
    def test_RiskList(list, actOnMST):
        RiskPole.actOnMST(list)
        RiskPole.actOnMST.assert_called_with(list)
    def test_ParticularHolisticList(list, actOnMST):
        ParticularHolisticPole.actOnMST(list)
        ParticularHolisticPole.actOnMST.assert_called_with(list)
    def test_PrimacyRecencyList(list, actOnMST):
        PrimacyRecencyPole.actOnMST(list)
        PrimacyRecencyPole.actOnMST.assert_called_with(list)
    def test_RoutineCreativeList(list, actOnMST):
        RoutineCreativePole.actOnMST(list)
        RoutineCreativePole.actOnMST.assert_called_with(list)
    def test_EmotionalList(list, actOnMST):
        EmotionalPole.actOnMST(list)
        RoutineCreativePole.actOnMST.assert_called_with(list)

if __name__ == '__main__':
    unittest.main()