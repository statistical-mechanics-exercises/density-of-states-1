import matplotlib.pyplot as plt 
import numpy as np 

def hamiltonian( spins ) :
  eng = 0
  # Your code to calculate the Hamiltonian goes here
  eng = -spins[0]*spins[-1]
  for i in range(1,len(spins)) : eng = eng - spins[i-1]*spins[i]
  return eng

# Generate an index for each microstate
indices = []
for i in range(2**8) : indices.append(i)

energies = []
for index in indices :
  spins, ind = 8*[0], index 
  # Your code to convert the integer index to the corresponding spin coordinates goes here
  for i in range(8) :
      spins[i] = np.floor( index / 2**(7-i) )
      index = index - spins[i]*(2**(7-i))
      if spins[i]==0 : spins[i] = -1
  energies.append( hamiltonian( spins ) )

# This will plot the energies of the configurations against their numerical indexes. 
plt.plot( indices, energies, 'ko')
plt.xlabel("numerical index")
plt.ylabel("energy / J")
plt.savefig( "index_versus_energy.png")
