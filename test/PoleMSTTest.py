import unittest

from dm.Actor import Actor, Event
from dm.Move import Move
from dm.Pole import *
from dm.State import State
from dm.MST import MST


class TestPoleMST(unittest.TestCase):
    def test_rationalityPole(self):
        move1 = Move({"f1": 1}, {"i1": 1}, [], 0, None)
        move2 = Move({"f1": 2}, {"i1": 2}, [], .45, None)
        move3 = Move({"f1": 3}, {"i1": 3}, [], .95, None)

        curstate1 = State({'f1': 0}, {'i1': 0})
        desState1 = State({'f1': 100}, {'i1': 100})

        test_MST1 = MST(curstate1, desState1, [move1, move2, move3], 2)
        test_MST2 = MST(curstate1, desState1, [move1, move2, move3], 2)
        test_MST3 = MST(curstate1, desState1, [move1, move2, move3], 2)
        test_polelow = RationalityPole(-1, 1)
        test_polemiddle = RationalityPole(0, 1)
        test_polehigh = RationalityPole(1, 1)
        actorlow = Actor([test_polelow], None, None, None, 0.05, None, None, [], None)  # will remove no moves
        actormiddle = Actor([test_polemiddle], None, None, None, 0.05, None, None, [], None)  # will remove move1
        actorhigh = Actor([test_polehigh], None, None, None, 0.05, None, None, [], None)  # will remove move1, move2

        low_mst = test_polelow.actOnMST(test_MST1, actorlow)

        self.assertTrue(low_mst.containsMove(move1) and low_mst.containsMove(move2) and low_mst.containsMove(move3))

        mid_mst = test_polemiddle.actOnMST(test_MST2, actormiddle)
        print("middle test_MST")

        self.assertTrue(mid_mst.containsMove(move2))
        self.assertFalse(mid_mst.containsMove(move1))
        self.assertTrue(mid_mst.containsMove(move3))

        high_mst = test_polehigh.actOnMST(test_MST3, actorhigh)

        self.assertTrue(high_mst.containsMove(move3))
        self.assertFalse(high_mst.containsMove(move1))
        self.assertFalse(high_mst.containsMove(move2))

    def test_RiskPole(self):
        curstate1 = State({"f1": 100, "f2": 0}, {"i1": 0})
        desState1 = State({'f1': 1000}, {'i1': 1000})
        move1 = Move({"f1": 0, "f2": 0}, {"i1": 1}, [], 1, None)
        move2 = Move({"f1": 50, "f2": 0}, {"i1": 2}, [], 1, None)
        move3 = Move({"f1": 100, "f2": 0}, {"i1": 3}, [], 1, None)
        move4 = Move({"f1": 200, "f2": 0}, {"i1": 3}, [], 1, None)
        test_MST1 = MST(curstate1, desState1, [move1, move2, move3, move4], 2)
        test_MST2 = MST(curstate1, desState1, [move1, move2, move3, move4], 2)
        test_MST3 = MST(curstate1, desState1, [move1, move2, move3, move4], 2)
        test_polelow = RiskPole(-1, 1)
        test_polemiddle = RiskPole(0, 1)
        test_polehigh = RiskPole(1, 1)
        actorlow = Actor([test_polelow], curstate1, None, None, 0.05, None, None, [], None)  #
        actormiddle = Actor([test_polemiddle], curstate1, None, None, 0.05, None, None, [], None)  #
        actorhigh = Actor([test_polehigh], curstate1, None, None, 0.05, None, None, [], None)
        low_mst = test_polelow.actOnMST(test_MST1, actorlow)  # contain only move1

        mid_mst = test_polemiddle.actOnMST(test_MST2, actormiddle)  # containmove1 and 2

        high_mst = test_polehigh.actOnMST(test_MST3, actorhigh)  # contain 123
        self.assertTrue(low_mst.containsMove(move1))
        self.assertFalse(low_mst.containsMove(move2))
        self.assertFalse(low_mst.containsMove(move3))
        self.assertFalse(low_mst.containsMove(move4))
        self.assertTrue(mid_mst.containsMove(move1))
        self.assertTrue(mid_mst.containsMove(move2))
        self.assertFalse(mid_mst.containsMove(move3))
        self.assertFalse(mid_mst.containsMove(move4))
        self.assertTrue(high_mst.containsMove(move1))
        self.assertTrue(high_mst.containsMove(move2))
        self.assertTrue(high_mst.containsMove(move3))
        self.assertFalse(high_mst.containsMove(move4))

    def test_PrimacyRecencyPole(self):
        curstate1 = State({"f1": 100, "f2": 0}, {"i1": 0})
        desState1 = State({'f1': 1000}, {'i1': 1000})
        test_polelow = PrimacyRecencyPole(-1, .1)
        test_polemiddle = PrimacyRecencyPole(0, 1)
        test_polehigh = PrimacyRecencyPole(1, 1)
        move1 = Move({"f1": 101, "f2": 0}, {"i1": 1}, [], 1, None)
        move2 = Move({"f1": 102, "f2": 0}, {"i1": 1}, [], 1, None)
        move3 = Move({"f1": 110, "f2": 0}, {"i1": 1}, [], 1, None)
        move4 = Move({"f1": 106, "f2": 0}, {"i1": 1}, [], 1, None)
        move5 = Move({"f1": 101, "f2": 0}, {"i1": 0}, [], 1, None)
        move6 = Move({"f1": 102, "f2": 0}, {"i1": 0}, [], 1, None)
        move7 = Move({"f1": 110, "f2": 0}, {"i1": 0}, [], 1, None)
        move8 = Move({"f1": 106, "f2": 0}, {"i1": 0}, [], 1, None)
        move00 = Move({"f1": 0, "f2": 0}, {"i1": 0}, [], 1, None)
        event1 = Event(None, None, move1, 0)
        event2 = Event(None, None, move2, 0)
        event3 = Event(None, None, move3, 0)
        event4 = Event(None, None, move4, 0)
        event5 = Event(None, None, move5, 0)
        event6 = Event(None, None, move6, 0)
        event7 = Event(None, None, move7, 0)
        event8 = Event(None, None, move8, 0)

        actorlow = Actor([test_polelow], curstate1, None, None, .05, None, None, [], [])
        actormiddle = Actor([test_polemiddle], curstate1, None, None, .05, None, None, [], [])
        # high recency
        actorhigh = Actor([test_polehigh], curstate1, None, None, .05, None, None, [], [])
        actorlow.memory = [event1, event2, event3, event4]
        actorhigh.memory = [event1, event2, event3, event4]
        actormiddle.memory = [event1, event2, event3, event4]
        actorlow.history = [event5, event6, event7, event8]
        actormiddle.history = [event5, event6, event7, event8]
        actorhigh.history = [event5, event6, event7, event8]
        test_MST1 = MST(curstate1, desState1, [move1, move2, move3, move4, move5, move6, move7, move8, move00], 2)
        test_MST2 = MST(curstate1, desState1, [move1, move2, move3, move4, move5, move6, move7, move8, move00], 2)
        test_MST3 = MST(curstate1, desState1, [move1, move2, move3, move4, move5, move6, move7, move8, move00], 2)
        low_mst = test_polelow.actOnMST(test_MST1, actorlow)  # contain only move 1,2,5,6,7,8,00
        mid_mst = test_polemiddle.actOnMST(test_MST2, actormiddle)  # contain 1,2,5,6,00
        high_mst = test_polehigh.actOnMST(test_MST3, actorhigh)  # contain 1,2,3,,4 ,5,6,00

        self.assertTrue(low_mst.containsMove(move1))
        self.assertTrue(low_mst.containsMove(move2))
        self.assertTrue(low_mst.containsMove(move5))
        self.assertTrue(low_mst.containsMove(move6))
        self.assertTrue(low_mst.containsMove(move7))
        self.assertTrue(low_mst.containsMove(move00))
        self.assertFalse(low_mst.containsMove(move3))
        self.assertFalse(low_mst.containsMove(move4))
        self.assertTrue(low_mst.containsMove(move8))

        self.assertTrue(mid_mst.containsMove(move1))
        self.assertTrue(mid_mst.containsMove(move2))
        self.assertTrue(mid_mst.containsMove(move5))
        self.assertTrue(mid_mst.containsMove(move6))
        self.assertTrue(mid_mst.containsMove(move00))
        self.assertFalse(mid_mst.containsMove(move3))
        self.assertFalse(mid_mst.containsMove(move4))
        self.assertFalse(mid_mst.containsMove(move7))
        self.assertFalse(mid_mst.containsMove(move8))
        self.assertFalse(mid_mst.containsMove(move3))

        self.assertTrue(high_mst.containsMove(move2))
        self.assertTrue(high_mst.containsMove(move3))
        self.assertTrue(high_mst.containsMove(move4))
        self.assertTrue(high_mst.containsMove(move5))
        self.assertTrue(high_mst.containsMove(move6))
        self.assertTrue(high_mst.containsMove(move00))
        self.assertTrue(not high_mst.containsMove(move7))
        self.assertTrue(not high_mst.containsMove(move8))
        self.assertTrue(high_mst.containsMove(move1))

    # def test_RoutineCreativePole(self):
    #     curstate1 = State({"f1": 100, "f2": 0}, {"i1": 0})
    #     desState1 = State({'f1': 1000}, {'i1': 1000})
    #     test_polelow = RoutineCreativePole(-1, 1)
    #     test_polemiddle = RoutineCreativePole(0,1)
    #     test_polehigh = RoutineCreativePole(1,1)
    #     move1 = Move({"f1": 0, "f2": 0}, {"i1": 1}, [], 1, None)
    #     move2 = Move({"f1": 50, "f2": 0}, {"i1": 2}, [], 1, None)
    #     move3 = Move({"f1": 100, "f2": 0}, {"i1": 3}, [], 1, None)
    #     move4 = Move({"f1": 200, "f2": 0}, {"i1": 3}, [], 1, None)
    #     move5 = Move({"f1": 0, "f2": 0}, {"i1": 1}, [], 1, None)
    #     move6 = Move({"f1": 50, "f2": 0}, {"i1": 2}, [], 1, None)
    #     move7 = Move({"f1": 100, "f2": 0}, {"i1": 3}, [], 1, None)
    #     move8 = Move({"f1": 200, "f2": 0}, {"i1": 3}, [], 1, None)
    #     move9 = Move({"f1": 0, "f2": 0}, {"i1": 1}, [], 1, None)
    #     move0 = Move({"f1": 50, "f2": 0}, {"i1": 2}, [], 1, None)
    #     test_MST1 = MST(curstate1, desState1, [move1, move2, move3, move4, move5, move6, move7, move8, move9, move0], 2)
    #     test_MST2 = MST(curstate1, desState1, [move1, move2, move3, move4, move5, move6, move7, move8, move9, move0], 2)
    #     test_MST3 = MST(curstate1, desState1, [move1, move2, move3, move4, move5, move6, move7, move8, move9, move0], 2)
    #     actorlow = Actor([test_polelow], curstate1, None, None, .05, None, None, [], [])
    #     actormiddle = Actor([test_polemiddle], curstate1, None, None, .05, None, None, [], [])
    #     actorhigh = Actor([test_polehigh], curstate1, None, None, .05, None, None, [], [])
    #     low_mst = test_polelow.actOnMST(test_MST1, actorlow)
    #     mid_mst = test_polemiddle.actOnMST(test_MST2, actormiddle)
    #     high_mst = test_polehigh.actOnMST(test_MST3, actorhigh)
    #     print(len(low_mst.getMoves()))
    #     self.assertTrue(len(low_mst.getMoves())==0)
    #     print(low_mst.getMoves())
    #     self.assertTrue(len(mid_mst.getMoves())>3 and len(mid_mst.getMoves())<7)
    #     self.assertTrue(len(high_mst.getMoves())>8)

    def test_EmotionalPole(self):
        curstate1 = State({"f1": 100}, {"i1": 0})
        desState1 = State({'f1': 1000}, {'i1': 1000})
        test_polelow = EmotionalPole(-.81, 1)
        test_polemiddle = EmotionalPole(.5, 1)
        test_polehigh = EmotionalPole(1, 1)
        move1 = Move({"f1": 0}, {"i1": 0}, [], .5, 'Engage in diplomatic cooperation')  # .6-.8

        move2 = Move({"f1": 0}, {"i1": 0}, [], .5, 'Appeal')  # 4-6
        move3 = Move({"f1": 0}, {"i1": 0}, [], .5, 'Build economic infrastructure')  # .5-.7
        move4 = Move({"f1": 0}, {"i1": 0}, [], .5, 'Assault')  # -.2
        move5 = Move({"f1": 0}, {"i1": 0}, [], .5, 'Coerce')  # -.8
        test_MST1 = MST(curstate1, desState1, [move1, move2, move3, move4, move5], 2)
        test_MST2 = MST(curstate1, desState1, [move1, move2, move3, move4, move5], 2)
        test_MST3 = MST(curstate1, desState1, [move1, move2, move3, move4, move5], 2)
        actorlow = Actor([test_polelow], curstate1, None, None, .05, None, None, [], [])
        actormiddle = Actor([test_polemiddle], curstate1, None, None, .05, None, None, [], [])
        actorhigh = Actor([test_polehigh], curstate1, None, None, .05, None, None, [], [])
        low_mst = test_polelow.actOnMST(test_MST1, actorlow)
        mid_mst = test_polemiddle.actOnMST(test_MST2, actormiddle)
        high_mst = test_polehigh.actOnMST(test_MST3, actorhigh)
        self.assertTrue(low_mst.containsMove(move5))
        self.assertFalse(low_mst.containsMove(move1) and low_mst.containsMove(move2) and low_mst.containsMove(
            move3) and low_mst.containsMove(move4))
        self.assertFalse(mid_mst.containsMove(move1))
        self.assertFalse(mid_mst.containsMove(move4))
        self.assertFalse(mid_mst.containsMove(move5))
        self.assertTrue(mid_mst.containsMove(move2))
        self.assertFalse(mid_mst.containsMove(move3))
        # TODO do we want to change the legit error or just the bounds the move can be in

    def test_GenerosityPole(self):
        curstate1 = State({"f1": 100}, {"i1": 0})
        desState1 = State({'f1': 1000}, {'i1': 1000})
        test_polelow = GenerosityPole(-1, 1)
        test_polemiddle = GenerosityPole(0, 1)
        test_polehigh = GenerosityPole(1, 1)
        move1 = Move({"f1": 100, "f2": 0}, {"i1": 1}, [], 1, None)  # most expensive
        move2 = Move({"f1": 75, "f2": 0}, {"i1": 1}, [], 1, None)
        move3 = Move({"f1": 45, "f2": 0}, {"i1": 1}, [], 1, None)
        move4 = Move({"f1": 0, "f2": 0}, {"i1": 1}, [], 1, None)
        test_MST1 = MST(curstate1, desState1, [move1, move2, move3, move4], 2)
        test_MST2 = MST(curstate1, desState1, [move1, move2, move3, move4], 2)
        test_MST3 = MST(curstate1, desState1, [move1, move2, move3, move4], 2)
        actorlow = Actor([test_polelow], curstate1, None, None, .05, None, None, [], [])
        actormiddle = Actor([test_polemiddle], curstate1, None, None, .05, None, None, [], [])
        actorhigh = Actor([test_polehigh], curstate1, None, None, .05, None, None, [], [])
        low_mst = test_polelow.actOnMST(test_MST1, actorlow)
        mid_mst = test_polemiddle.actOnMST(test_MST2, actormiddle)
        high_mst = test_polehigh.actOnMST(test_MST3, actorhigh)
        self.assertTrue(len(low_mst.getMoves()) == 1)
        self.assertTrue(len(high_mst.getMoves()) == 4)
        self.assertTrue(len(mid_mst.getMoves()) == 2)
        self.assertTrue(True)

        if __name__ == '__main__':
            unittest.main()
