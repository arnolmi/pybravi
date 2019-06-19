#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pybravi` package."""


from pybravi.lattice import gen_lattice_vector
import numpy as np


def test_gen_lattice_vector():
    vec_a, vec_b = gen_lattice_vector([0, 10], -120)
    assert not np.array_equal(vec_a, vec_b)

    rads = np.arccos(vec_a.dot(vec_b) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b)))
    expected_rads = np.radians(120)
    assert np.abs(rads - expected_rads) <= 0.001
