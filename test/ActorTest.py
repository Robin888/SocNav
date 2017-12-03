import dm.utils as utils
from dm.Actor import Actor
from dm.Move import Move
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

data = utils.read_moves("../data/moves.csv")

for move in data:
    IO_string_set = set()

    IO_list = [utils.IO_random_sampler(x) for x in
               [move["warmth"],
                move["affinity"], move["legitimacy"],
                move["dominance"], move["competence"]]]
    IO_string = utils.list_to_string(IO_list)
    while IO_string in IO_string_set:
        IO_list = [utils.IO_random_sampler(x) for x in
                   [move["warmth"],
                    move["affinity"], move["legitimacy"],
                    move["dominance"], move["competence"]]]
    Move(move["code"],
         move["move_name"],
         move["move_type"],
         IO_list,
         move["ph"],
         move["low_resources"],
         move["med_resources"],
         move["high_resources"],
         move["infrastructure"],
         category='Build political infrastructure')

actor.makeDecision()
