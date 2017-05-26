from operator import attrgetter
import abc
import numpy as np
import math
from MST import MST
from random import *
'''
This is the superclasss for all poles. Classes inheriting from this class must define a method act.
'''
class Pole(object, metaclass = abc.ABCMeta):
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    @abc.abstractmethod
    def actOnMST(self, mst, actor):
        return

    @abc.abstractmethod
    def actOnList(self, orderedList, actor):
        return
'''
The following classes inherit from the Pole superclass above. They all must define a method act. Whenever there is an error term used, this should be the actor.error.
'''

class RationalityPole(Pole):
    def __init__(self, value, weight):
        super(RationalityPole, self).__init__(value, weight)

    def actOnList(self, orderedList, actor):
        # rationality: a rational actor will consider moves that cost less. 100% rationality actor will want as close to zero as possible, plus an error term
        # work with ordered list of moves
        nl = sorted(orderedList, key= attrgetter('resources')) # order moves based on cost (absolute value of resources deployed), with "cheapest" moves first
        tempval = len(nl)*(self.value + actor.error) # scale the value of the pole by the length of the list, keep the first (*value* + errorTerm) amount of moves in the list
        for move in nl:
            if tempval <= move.ioParams.value: #first amount of moves in the list that have values that are less than the scaled pole value
                nl.remove(move)
        ol = orderedList
        for item in ol: #removing items that are not in nl, from original fed in list
            if item not in nl:
                ol.remove(item)
        return ol

    def actOnMST(self, mst, actor):
        # rationality: a more rational actor will consider moves that have a higher probability of ending up in the desired state
        moves = mst.getMoves(actor.currentState) # get all moves avaliable from current state
        for move in moves:
            if move.probability < (self.value + actor.error): # remove the moves that have a probability of ending up in the desired state lower than the actor's rationality + an error term
                #im assuming that the probability of ending up in the desired state is the value of tbe move  and the value of the pole is the actors rationality
                mst.removeMove(move)
        return mst

class RiskPole(Pole):
    def __init__(self, value, weight):
        super(RiskPole, self).__init__(value, weight)
    def actOnList(self, orderedList, actor):
        # risk: allow moves for which there aren't enough resources
            # this increases the error term for the resource cut
            # done proportional to the pole. If the pole is 100%, the error term will go to infinity and no moves will be filtered by the resource cut
        ol = orderedList
        actor.resourerror = ((pow(-10, self.value)/(self.value-1)) - 0.05) #pole cannot have bigger value then one, or else this function will not work
        return ol

    def actOnMST(self, mst, actor):
        # risk: a more risky actor will consider moves that have a higher risk associated with them
        # work with mst
        moves = mst.getMoves(actor.currentState) # get all moves available from current state
        for move in moves:
            if move.risk < self.value + actor.error:  # remove all moves that have a higher risk than the value of the pole + an error term with mst.removeMove(move)
                mst.removeMove(move)
        return mst

class ParticularHolisticPole(Pole):
    # stubbornness will be stubborn, want to do specifically what the previous poles chose, and disregard what poles later say
    def __init__(self, value, weight):
        super(ParticularHolisticPole, self).__init__(value, weight)
    def actOnList(self, orderedList, actor):
        # holistic vs particular: holistic actor considers moves further from centroid.
        # work with list of orderedMoves from k-means
        ol = orderedList
        # obtain greatest possible distance from centroid
        maxdistance = abs(np.linalg.norm(ol[-1]-actor.ioValues))#k-means should be written before, to then be able to find the distance
        # scale the value of the particular/holistic pole by that amount.
        tempval = maxdistance*self.value
        # remove all moves that are a distance greater than the scaled pole value + an error term from the orderedMoves list
        for move in ol:
            if move.getIOValue().value > (tempval + actor.error):
                ol.remove(move)
        return ol

 #talk to nikita about this
    def actOnMST(self, mst, actor):
        # stubbornness will be stubborn, want to do specifically what the previous poles chose, and disregard what poles later say, what are we saying here?
        # 100% stubborn actor will not proceed to any pole later on. less stubborn actors will let more poles act.
        # need to create a scale that divides how many poles we want to act after this pole is called...
            # by intervals of .3 -- depending on how many more poles should act?
        moves = mst.getMoves(actor.currentState)  # get all moves available from current state
        tempval = self.value

        return mst



