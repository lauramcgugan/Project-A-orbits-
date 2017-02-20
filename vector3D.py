"""
Project 2A:
Collection of functions for various vector manipulations.

Authors: E. Zaid and L. McGugan
Version: 20/02/2017
"""

import math
import numpy as np

 
def normSq(v):
        """
        Return the square of the magnitude of the vector
        :param v: the vector
        :return: sum of the squared vector elements v[0]**2 + v[1]**2 + v[2]**2
        """
	return v[0]**2 + v[1]**2 + v[2]**2


def norm(v):
        """
        Return the magnitude of the vector
        :param v: the vector
        :return: square root of the sum of the squared vector elements {v[0]**2 + v[1]**2 + v[2]**2}**1/2
        
        """
	return math.sqrt(normSq(v))

 
def scal_m(v,a):
        """
        Multiply vector by a scalar
        :param v: vector
        :param a: scalar
        :return: product of vector and scalar v*a
        """
	return v*a


def scal_d(v,a):
        """
        Divide vector by a scalar
        :param v: vector
        :param a: scalar
        :return: quotient of vector and scalar v/a
        """
	return v/a


def add(v,u):
        """
        Sum of two vectors
        :param v: first vector
        :param u: second vector
        :return: the sum of two vectors v+u
        """
	return v+u

 
def diff(v,u):
        """
        Difference of two vectors
        :param v: first vector
        :param u: second vector
        :return: the difference of two vectors v-u        
        """
	return v-u


def dot(v,u):
        """
        Scalar product of two vectors
        :param v: first vector
        :param u: second vector
        :return: the sum of the product of the corresponding elements v[0]*u[0] +v[1]*u[1] + v[2]*u[2]
        """
	return v[0]*u[0] +v[1]*u[1] + v[2]*u[2]


def cross(v,u):
        """
        Vector cross product of two vectors
        :param v: first vector
        :param u: second vector
        :return: the vector product v cross u
        """
	e0=(v[1]*u[2]-v[2]*u[1])
	e1=-(v[0]*u[2]-v[2]*u[0])
	e2=(v[0]*u[1]-v[1]*u[0])
	return np.array([e0,e1,e2]) 

 




