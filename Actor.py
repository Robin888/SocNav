from MST import MST


class Actor:
    def __init__(self, poles, currentState, desiredState, maxTime, error, resourerror, history, criticalState):
        self.poles = sorted(poles, key=lambda pole: pole.weight)
        self.currentState = currentState
        self.desiredState = desiredState
        self.maxTime = maxTime
        self.error = error
        self.resourerror = resourerror
        self.history = history
        self.memory = []
        self.criticalState = criticalState
        self.successfulMoves = []

    '''
    orders possible moves based on ideal move (k-means)
    record how far away each move is from the ideal move
    The poles will act here for the first time.
    The order these poles will act will depend on their weights.
    To see specific actions of poles see the actOnList method of the poles.
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
                if resource < -self.errorBound: #should be switched to resourerror
                    remove.add(move)
        moves = [i for i in moves if i not in remove]
        return moves

    '''
    check if the previous move was successful.
    successful means that the move made the state of the actor closer to the desired state.
    the more negative the value returned is, the more successful a move was. 0 means move didn't change the state.
    Positive means the move moved the current state further from the desired state.
    negative means the move moved the current state closer to the desired state than before
    '''
    def howSuccessfulWasMove(self):
        return self.currentState - self.memory[0].desiredState > self.memory[0].currentState - self.memory[0].desiredState

    '''
    chooses the move to be made by thisactor
    appends the move and to memory of the actor.
    returns the Move that is chosen by this actor
    '''

    def makeDecision(self):
        if self.howSuccessfulWasMove() < 0:
            self.memory[0].success = self.howSuccessfulWasMove()
            self.successfulMoves.append(self.memory[0].move)
        # TODO
        #check if resources are critically low in the current state
        for i in range(0, len(self.currentState)):
            if self.currentState[i] < self.criticalState[i]:
                self.trigger(self.criticalState[i].name, self.criticalState[i].value)

        orderedMoves = self.orientation()
        cutResources = self.cutByResources(orderedMoves)
        mst = MST(self.currentState, self.desiredState, cutResources, self.maxTime)
        mst = self.pH(mst)
        # check how many moves left in mst.
        moves = mst.getMoves()
            # if no moves left, actor will chose to not make any move at all.
            # if one left, then that is the move to be made
            # else chose move at random. (actor's PH decided that these moves are equivalent, so either is acceptable).

        event = Event(self.currentState,self.desiredState, result)
        self.addToMemory(result)
        return result

    '''
    checks to see what would be left of this actor's resources if this move were applied.
    returns the state of the actor's resources after applying the given move
    '''

    def applyPossibleMove(self, move):
        # TODO
        state = self.currentState
        for i in range(0, len(move.pmesiiVars)):
            state.pmesiiVars[i] += move.pmesiiVars[i]
        return state


    '''
    add a move to this actor's memory
    '''

    def addToMemory(self, move):
        self.memory.append(Event(self.currentState, move)) #shouldn't we also include the desiredState?

    '''
   The poles will act again here, on the MST. The order in which these will act depends on the weights of the poles.

    '''

    def pH(self, mst):
        poles = self.poles
        #sort poles based on weight
        for pole in poles:
            #add clause here for the stoppage of looking at other poles -- this due to particularholisticpole method
            mst = pole.actOnMST(mst, self)

        return mst

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
    def __init__(self, currentState, desiredState, move):
        self.currentState = currentState
        self.desiredState = desiredState
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