class PrimacyRecencyPole(Pole):
    def __init__(self, value, weight):
        super(PrimacyRecencyPole, self).__init__(value, weight)

    def actOnMST(self, mst, actor):
        # primacy (#using history as a guideline) vs recency (being more creative : go through actor's history/memory (in a way that is reflective of the value of the pole, ie if the actor likes history more, then more events in history will be considered and vice versa)
        #need to create another scale that according to the values will tell us how man y
        # need to be careful to remove an amount of moves that is reasonable
        # if a state in history is similar enough (within error bound) to the actor's current state:
            # if the move taken then is not similar enough (outside error bound) to a move in the MST, then remove it from MST.
            # similarity is defiend as absolute value of difference between resource deployment of two moves, similar to the similarity of states.
            # Compare using event.compareTo
            # need to be careful about removing too many moves. Juan check it so it doesn't remove everything


        return mst

    def actOnList(self, orderedList, actor):
        # primacy vs recency: an actor that has a higher primacy rating will look through history. if recency is more important, then the actor will look at his memory.
        ol = orderedList # work with the orderedMoves list.
        # get history and memory from the actor.
        history = actor.history
        memory = actor.memory
        # figure out how many more times primacy is more important than recency:
        val = int(round(abs((1 - self.value)/self.value)))
        # go through both lists at once, proportional to val:
        for event in history:
            # each time an event from history is examined, val events will be examined from memory.
            splice = memory[:val] #maybe val-1?
            for item in splice:
                # check whether the events are similar to the situation that the actor is in now with actor.curState. use Event.compare(event1, event2)
                similarity = Event.compare(event, item) #0 means the same, infinity means not similar at all
                if(similarity < 5): #5 is an arbitrary number -- recognize that we need to come up with the threshold to then be able to pinpoint what we want
                    # if the situation is similar beyond some threshold, then the move that associated with that move will be added to the mst.
                    mst.add(move) #I know this isn't a command, but mst is not made until we make the mst -- so should we store this move? 

        return input


class RoutineCreativePole(Pole):
    def __init__(self, value, weight):
        super(RoutineCreativePole, self).__init__(value, weight)

    def actOnMST(self, mst, actor):
        # routine vs creative: creative actor considers more random moves.
        moves = mst.getMoves(actor.currentState)  # get all moves available from current state
        for move in moves:  # for every move going from the current state:
            rnum = uniform(0,.999999999999) # do you think numpy is better at this? -- obtain a random number within bounds [0, 1). if it is more than the value of the routine/creative pole + an error Term:
            if rnum > (self.value + actor.error):
                mst.removeMove(move) # path will be removed. via mst.removeMove
        return mst

    def actOnList(self, orderedList, actor):
        # routine vs creative: routine actor will consider moves that have been successful in the past, while creative actors will be willing to try new moves
            # Add successful moves from the past to the list (Not all successful moves, only maxTimeTicks amount of moves in the past). Most successful moves will be added first.
            # success of a move is defined in actor.howSuccessfulWasMove
            # go through the list, removing moves that are not similar enough to the successful moves
                # how similar is enough depends on the value of the pole: 100% creative actor will have no moves removed. -1 is routine, 1 is creative
        ol = orderedList
        val = actor.howSuccessfulWasMove()
        for move in ol:

        return ol


class EmotionalPole(Pole):
    def __init__(self, value, weight):
        super(EmotionalPole, self).__init__(value, weight)

    # positive love negative fear 0 bland
    # extreme values are error terms
    def actOnList(self, orderedList, actor):
        # see below for description of pole function.
            # add moves that go a long with the value of the pole, similar to the way they are removed below.
            # if pole is extreme, then set error term

        return []

    def actOnMST(self, mst, actor):
        #a nything beyond -0.8 or 0.8 (extreme) we treat as increased error and in this case, tendency to choose violence.
        # From 0 to 0.7 you have increased tendency to build
        # From 0 to -0.7 you have a tendency to destroy. This is manifested through increasingly hostile kinetic moves.
        # go through MST. check category of move through move.category
        # moveCategories = a dictionary mapping from category to a range of values of this pole.
            # remove moves whose category does not map to a range of values that contains the value of the pole (+/- an arror term)
        return mst
