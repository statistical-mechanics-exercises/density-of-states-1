import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_hamiltonian(self) :
        for i in range(2**5) :
            num, spins = i, 5*[0]
            for j in range(5) :
                spins[j] = np.floor( num / 2**(4-j) )
                num = num - spins[j]*2**(4-j)
                if spins[j]==0 : spins[j] = -1
            energy = -spins[0]*spins[len(spins) - 1 ]
            for i in range(0,len(spins)-1) : energy = energy - spins[i]*spins[i+1]
            self.assertTrue( np.abs(hamiltonian( spins )-energy)<1e-7, "The hamiltonian gives the wrong value for the energy" )
            
    def test_graph(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        k = 0
        for ind in this_x :
            self.assertTrue( ind < 2**8 )
            spins, num = 8*[0], ind 
            for j in range(8) :
                spins[j] = np.floor( num / 2**(7-j) )
                num = num - spins[j]*2**(7-j)
                if spins[j]==0 : spins[j] = -1
            self.assertTrue( this_y[k] == hamiltonian(spins), "The energies have been plotted incorrectly" )
            k = k + 1
   
