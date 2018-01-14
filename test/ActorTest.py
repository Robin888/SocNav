import dm.utils as utils
from dm.Actor import Actor
from dm.Move import Move
from dm.Pole import *
from dm.State import State
from dm.risk_calculation import generate_resource_vocab

rationality = RationalityPole(0, 1)
risk = RiskPole(0, 1)
emotion = EmotionalPole(0, 1)
generosity = GenerosityPole(0, 1)
particularHolistic = ParticularHolisticPole(1, 1)
primacyRecency = PrimacyRecencyPole(0, 1)
routineCreative = RoutineCreativePole(0, 1)

data = utils.read_moves("../data/moves.csv")
moves = []
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
    moves.append(Move(move["code"],
                      move["move_name"],
                      move["move_type"],
                      IO_list,
                      move["ph"],
                      [resource.strip() for resource in move["low_resources"].replace(",", " ").split()],
                      [resource.strip() for resource in move["med_resources"].replace(",", " ").split()],
                      [resource.strip() for resource in move["high_resources"].replace(",", " ").split()],
                      move["infrastructure"],
                      category='Build political infrastructure'))

generate_resource_vocab(moves)
# TODO
# one hot for infrastructure as well

s1 = [0] * 52
s2 = [100] * 52
s3 = [-1000] * 52

curState = State({i: s1[i] for i in range(len(s1))}, {0: 0})
desState = State({i: s2[i] for i in range(len(s2))}, {0: 100})
criticalState = State({i: s3[i] for i in range(len(s3))}, {0: -1000})

io_values = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

actor = Actor([rationality, risk, emotion, generosity, particularHolistic, primacyRecency, routineCreative], curState,
              desState, maxTime=2, error=0, history=[], criticalState=criticalState, allActors=[], ioValues=io_values,
              end_io_state=io_values)

for i in range(0, 10):
    actor.makeDecision()
