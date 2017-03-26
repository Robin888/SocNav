import networkx as nx


class MST:
    def __init__(self, curState, desiredState, moves, maxTime):
        self.curState = curState
        self.desiredState = desiredState
        self.graph = nx.Graph()
        self.maxTime = maxTime
        self.possibleMoves = moves
        self.tree = self.generateTree(self.curState, 0)

    '''
    build the tree
    parentNode = the current state of the system, which will be the root node of the tree.
    curTime - the amount of time ticks for which to build the tree.
    '''

    def generateTree(self, parentNode, curTime):
        self.graph.add_node(parentNode)
        # need to define equivalence of states. actors may choose to settle for a state that is "close enough"
        if parentNode != self.desiredState:
            for move in self.possibleMoves:
                possibleState = move.getPossibleState(parentNode)
                possibleState.setTime(curTime)
                self.graph.add_node(possibleState)
                self.graph.add_edge(parentNode, possibleState, object=move)
        if curTime < self.maxTime:
            #change this to self.graph.neighbors(parentNode)
            adjacency = self.graph[parentNode]
            for k, v in adjacency.items():
                self.generateTree(k, curTime=curTime + 1)
        return parentNode

    def getTree(self):
        return self.tree

    '''
    remove the given move (starting from the curState) from the tree.
    '''
    def removeMove(self, move):
        # find move among edges from root of the tree
        # get the first node along that path.
        # remove the whole path with removePath(self.tree, childNode)
        pass

    '''
    remove a whole path, up until it merges with another existing one or until it reaches the desired state.
    '''

    def removePath(self, parentNode, childNode):

        adjacency = self.graph.neighbors(childNode)
        # need to define equivalence of states. actors may choose to settle for a state that is "close enough"
        if len(adjacency) == 2 and childNode != self.desiredState:
            for child in adjacency:
                if child != parentNode:
                    newChild = child
            self.removePath(childNode, newChild)

        self.graph.remove_edge(parentNode, childNode)
        self.graph.remove_node(childNode)

    '''
    Get all of the moves from the current state.
    '''
    def getMoves(self):
        # TODO return list of moves stemming from current state
        neighbors = self.graph.neighbors(self.curState)
        moves = [self.graph.get_edge_data(self.curState, neighbor)["object"] for neighbor in neighbors]
        return moves
