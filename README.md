# Plotting the energies of all the microstates

The previous exercises taught you how to compute the ensemble averages for physical properties such as the magnetisation and the energy.  This is not the whole story, however, as the values of these quantities will fluctuate around these average values even when the system is at equilibrium.  Over the course of these last few exercises we are thus going to learn how to characterise how much these physical quantities will fluctuate by learning to compute the distribution of values that the magnetisation and the energy takes.  Before getting on to that, however, let's first look at the energies of all the microstates that a system of eight spins can be within.

In this exercise, we are going to look at the 1D Ising model in the absence of a magnetic field.  The Hamiltonian that you will need to implement in the box on the left here is thus:

![](https://render.githubusercontent.com/render/math?math=E=-\sum_{i=1}^Ns_is_{i%2B1})

Furthermore, notice that (as always) ![](https://render.githubusercontent.com/render/math?math=s_{N%2B1}=s_1).

I have written a loop that will run over all the microstates within the code for you.  Within this loop you will need to implement the usual algorithm that converts each of the integers between 0 and ![](https://render.githubusercontent.com/render/math?math=2^8-1) to a set of microscopic coordinates for a system of 8 spins. 

You will notice that I have created a list called `indices` and a list called `energies` that will ultimately hold each of the numerical indices for the microstates and the energies of each of the microstates respectively.  I have then written code to plot these `indices` against the `energies`.  The final result of your calculation will thus be a graph that contains a point that shows the energy of each of the various microstates.
