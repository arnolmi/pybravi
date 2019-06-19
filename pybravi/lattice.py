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


# def gen_hexagonal_cell(shape, lattice_vectors):
#    """
#    stub
#    """
#    pass


# def lattice_factory(lattice_type):
#    """
#    stub
#    """
#    pass
