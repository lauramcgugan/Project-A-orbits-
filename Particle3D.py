"""
Computer Modelling Project A

Authors: E. Zaid and L. McGugan
14/02/2017

"""

# Import vector3D containing 3D vector calculations from exercise 2
import numpy as np
import vector3D as vc

# Create Particle 3D class
class Particle3D(object):

    # Initialise a Particle3D instance
    def __init__(self, mass, label, x_pos, y_pos, z_pos, x_vel, y_vel, z_vel):
        self.mass = mass
        self.label = label
        self.position = np.array([x_pos, y_pos, z_pos])
        self.velocity = np.array([x_vel, y_vel, z_vel])

    # Define formatted string output
    def __str__(self):
        return "label = " + str(self.label) + " r = " + str(self.position)

        
    # Kinetic energy
    def KE(self):
        return 0.5*self.mass*vc.norm(self.velocity)**2

    # Time integration methods
    # First-order velocity update
    def leapVelocity(self, dt, force):
        self.velocity = self.velocity + dt*force/self.mass

    # First-order position update
    def leapPosFirst(self, dt):
        self.position = self.position + dt*self.velocity

    # Second-order position update
    def leapPosSecond(self, dt, force):
        self.position = self.position + dt*self.velocity + 0.5*dt**2*force/self.mass

    # Define static method to calculate particle separation
    @staticmethod
    def separation(particle1, particle2):
        return particle1.position - particle2.position
