from MST import MST


class Actor:
    def __init__(self, poles, curState, desiredState, maxTime, error, history, criticalState):
        self.poles = poles
        self.curState = curState
        self.desiredState = desiredState
        self.maxTime = maxTime
        self.error = error
        self.history = history
        self.memory = []
        self.criticalState = criticalState

    '''
    orders possible moves based on ideal move (k-means)
    record how far away each move is from the ideal move
    Some moves may be cut off here based on the particular/holistic and routine/creative poles.
    Other may moves will be added based on the primacy/recency pole.
    The order these poles will act will depend on their weights.
    returns list of possible moves, ordered.
    '''

    # make actor history and memory for IO - populate "history", memory is populated during
    def orientation(self):
        # alter all of the poles (possibly), remember to put back
        # add honor pole
        # TODO order the moves based on ideal move using k-means, keeping track of how far each move is from the centroid

        orderedMoves = []
        # TODO sort the poles in here
        poles = self.poles
        # ordered by distance from centroid.
        for pole in poles:
            orderedMoves = pole.actOnList(orderedMoves, self)
        return orderedMoves

    '''
    cuts down possible moves by amount of resources that the actor
    currently has, within some error bound, because actors may chose
    to make moves even if they don't have enough resources
    returns list of moves filtered by resources
    '''

    def cutByResources(self, moves):
        remove = set()
        for move in moves:
            tempState = self.applyPossibleMove(move)
            for resource in tempState.pmesiiVars:
                if resource < -self.errorBound:
                    remove.add(move)
        moves = [i for i in moves if i not in remove]
        return moves

    '''
    chooses the move to be made by this actor
    appends the move to history and to memory of the actor.
    returns the Move that is chosen by this actor
    '''

    def makeDecision(self):
        # TODO
        #check if resources are critically low in the current state
        for i in range(0, len(self.curState)):
            if self.curState[i] < self.criticalState[i]:
                self.trigger(self.criticalState[i].name, self.criticalState[i].value)

        orderedMoves = self.orientation()
        cutResources = self.cutByResources(orderedMoves)
        mst = MST(self.curState, self.desiredState, cutResources, self.maxTime)
        mst = self.pH(mst)
        # check how many moves left in mst.
        moves = mst.getMoves()
            # if no moves left, actor will chose to not make any move at all.
            # if one left, then that is the move to be made
            # else chose move at random. (actor's PH decided that these moves are equivalent, so either is acceptable).

        event = Event(self.curState, result)
        self.addToMemory(result)
        return result

    '''
    checks to see what would be left of this actor's resources if this move were applied.
    returns the state of the actor's resources after applying the given move
    '''

    def applyPossibleMove(self, move):
        # TODO
        state = self.curState
        for i in range(0, len(move.pmesiiVars)):
            state.pmesiiVars[i] += move.pmesiiVars[i]
        return state


    '''
    add a move to this actor's memory
    '''

    def addToMemory(self, move):
        # TODO: this has to be different, memory is not the same as history. Figure out how to tell something is more important to an actor than something elses
        event = Event(self.curState, move)
        self.memory.append(event)

    '''
    The rest of the poles will act here. These are Primacy/Recency, Emotion, Urgency, Risk, Rationality. The order in which these will act depends on the weights of the poles.

    '''

    def pH(self, mst):
        poles = self.poles

        #TODO: sort poles based on weight
        for pole in poles:
            mst = pole.actOnMST(mst, self)
        return mst

    def setError(self, error):
        self.errorBound = error

    def getHistory(self):
        return self.history

    def getMemory(self):
        return self.memory
    '''
    trigger a move based on critically low values. temporarily set the desired state to one that will fix the currently lacking resource. Maybe we can make a stack of states that an actor needs to achieve
    '''
    #TODO: remember to reset it after! Python question
    def trigger(self, name, value):
        self.desiredState.set(name, value)
        # do something else

'''
This class represents an event in an actor's history/memory. It records the state that the actor was in, and the move that was made from that state
'''
class Event:
    def __init__(self, state, move):
        self.state = state
        self.move = move

    '''
    Compute how different two events are based on the state. Equal states will have 0 difference, so compare will return 0.
    '''
    @staticmethod
    def compare(event1, event2):
        difference = 0
        for i in range(0, len(event1.state.pmesiiVars)):
            difference += abs(event1.state.pmesiiVars[i] - event2.state.pmesiiVars[i])

        return difference
