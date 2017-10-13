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

import unittest

from Actor import Actor
from Move import Move
from Pole import *
from State import State


class TestStringMethods(unittest.TestCase):

    def test_rationalityPole(self):
        move1 = Move({"test1": 5, "test2": 10, "test3": 20}, None, [], .5, None)
        move2 = Move({"test1": 100, "test2": 200, "test3": 300}, None, [], .5, None)
        move3 = Move({"test1": 1, "test2": 1, "test3": 1}, None, [], .5, None)
        move4 = Move({"test1": -10, "test2": 10, "test3": -100}, None, [], .5, None)
        move5 = Move({"test1": 500, "test2": 1000, "test3": 10000}, None, [], .5, None)
        move0 = Move({"test1": 0, "test2": 0, "test3": 0}, None, [], 0, None)
        moves = [move1, move2, move3, move4, move5, move0]
        test_polelow = RationalityPole(-1,1)
        test_polemiddle= RationalityPole(-.5, 1)
        test_polehigh = RationalityPole(1, 1)
        actorlow = Actor([test_polelow], None, None, None, 0.05, None, None, [], None)
        actormiddle = Actor([test_polemiddle], None, None, None, 0.05, None, None, [], None)
        actorhigh = Actor([test_polehigh], None, None, None, 0.05, None, None, [], None)

        moveslow = test_polelow.actOnList(moves, actorlow)
        movesmiddle = test_polemiddle.actOnList(moves, actormiddle)
        moveshigh = test_polehigh.actOnList(moves, actorhigh)
        self.assertEqual(len(moveshigh), 6)
        self.assertEqual(len(moveslow), 0)
        self.assertTrue(len(movesmiddle) <4)

    def test_riskPole(self):
        move1 = Move({"test1": 5, "test2": 10, "test3": 20}, None, [], .5, None)
        move2 = Move({"test1": 100, "test2": 200, "test3": 300}, None, [], .5, None)
        move3 = Move({"test1": 1, "test2": 1, "test3": 1}, None, [], .5, None)
        move4 = Move({"test1": -10, "test2": 10, "test3": -100}, None, [], .5, None)
        move5 = Move({"test1": 500, "test2": 1000, "test3": 10000}, None, [], .5, None)
        move0 = Move({"test1": 0, "test2": 0, "test3": 0}, None, [], 0, None)
        moves = [move1, move2, move3, move4, move5, move0]
        test_polelow = RiskPole(-1, 1)
        test_polemiddle = RiskPole(0, 1)
        test_polehigh = RiskPole(.99, 1)
        actorlow = Actor([test_polelow], None, None, None, 0.05, None, None, [], None)
        actormiddle = Actor([test_polemiddle], None, None, None, 0.05, None, None, [], None)
        actorhigh = Actor([test_polehigh], None, None, None, 0.05, None, None, [], None)
        moveslow = test_polelow.actOnList(moves, actorlow)
        movesmiddle = test_polemiddle.actOnList(moves, actormiddle)
        moveshigh = test_polehigh.actOnList(moves, actorhigh)

        self.assertTrue(actorlow.error <1 )
        print("low error", actorlow.resourcesError)
        #print("high error", actorhigh.error)
        print("high error" + str(actorhigh.resourcesError))
        print("middle error",actormiddle.resourcesError)
        #print(actormiddle.error)
        print("done")

    def test_ParticularHolisticPole(self):

        move1 = Move({"test1": 5, "test2": 10, "test3": 20}, None, [0,0,0,0], .5, None)
        move2 = Move({"test1": 100, "test2": 200, "test3": 300}, None, [15,20,14,19], .5, None)
        move3 = Move({"test1": 1, "test2": 1, "test3": 1}, None, [200,-350,900,3], .5, None)
        move4 = Move({"test1": -10, "test2": 10, "test3": -100}, None, [39,189,289,398], .5, None)
        move5 = Move({"test1": 500, "test2": 1000, "test3": 10000}, None, [10,20,30,40], .5, None)
        move0 = Move({"test1": 0, "test2": 0, "test3": 0}, None, [1000,1000,1000,1000], 0, None)
        moves = [move1, move2, move3, move4, move5, move0]
        test_polelow = ParticularHolisticPole(-1, 1)
        test_polemiddle = ParticularHolisticPole(0, 1)
        test_polehigh = ParticularHolisticPole(1, 1)
        actorlow = Actor([test_polelow], None, None, None, 0.05, None, None, [], [0,0,0,0])
        actormiddle = Actor([test_polemiddle], None, None, None, 0.05, None, None, [], [0,0,0,0])
        actorhigh = Actor([test_polehigh], None, None, None, 0.05, None, None, [], [0,0,0,0])
        moveslow = test_polelow.actOnList(moves, actorlow)
        movesmiddle = test_polemiddle.actOnList(moves, actormiddle)
        moveshigh = test_polehigh.actOnList(moves, actorhigh)

        self.assertTrue(len(moveslow) !=6)
        self.assertTrue(len(moveshigh)>=5)


    def test_PrimacyRecencyPole(self):
        test_polelow = PrimacyRecencyPole(-1, 1)
        test_polemiddle = PrimacyRecencyPole(0, 1)
        test_polehigh = PrimacyRecencyPole(1, 1)
        #high primacy
        actorlow = Actor([test_polelow], State({"test1":1, "test2": 0, "test3": 0, "test4": 0}, None), None, None,.05, None,None, [], [])
        actormiddle = Actor([test_polemiddle], State({"test1":1, "test2": 0, "test3": 0, "test4": 0},None), None, None,.05, None,None, [], [])
        #high recency
        actorhigh = Actor([test_polehigh], State({"test1":1, "test2": 0, "test3": 0, "test4": 0}, None), None, None,.05, None,None, [], [])

        event1 = Event(None, None,Move({"test1":1, "test2": 1, "test3": 1, "test4": 1}, None, [], .5, None),0 )
        event2 = Event(None, None, Move({"test1":1, "test2": 1, "test3": 1, "test4": 2}, None, [], .5, None),0)
        event3 = Event(None, None, Move({"test1":.96, "test2": 0, "test3": 0, "test4": 0}, None, [], .5, None),0)
        event4 = Event(None, None, Move({"test1":0, "test2": 0, "test3": 0, "test4": 0}, None, [], .5, None),0)
        event5 = Event(None, None, Move({"test1":1, "test2": 1, "test3": 1, "test4": 2}, None, [], .5, None),0)
        event6 = Event(None, None, Move({"test1":101, "test2": 100, "test3": 100, "test4": 100}, None, [], .5, None),0)
        event7 = Event(None, None, Move({"test1":501, "test2": 500, "test3": 500, "test4": 500}, None, [], .5, None),0)
        event8 = Event(None, None, Move({"test1":1, "test2": 1, "test3": 0, "test4": 0}, None, [], .5, None),0)
        moves = []
        history = [event1, event2, event3, event4]
        memory = [event5, event6, event7, event8]
        actorlow.history = history
        actorhigh.history = history
        actormiddle.history = history
        actorlow.memory=memory
        actormiddle.memory = memory
        actorhigh.memory = memory

        print("MOVES LOW")
        moveslow = test_polelow.actOnList(moves, actorlow)
        print("MOVES MID:")
        movesmiddle = test_polemiddle.actOnList(moves, actormiddle)
        print("MOVES HIGH:")
        moveshigh = test_polehigh.actOnList(moves, actorhigh)
        # print(moveslow == movesmiddle==moveshigh)
        # print(len(movesmiddle))
        # print(moveshigh[0].resources.items())


    def test_RoutineCreativePole(self):
        test_polelow = RoutineCreativePole(-.75, 1)
        test_polemiddle = RoutineCreativePole(0, 1)
        test_polehigh = RoutineCreativePole(1, 1)
        # high primacy
        actorlow = Actor([test_polelow], State({"test1":1, "test2": 1, "test3": 1, "test4": 1}, None),None, None, .1,
                         None, None, [], [])
        actormiddle = Actor([test_polemiddle], State({"test1":1, "test2": 1, "test3": 1, "test4": 1}, None),
                            None, None, .1, None, None, [], [])
        # high recency
        actorhigh = Actor([test_polehigh], State({"test1":1, "test2": 1, "test3": 1, "test4": 1}, None), None,None, .1, None, None, [], [])

        event1 = Event(None, None,Move({"test1":1, "test2": 1, "test3": 1, "test4": 1}, None, [], .5, None),0 )
        event2 = Event(None, None, Move({"test1":0, "test2": 0, "test3": 0, "test4": 0}, None, [], .5, None),0)
        # event3 = Event(None, None, Move({"test1":100, "test2": 100, "test3": 200, "test4": 300}, None, [], .5, None),0)
        # event4 = Event(None, None, Move({"test1":0, "test2": 0, "test3": 0, "test4": 1}, None, [], .5, None),0)
        # event5 = Event(None, None, Move({"test1":1, "test2": 1, "test3": 1, "test4": 2}, None, [], .5, None),0)
        # event6 = Event(None, None, Move({"test1":101, "test2": 100, "test3": 100, "test4": 100}, None, [], .5, None),0)
        # event7 = Event(None, None, Move({"test1":501, "test2": 500, "test3": 500, "test4": 500}, None, [], .5, None),0)
        # event8 = Event(None, None, Move({"test1":1, "test2": 1, "test3": 0, "test4": 0}, None, [], .5, None),0)


        moves = [Move({"test1":1, "test2": 1, "test3": 1, "test4": 1}, None, [], .5, None),
                     Move( {"test1": 0, "test2": 0, "test3": 0, "test4": 0}, None, [], .5, None),
                    Move({"test1": 1000, "test2": 1000, "test3": 1000, "test4": 1000}, None, [], .5, None),
                 Move({"test1": .75, "test2": .75, "test3": .75, "test4": .75}, None, [], .5, None),
                 Move({"test1": .89, "test2":.99, "test3": .99, "test4": 1}, None, [], .5, None)]
        successfulMoves = [event1, event2] #,event3, event4, event5, event6, event7, event8]
        actorlow.timeTicks = 8
        actormiddle.timeTicks = 8
        actorhigh.timeTicks = 8
        actorlow.successfulMoves = successfulMoves
        actorhigh.successfulMoves = successfulMoves
        actormiddle.successfulMoves = successfulMoves
        moveslow = test_polelow.actOnList(moves, actorlow )
        movesmiddle = test_polemiddle.actOnList(moves, actormiddle)
        moveshigh = test_polehigh.actOnList(moves, actorhigh)
        print("PRINTING MOVES LOW MIDDLE HIGH")
        print(len(moveslow))
        print(len(movesmiddle))
        print(len(moveshigh))
    def test_EmotionalPole(self):
        #need to make categories and see if they add moves
        #pretty much only need to make actors, poles, and moves w only categories
        test_polelow = EmotionalPole(-.21, 1)
        test_polemiddle = EmotionalPole(0, 1)
        test_polehigh = EmotionalPole(.6, 1)
        actorlow = Actor([test_polelow], None, None, None, 0.05, None, None, [], [])
        actormiddle = Actor([test_polemiddle], None, None, None, 0.05, None, None, [], [])
        actorhigh = Actor([test_polehigh], None, None, None, 0.05, None, None, [], [])

        move1= Event(None, None, Move({"t1":0}, None, [], .5,'Engage in diplomatic cooperation'), 0)

        move2 =Event(None, None, Move({"t1":0}, None, [], .5, 'Engage in in material cooperation'), 0)
        move3 = Event(None, None, Move({"t1":0}, None, [], .5, 'Appeal'), 0)
        move4 = Event(None,None, Move({"t1":0}, None, [], .5, 'Build economic infrastructure'),0)
        move5 = Event(None,None, Move({"t1":0}, None, [], .5, 'Build energy infrastructure'),0)
        move6 = Event(None, None, Move({"t1":0},  None,[], .5, 'Build military infrastructure'), 0)
        moveneg = Event(None, None,Move({"t1":0}, None, [], .5,'Assault') ,0)
        moveneg2 = Event(None,None, Move({"t1":0}, None, [], .5, 'Coerce'), 0)
        history = [move1, move2,move3,move4,move5,move6, moveneg, moveneg2]
        actorlow.history = history
        actormiddle.history= history
        actorhigh.history = history
        moves = []
        moveslow = test_polelow.actOnList(moves,actorlow)
        movesmiddle = test_polemiddle.actOnList(moves, actormiddle)
        moveshigh = test_polehigh.actOnList(moves, actorhigh)
        print("emotionalpole move length")
        print(len(moveslow))
        print(len(movesmiddle))
        print(len(moveshigh))

    def test_GenerosityPole(self):
        test_polelow = GenerosityPole(-1, 1)
        test_polemiddle = GenerosityPole(0, 1)
        test_polehigh = GenerosityPole(1, 1)
        actorlow = Actor([test_polelow], None, None, None, .05,None, None, [], [])
        actormiddle = Actor([test_polemiddle], None,None, None, .05, None, None, [], [])

        actorhigh = Actor([test_polehigh], None, None, None, .05, None, None, [], [])

        move1 = Move({"test1": 100, "test2": 100, "test3": 100}, None, [], .5, None)
        move2 = Move({"test1": 200, "test2": 200, "test3": 200}, None, [], .5, None)
        move3 = Move({"test1": 0, "test2": 0, "test3": 0}, None, [], .5, None)
        move4 = Move({"test1": 1000, "test2": 1000, "test3": 1000}, None, [], .5, None)
        move5 = Move({"test1": 500, "test2": 1000, "test3": 1000}, None, [], .5, None)
        moves = [move1,move2,move3,move4,move5]
        moveslow = test_polelow.actOnList(moves,actorlow)
        movesmiddle = test_polemiddle.actOnList(moves, actormiddle)
        moveshigh = test_polehigh.actOnList(moves, actorhigh)
        self.assertTrue(move3 in moveslow)
        self.assertTrue(len(moveslow)==1)
        self.assertTrue(len(moveshigh)==5)
        self.assertTrue((move4 not in movesmiddle))






if __name__ == '__main__':



    unittest.main()

