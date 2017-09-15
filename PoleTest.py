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
import Actor

Actor.error = 0.5

#ioParams is None, category None for now, probability 0 to 1
sampleMove1 = Move(ioParams = -1, probability = 0.1, category = None,
    resources = {resource1: [1,3], resource2: [1,3], resource3: [1,3], resource4: [1,3]}
sampleMove2 = Move(ioParams = -.8, probability = 0.1, category = None,
    resources = {resource1: [7,9], resource2: [7,9], resource3: [7,9], resource4: [7,9]}
sampleMove3 = Move(ioParams = -.6, probability = 0.9, category = None,
    resources = {resource1: [1,3], resource2: [1,3], resource3: [1,3], resource4: [1,3]}
sampleMove4 = Move(ioParams = -.4, probability = 0.9, category = None,
    resources = {resource1: [4,6], resource2: [4,6], resource3: [4,6], resource4: [4,6]}
sampleMove5 = Move(ioParams = -.2, probability = 0.2, category = None,
    resources = {resource1: [1,3], resource2: [1,3], resource3: [1,3], resource4: [1,3]}
sampleMove6 = Move(ioParams = 0, probability = 0.8, category = None,
    resources = {resource1: [1,3], resource2: [1,3], resource3: [1,3], resource4: [1,3]}
sampleMove7 = Move(ioParams = .2, probability = 0.3, category = None,
    resources = {resource1: [4,6], resource2: [4,6], resource3: [4,6], resource4: [4,6]}
sampleMove8 = Move(ioParams = .4, probability = 0.7, category = None,
    resources = {resource1: [7,9], resource2: [7,9], resource3: [7,9], resource4: [7,9]}
sampleMove9 = Move(ioParams = .6, probability = 0.1, category = None,
    resources = {resource1: [4,6], resource2: [4,6], resource3: [4,6], resource4: [4,6]}
sampleMove10 = Move(ioParams = .8, probability = 0.2, category = None,
    resources = {resource1: [7,9], resource2: [7,9], resource3: [7,9], resource4: [7,9]}

sampleMove1.howSuccessfulWasMove = -1
sampleMove2.howSuccessfulWasMove = -.8
sampleMove3.howSuccessfulWasMove = -.6
sampleMove4.howSuccessfulWasMove = -.4
sampleMove5.howSuccessfulWasMove = -.2
sampleMove6.howSuccessfulWasMove = 0
sampleMove7.howSuccessfulWasMove = .2
sampleMove8.howSuccessfulWasMove = .4
sampleMove9.howSuccessfulWasMove = .6
sampleMove10.howSuccessfulWasMove = 1

list = []
list.append(sampleMove1,sampleMove2,sampleMove3,sampleMove4,sampleMove5, sampleMove6, sampleMove7, sampleMove8, sampleMove9, sampleMove10)
memory = []
memory.append(sampleMove1, sampleMove2, sampleMove3, sampleMove4, sampleMove5, sampleMove6)
mst = MST(currentState = ({"A": 4}, {"B": 5}), desiredState = ({"A": 6}, {"B": 9}), moves = list, maxTime = 7)

#value = (-1,1), weight = (0,1)? (Tony says 0-1 for weight might not be enough)
RationalityPole = RationalityPole(.3, .5)
RiskPole = RiskPole(.5, .5)
ParticularHolisticPole = ParticularHolisticPole(-.4, .4)
PrimacyRecencyPole = PrimacyRecencyPole(-.2, .2)
RoutineCreativePole = RoutineCreativePole(.1, .1)
EmotionalPole = EmotionalPole(.6, .6)
GenerosityPole = GenerosityPole(.4,.4)

#According to Tony: can test = RationalityPole-yes, RiskPole-yes, RoutineCreativePole-maybe, everything else-no

class TestPoleListMethod(unittest.TestCase):
    def test_RationalityList(self, list, actOnList):
        list2 = RationalityPole.actOnList(list)
        list2.assertEquals(list)
        #len(nl)*(self.value + actor.error) <= move.ioParams.value = remove, remove moves, no moves will be removed (multiply by len(nl) vs ioParams = [-1,1]

    def test_RiskList(self, list, actOnList):
        list2 = RiskPole.actOnList(list)
        print(actor.error)
        list2.assertEquals(list) #should return same list

    #def test_ParticularHolisticList(self, list, actOnList): k-means? clarification, iovalues
        #ParticularHolisticPole.actOnList(list)
        #ParticularHolisticPole.actOnList.assert_called_with(list)

    #def test_PrimacyRecencyList(self, list, actOnList): set history and memory manually, need pmesii excel file
        #history = list
        #memory = memory
        #PrimacyRecencyPole.actOnList(list)
        #PrimacyRecencyPole.actOnList.assert_called_with(list)

    def test_RoutineCreativeList(self, list, actOnList):
        list2 = RoutineCreativePole.actOnList(list)
        list2.assertEquals(list.remove(sampleMove6, sampleMove7, sampleMove8, sampleMove9, sampleMove10))
        #actor.howSuccessfulWasMove(move) > (actor.howSuccessfulWasMove(move) summed over all moves)/len(oldMoves) = remove moves 6, 7, 8, 9, 10

    #def test_EmotionalList(self, list, actOnList):
        #EmotionalPole.actOnList(list)
        #RoutineCreativePole.actOnList.assert_called_with(list)
        #need to see moveCategories before proceeding, no category?

    def test_GenerosityList(self, list, actOnList):
        list2 = GenerosityPole.actOnList(list)
        list2.assertEquals(list.remove(sampleMove2, sampleMove8, sampleMove10, sampleMove4, sampleMove7, sampleMove9))
        #move.sum > ( ((abs(self.value) / 2) + 0.5) * self.maxListPrice) + actor.error), remove moves 2, 8, 10, maybe 4, 7, 9 (depends on random resources)

class TestPoleMSTMethod(unittest.TestCase):
    def test_RationalityMST(self, mst, actOnMST):
        mst2 = RationalityPole.actOnMST(mst)
        mst2.assertEquals(mst.remove(sampleMove1,sampleMove2, sampleMove5, sampleMove7, sampleMove8, sampleMove9, sampleMove10))
        #move.probability < (self.value + actor.error) (= .3 + .5 = .8) removed, sampleMoves 1, 2, 5, 7, 8, 9, 10 should be removed

    def test_RiskMST(self, mst, actOnMST):
        mst2 = RiskPole.actOnMST(mst)
        mst2.assertEquals(mst.remove(sampleMove1))
        #move.risk < self.value + actor.error (.5 + .5 = 1) removed, sampleMove1 should be removed

    def test_ParticularHolisticMST(self, mst, actOnMST):
        mst2 = ParticularHolisticPole.actOnMST(mst)
        mst2.assertEquals(mst)
        #should return same mst

    #def test_PrimacyRecencyMST(self, mst, actOnMST): need to set history? event.compareTo--event class? need pmesii
        #PrimacyRecencyPole.actOnMST(mst)
        #PrimacyRecencyPole.actOnMST.assert_called_with(mst)

    def test_RoutineCreativeMST(self, mst, actOnMST):
        mst2 = RoutineCreativePole.actOnMST(mst)
        mst2.assertEquals(mst.remove(sampleMove5,sampleMove3,sampleMove7))
        #rnum > (self.value + actor.error) (.1 + .5 = .6) removed, randomly removes moves, I picked randomly here

    #def test_EmotionalMST(self, mst, actOnMST):
        #mst2 = EmotionalPole.actOnMST(mst)
        #mst2.assertEquals(mst)
        #need to see moveCategories before proceeding, need category

    #def test_GenerosityMST(self, mst, actOnMST):
        #mst2 = GenerosityPole.actOnMST(mst)
        #mst2.assertEquals(mst)
        #Incomplete, can't test yet

if __name__ == '__main__':
    unittest.main()