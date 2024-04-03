import math
import numpy as np
from bucket import Bucket


def test_bucket_init():
    radius = 1
    height = 2
    b = Bucket(radius, height)
    assert b.radius == radius
    assert b.height == height
    assert b.filling == 0.5


def test_fill_bucket():
    radius = 1
    height = 1
    volume = math.pi * radius**2 * height  # volume of bucket
    b = Bucket(radius, height)  # default filling fraction is 50%
    b.fill(volume / 4)  # fill bucket up to 75%
    assert np.allclose(b.filling, 0.75)


def test_overfill_bucket():
    b = Bucket(1, 1)
    b.fill(200)
    assert np.allclose(b.filling, 1)



def test_bucket_volume():
    b = Bucket(1, 1)
    assert np.allclose(b.bucket_volume, math.pi)


def test_underfill_bucket():
     b = Bucket(1, 1)
     volume = math.pi
     # force underflow by removing a full bucket
     b.fill(-volume )
     assert np.allclose(b.filling, 0)
