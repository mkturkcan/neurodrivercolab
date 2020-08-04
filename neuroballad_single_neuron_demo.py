from neuroballad import * #Import Neuroballad
C = Circuit() #Create a circuit
C.add([0], LeakyIAF(resting_potential = -70.0,
                    reset_potential = -70.0,
                    threshold = -45.0, #
                    capacitance = 2.0, # in mS
                    resistance = 10.0, # in Ohm
                    )) #Create a single leaky IAF neuron

C.add([1], HodgkinHuxley()) #Create a single HH neuron

C_in_a = InIStep(0, 40., 0.20, 0.40) #Create current input for node 0
C_in_b = InIStep(1, 40., 0.20, 0.40) #Create current input for node 1
C.sim(1., dt = 1e-4, in_list = [C_in_a, C_in_b]) #Use the three inputs and simulate