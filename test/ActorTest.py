from dm.Actor import Actor
from dm.Pole import *
from dm.State import State

rationality = RationalityPole(1, 1)
risk = RiskPole(1, 1)
emotion = EmotionalPole(1, 1)
generosity = GenerosityPole(1, 1)
particularHolistic = ParticularHolisticPole(1, 1)
primacyRecency = PrimacyRecencyPole(1, 1)
routineCreative = RoutineCreativePole(1, 1)

curState = State({'f1': 0}, {'i1': 0})
desState = State({'f1': 100}, {'i1': 100})
criticalState = State({'f1': -10000}, {'i1': -10000})

io_values = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

actor = Actor([rationality, risk, emotion, generosity, particularHolistic, primacyRecency, routineCreative], curState,
              desState, maxTime=10, error=0, history=[], criticalState=criticalState, allActors=[], ioValues=io_values,
              end_io_state=io_values)

actor.makeDecision()
