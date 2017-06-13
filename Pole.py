import abc
from MST import MST

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
            # make copy of list
            # order moves based on cost (absolute value of resources deployed), with "cheapest" moves first
            # scale the value of the pole by the length of the list, keep the first (*value* + errorTerm) amount of moves in the list
        return []

    def actOnMST(self, mst, actor):
        # rationality: a more rational actor will consider moves that have a higher probability of ending up in the desired state
        # ie if there is no move that guarantees the final state with 100% probability, an actor with 100% rationality will chose not to make any move.
        # work with mst
            # get all moves avaliable from current state
            # remove the moves that have a probability of ending up in the desired state lower than the actor's rationality + an error term
            # mst.removeMove(move)
        return mst

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
    # stubbornness will be stubborn, want to do specifically what the previous poles chose, and disregard what poles later say
    def __init__(self, value, weight):
        super(ParticularHolisticPole, self).__init__(value, weight)

    def actOnMST(self, mst, actor):
        # stubbornness will be stubborn, want to do specifically what the previous poles chose, and disregard what poles later say
        # 100% stubborn actor will not proceed to any pole later on. less stubborn actors will let more poles act.
        # Juan - think about how to do this. Requires some modification in actor class as well.
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
        # primacy vs recency: go through actor's history/memory (in a way that is reflective of the value of the pole, ie if the actor likes history more, then history will more events in history will be considered and vice versa)
        # need to be careful to remove an amount of moves that is reasonable
        # if a state in history is similar enough (within error bound) to the actor's current state:
            # if the move taken then is not similar enough (outside error bound) to a move in the MST, then remove it from MST.
            # similarity is defiend as absolute value of difference between resource deployment of two moves, similar to the similarity of states.
            # Compare using event.compareTo
            # need to be careful about removing too many moves. Juan check it so it doesn't remove everything
        return mst

    def actOnList(self, orderedList, actor):
        # JUAN - when you get to this one hit me up I'll send you a sample solution I wrote for it. You can start from there and then improve if needed.
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
        # routine vs creative: routine actor will consider moves that have been successful in the past, while creative actors will be willing to try new moves
            # Add successful moves from the past to the list (Not all successful moves, only maxTimeTicks amount of moves in the past). Most successful moves will be added first.
            # success of a move is defined in actor.howSuccessfulWasMove
            # go through the list, removing moves that are not similar enough to the successful moves
                # how similar is enough depends on the value of the pole: 100% creative actor will have no moves removed.
                # Compare move similarity with move.compareTo

        return []


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
        # moveCategories = a dictionary mapping from category to a range of values of this pole. <- will be given somehow. Depends on SMRs.
            # remove moves whose category does not map to a range of values that contains the value of the pole (+/- an arror term)
        return mst

class GenerosityPole(Pole):
    def __init__(self, value, weight):
        super(GenerosityPole, self).__init__(value, weight)
        self.maxListPrice = None

    def actOnList(self, orderedList, actor):
        # if self.maxListPrice = None: (if statement for caching)
            # go through list, find most expensive move by summing over all resources. self.maxListPrice = resulf of this calculation
        # scale value of pole to [0, 1] val = result of this calculation
        # val = val * self.maxListPrice
        # go through list, remove all moves that have cost (total resource delta) greater than val + error term
        return []
        
    def actOnMST(self, mst, actor):
        # similar function as above, maybe you can extract a method to avoid duplicate code.
        # go through each path on the mst (recursively) (two passes)
        # first time find most expensive move = val
        # scale pole to [0, 1] 
        # val = val * most expensive move
        # second time go through each path and remove the path if any move in it is more expensive than val + an error 
        return mst