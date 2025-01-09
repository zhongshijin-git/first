from mindquantum import *


circ = Circuit()
n_qubits = 6
circ += UN(H, n_qubits)

circ += BarrierGate(True)
circ += X.on(2)
circ += X.on(0)
circ += PhaseShift(1.8614).on(5,[1,0,2,3,4])
circ += X.on(2)
circ += X.on(0)




circ += BarrierGate(True)
circ += X.on(2)
circ += X.on(3)
circ += PhaseShift(1.8614).on(5,[1,0,2,3,4])
circ += X.on(3)
circ += X.on(2)


circ += BarrierGate(True)
circ += X.on(0)
circ += X.on(3)
circ += X.on(2)
circ += X.on(4)
circ += PhaseShift(1.8614).on(5,[1,0,2,3,4])
circ += X.on(3)
circ += X.on(2)
circ += X.on(4)
circ += X.on(0)

circ += BarrierGate(True)
circ += UN(RY(1.5708), n_qubits)
circ += PhaseShift(1.8614).on(5,[1,0,2,3,4])
circ += UN(RY(-1.5708), n_qubits)
circ += BarrierGate(True)


circ += X.on(2)
circ += X.on(0)
circ += PhaseShift(1.8614).on(5,[1,0,2,3,4])
circ += X.on(2)
circ += X.on(0)




circ += BarrierGate(True)
circ += X.on(2)
circ += X.on(3)
circ += PhaseShift(1.8614).on(5,[1,0,2,3,4])
circ += X.on(3)
circ += X.on(2)


circ += BarrierGate(True)
circ += X.on(0)
circ += X.on(3)
circ += X.on(2)
circ += X.on(4)
circ += PhaseShift(1.8614).on(5,[1,0,2,3,4])
circ += X.on(4)
circ += X.on(2)
circ += X.on(3)
circ += X.on(0)

circ += BarrierGate(True)
circ += UN(RY(1.5708), n_qubits)
circ += PhaseShift(1.8614).on(5,[1,0,2,3,4])
circ += UN(RY(-1.5708), n_qubits)
circ += BarrierGate(True)

circ += X.on(2)
circ += X.on(0)
circ += PhaseShift(1.8614).on(5,[1,0,2,3,4])
circ += X.on(2)
circ += X.on(0)




circ += BarrierGate(True)
circ += X.on(2)
circ += X.on(3)
circ += PhaseShift(1.8614).on(5,[1,0,2,3,4])
circ += X.on(3)
circ += X.on(2)


circ += BarrierGate(True)
circ += X.on(0)
circ += X.on(3)
circ += X.on(2)
circ += X.on(4)
circ += PhaseShift(1.8614).on(5,[1,0,2,3,4])
circ += X.on(4)
circ += X.on(2)
circ += X.on(3)
circ += X.on(0)

circ += BarrierGate(True)
circ += UN(RY(1.5708), n_qubits)
circ += PhaseShift(1.8614).on(5,[1,0,2,3,4])
circ += UN(RY(-1.5708), n_qubits)
circ += BarrierGate(True)



circ += X.on(2)
circ += X.on(0)
circ += PhaseShift(1.8614).on(5,[1,0,2,3,4])
circ += X.on(2)
circ += X.on(0)




circ += BarrierGate(True)
circ += X.on(2)
circ += X.on(3)
circ += PhaseShift(1.8614).on(5,[1,0,2,3,4])
circ += X.on(3)
circ += X.on(2)


circ += BarrierGate(True)
circ += X.on(0)
circ += X.on(3)
circ += X.on(2)
circ += X.on(4)
circ += PhaseShift(1.8614).on(5,[1,0,2,3,4])
circ += X.on(4)
circ += X.on(2)
circ += X.on(3)
circ += X.on(0)

circ += BarrierGate(True)
circ += UN(RY(1.5708), n_qubits)
circ += PhaseShift(1.8614).on(5,[1,0,2,3,4])
circ += UN(RY(-1.5708), n_qubits)
circ += BarrierGate(True)




circ += Measure().on(0)      
circ += Measure().on(1)
circ += Measure().on(2)
circ += Measure().on(3)
circ += Measure().on(4)
circ += Measure().on(5)
sim = Simulator("mqvector", circ.n_qubits)  
res = sim.sampling(circ, shots=10000)

print(res)
circ.svg()