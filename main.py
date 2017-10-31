import numpy as np
import pyquil.quil as pq
import pyquil.api as api
import pyquil.gates as gates


def pauli_x(qubit_in, register_out=0):
  p = pq.Program()
  p.inst(gates.X(qubit_in)).measure(0, register_out)
  return p, [register_out]


def coin_flip(qubit_in, register_out=0):
  p = pq.Program()
  p.inst(gates.H(qubit_in)).measure(0, register_out)
  return p, [register_out]


def main():
  qvm = api.SyncConnection()

  p, rs = pauli_x(0)
  print("5 trials of X|0> measured:", qvm.run(p, rs, trials=5))

  p, rs = pauli_x(1)
  print("5 trials of X|1> measured:", qvm.run(p, rs, trials=5))

  p, rs = coin_flip(0)
  print("5 trials of H|0> measured:", qvm.run(p, rs, trials=5))


if __name__ == "__main__":
  main()
