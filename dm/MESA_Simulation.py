import sys
sys.path.append("..")
import dm.utils as utils
from dm.Move import Move
from dm.Pole import *
from dm.State import State
from dm.risk_calculation import generate_resource_vocab
from dm.MST import MST
from dm import IO
from dm import risk_calculation
from dm.Event import Event
from mesa import Model
from mesa.time import RandomActivation,BaseScheduler
from dm.Actor_MESA import Actor

        # do something else

class Simulator(Model):
    """A model with some number of agents."""
    
    def __init__(self, N):
        super().__init__(N)
        self.num_agents = N
        self.schedule = RandomActivation(self)
        
  ################### Create global resources####################################
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
        
        s1 = [1000] * 52
        s2 = [100] * 52
        s3 = [-1000] * 52
        
        curState = State({i: s1[i] for i in range(len(s1))}, {0: 0})
        desState = State({i: s2[i] for i in range(len(s2))}, {0: 100})
        criticalState = State({i: s3[i] for i in range(len(s3))}, {0: -1000})
        
        io_values = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
        
        globalresource = Actor(unique_id=0,model=self,
                      poles=[rationality, risk, emotion, generosity, particularHolistic, primacyRecency, routineCreative],
                      currentState = curState, desiredState=desState, maxTime=2, error=0, 
                      history=[], criticalState=criticalState, allActors=[], ioValues=io_values,
                      end_io_state=io_values)
        self.schedule.add(globalresource)
#############################################################################
        
############################# add an actor###################################
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
        
        actor = Actor(unique_id=1,model=self,
                      poles=[rationality, risk, emotion, generosity, particularHolistic, primacyRecency, routineCreative],
                      currentState = curState, desiredState=desState, maxTime=2, error=0, 
                      history=[], criticalState=criticalState, allActors=[], ioValues=io_values,
                      end_io_state=io_values)
        self.schedule.add(actor)
##############################################################################
        
############################# add an actor###################################
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
        
        s1 = [10] * 52
        s2 = [100] * 52
        s3 = [-1000] * 52
        
        curState = State({i: s1[i] for i in range(len(s1))}, {0: 0})
        desState = State({i: s2[i] for i in range(len(s2))}, {0: 100})
        criticalState = State({i: s3[i] for i in range(len(s3))}, {0: -1000})
        
        io_values = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
        
        actor2 = Actor(unique_id=2,model=self,
                      poles=[rationality, risk, emotion, generosity, particularHolistic, primacyRecency, routineCreative],
                      currentState = curState, desiredState=desState, maxTime=2, error=0, 
                      history=[], criticalState=criticalState, allActors=[], ioValues=io_values,
                      end_io_state=io_values)
        self.schedule.add(actor2)
##############################################################################
        
       

    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()
        
    
    def multi_step_collector(self,times):
        initial_state={}
        for a in empty_model.schedule.agents:
            initial_state[a.unique_id]=a.currentState.resources.copy()
        data_collector=[]
        data_collector.append(initial_state)
        moves_made=[]
        for i in range(times):
            self.step()
            temp_state={}
            temp_move={}
            for a in empty_model.schedule.agents:
                temp_state[a.unique_id]=a.currentState.resources.copy()
                temp_move[a.unique_id]=a.moves_made
            data_collector.append(temp_state)
            moves_made.append(temp_move)
        return data_collector,moves_made
    
    def watcher(self,times,agent_alert=[],resources_alert={},moves_alert=[]):#three conditions in total
        initial_state={}
        for a in empty_model.schedule.agents:
            initial_state[a.unique_id]=a.currentState.resources.copy()
        data_collector=[]
        data_collector.append(initial_state)
        moves_made=[]
        for i in range(times):
            self.step()
            temp_state={}
            temp_move={}
            
            for a in empty_model.schedule.agents:
                temp_state[a.unique_id]=a.currentState.resources.copy()
                temp_move[a.unique_id]=a.moves_made
                
                #one condition
                if a.unique_id in agent_alert and len(resources_alert)==0 and len(moves_alert)==0:
                    print('the moves that actor',a.unique_id,'made at step',i+1, 'is', a.moves_made)
                    print('the resources of actor',a.unique_id,'made at step',i+1, 'is', a.currentState.resources)
                if  len(moves_alert)!=0 and len(agent_alert)==0 and len(resources_alert)==0:
                    for m in moves_alert:
                        if m in [str(e) for e in a.moves_made]:
                            print('actor',a.unique_id,'made the move',m,'at step',i+1)   
                if len(resources_alert)!=0 and len(agent_alert)==0 and len(moves_alert)==0:
                    for r in resources_alert.keys():
                        if a.currentState.resources[r]==resources_alert[r]:
                            print('the resources',r,'of actor',a.unique_id,'reach',resources_alert[r],'at step', i+1)
                
                #two conditions
                if a.unique_id in agent_alert and len(resources_alert)!=0:
                    for r in resources_alert.keys():
                        if a.currentState.resources[r]==resources_alert[r]:
                            print('the resources',r,'of actor',a.unique_id,'reach',resources_alert[r],'at step', i+1)
                if  len(moves_alert)!=0 and a.unique_id in agent_alert:
                    for m in moves_alert:
                        if m in [str(e) for e in a.moves_made]:
                             print('actor',a.unique_id,'made the move',m,'at step',i+1) 
                
            data_collector.append(temp_state)
            moves_made.append(temp_move)
        print('simulation done!')    
        return data_collector,moves_made
        
        
            
            
        


empty_model = Simulator(N=1)
#data, moves=empty_model.multi_step_collector(20)
data, moves=empty_model.watcher(100,agent_alert=[1],resources_alert={5:31},moves_alert=['Threaten'])
