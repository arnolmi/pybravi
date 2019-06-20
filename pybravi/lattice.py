"""
module for generating bravais lattices.
"""
import numpy as np


def gen_lattice_vector(vector, angle):
    """
    Generates the component of a lattice vector given an angle.

    Args:
        vector (np.array): the first vector
        angle  (int): the angle in degrees.
    """
    radians = np.radians(angle)
    cos, sin = np.cos(radians), np.sin(radians)
    rotation_matrix = np.array([[cos, sin], [-sin, cos]])
    a_vec = np.array(vector)
    b_vec = np.dot(rotation_matrix, a_vec)
    return b_vec, a_vec


def gen_lattice(shape, lattice_vectors):
    """
    Generates a lattice given a shape and lattice vectors

    Args:
       shape (tuple): shape of the lattice in a grid of points
       lattice_vectors (np.array): a pair of lattice vectors
    """
    # Translate along one vector to fill up the bottom row.
    x_pts = np.arange(0, shape[0])
    x_component = lattice_vectors[0][0]*x_pts
    y_component = lattice_vectors[0][1]*x_pts
    base = np.dstack((x_component, y_component))
    # now copy this array N times
    points = np.array([x*np.array(lattice_vectors[1]) +
                       base for x in range(0, shape[1])]).reshape(shape[0]*shape[1], 2)
    return points
