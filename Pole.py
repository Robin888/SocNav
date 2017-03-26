import abc
from MST import MST

'''
This is the superclasss for all poles. Classes inheriting from this class must define a method act.
'''
class Pole(metaclass=abc.ABCMeta):
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
            # make copy of list
            # order moves based on cost (absolute value of resources deployed), with "cheapest" moves first
            # scale the value of the pole by the length of the list, keep the virst (*value* + errorTerm) amount of moves in the list
        return []

    def actOnMST(self, mst, actor):
        # rationality: a more rational actor will consider moves that have a higher probability of ending up in the desired state
        # ie if there is no move that guarantees the final state with 100% probability, an actor with 100% rationality will chose not to make any move.
        # work with mst
            # get all moves avaliable from current state
            # remove the moves that have a probability of ending up in the desired state lower than the actor's rationality + an error term
            # mst.removeMove(move)
        return mst
#TODO Trigger moves - consider changing the desired state temporarily
#what happens when resources go negative

class RiskPole(Pole):
    def __init__(self, value, weight):
        super(RiskPole, self).__init__(value, weight)
    def actOnList(self, orderedList, actor):
        # risk: allow moves for which there aren't enough resources
            # this increases the error term for the resource cut
            # done proportional to the pole. If the pole is 100%, the error term will go to infinity and no moves will be filtered by the resource cut
        return []

    def actOnMST(self, mst, actor):
        # risk: a more risky actor will consider moves that have a higher risk associated with them
        # work with mst
            # get all moves available from current state
            # remove all moves that have a higher risk than the value of the pole + an error term with mst.removeMove(move)
        return mst

class ParticularHolisticPole(Pole):
    # TODO can't see the whole space
    # stubbornness will be stubborn, want to do specifically what the previous poles chose, and disregard what poles later say
    def __init__(self, value, weight):
        super(ParticularHolisticPole, self).__init__(value, weight)

    def actOnMST(self, mst, actor):
        # urgency pole: more urgent actors will consider less moves
            # cut off paths at random from the MST
        return mst

    def actOnList(self, orderedList, actor):
        # holistic vs particular: holistic actor considers moves further from centroid.
        # work with list of orderedMoves from k-means
            # obtain greatest possible distance from centroid
            # scale the value of the particular/holistic pole by that amount.
            # remove all moves that are a distance greater than the scaled pole value + an error term from the orderedMoves list
        return []


class PrimacyRecencyPole(Pole):
    def __init__(self, value, weight):
        super(PrimacyRecencyPole, self).__init__(value, weight)

    def actOnMST(self, mst, actor):
        return mst

    def actOnList(self, orderedList, actor):
        # primacy vs recency: an actor that has a higher primacy rating will look through history. if recency is more important, then the actor will look at his memory.
        # work with the orderedMoves list.
        # get history and memory from the actor.
        # figure out how many more times primacy is more important than recency:
            # val = (1 - self.value)/self.value
        # go through both lists at once, proportional to val:
            # each time an event from history is examined, val events will be examined from memory.
            # check whether the events are similar to the situation that the actor is in now with actor.curState. use Event.compare(event1, event2)
            # if the situation is similar beyond some threshold, then the move that associated with that move will be added to the mst.
        return input


class RoutineCreativePole(Pole):
    def __init__(self, value, weight):
        super(RoutineCreativePole, self).__init__(value, weight)

    def actOnMST(self, mst, actor):
        # routine vs creative: creative actor considers more random moves.
        # work with mst:
            # for every move going from the current state:
                # obtain a random number within bounds [0, 1). if it is more than the value of the routine/creative pole + an error Term:
                    # path will be removed. via mst.removeMove
        return mst

    def actOnList(self, orderedList, actor):
        # routine vs creative: creative actor considers more random moves. 100% creative actor will have no moves pruned.
        # work with original orderedMoves list from k-means
            # for every move in the list:
                # obtain a random number within bounds [0, 1). if it is more than the value of the routine/creative pole + an error Term:
                    # move will be removed
                    # moves that are a further distance from the centroid will have a higher probability of being randomly removed by the routine/creative pole
                        # 1/(len - index) probability.
        return []

# positive love negative fear 0 bland
# extreme values are error terms
class EmotionalPole(Pole):
    def __init__(self, value, weight):
        super(EmotionalPole, self).__init__(value, weight)

    def actOnList(self, orderedList, actor):
        # work only on actor, same function as actOnMST.
            # this increases the pole Error
            # make some moves closer to the centroid than they should be.
            #TODO don't forget to restore original value in actor after first cut has finished
        return []

    def actOnMST(self, mst, actor):
        # emotional: an emotional actor will make more unprecedented moves. an unemotional actor will have a low actor-related error term.
        # work only on actor
            # increase error term of actor proportionally to the value of the pole with actor.setError(newError)
            # this increases the pole Error
        return mst
