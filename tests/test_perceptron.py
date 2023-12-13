# Start up libraries
import sys
sys.path.append(".")
import pytest
import platform
import os

from bin.perceptron import Perceptron

# Test expected to pass
def test_perceptron():
    # GIVEN perceptron object
    the_perceptron = Perceptron()
    # WHEN perceptron is trained with known data set and class labels
    the_perceptron.train([
        [1, 1],
        [1, 0],
        [0, 1],
        [0, 0],
        ], [1, 1, 1, 0])

    # THEN prediction for data points as expected
    assert the_perceptron.predict([1, 1]) == 1, "Error in [1,1], result should be 1"
    assert the_perceptron.predict([1, 0]) == 1, "Error in [1,0], result should be 1"
    assert the_perceptron.predict([0, 1]) == 1, "Error in [0,1], result should be 1"
    assert the_perceptron.predict([0, 0]) == 0, "Error in [0,0], result should be 0"

# Test expected to fail
@pytest.mark.xfail(reason="XFAIL", strict=True)

def test_perceptron_fail():
    # GIVEN perceptron object
    the_perceptron = Perceptron()
    # WHEN perceptron is trained with known data set and class labels
    the_perceptron.train([
        [1, 1],
        [1, 0],
        [0, 1],
        [0, 0],
        ], [1, 1, 1, 0])

    # THEN prediction for data points as expected
    assert the_perceptron.predict([1, 1]) == 0, "Error in [1,1], result should be 0"

# Test expected to be conditionally skipped, OS reason
@pytest.mark.skipif(platform.system()!="Linux", reason="OS is not linux ubuntu")

def test_memory():
    # GIVEN getting all memory using os.popen()
    total_memory, used_memory, free_memory = map(
        int, os.popen('free -t -m').readlines()[-1].split()[1:])

    # THEN check minimum memory levels
    assert total_memory > 0, "total memory is not less than 0"
    assert used_memory > 0, "used memory is not less than 0"
    assert free_memory > 0, "free memory is not less than 0"

# Test is skipped
@pytest.mark.skip(reason="This test is not yet ready for prime test")
def test_bogus():
    # GIVEN initial value of x
    x = "hi"
    
    # THEN check value of data
    assert x == "hey", "X should be 'hey'"

# Test is parametrized
@pytest.mark.parametrize(
        "trainingset, labels, expected",
        [
        ([[1,1],[1,0], [0,1], [0,0]], [1, 0, 0, 0], [1, 0, 0, 0]),
        ([[1,1],[1,0], [0,1], [0,0]], [1, 1, 0, 0], [1, 1, 0, 0]),
        ([[1,1],[1,0], [0,1], [0,0]], [1, 1, 1, 0], [1, 1, 1, 0]),
        ([[1,1],[1,0], [0,1], [0,0]], [1, 1, 1, 1], [1, 1, 1, 1]),
        ([[1,1],[1,0], [0,1], [0,0]], [0, 0, 0, 1], [0, 0, 0, 1]),
        ([[1,1],[1,0], [0,1], [0,0]], [0, 0, 1, 1], [0, 0, 1, 1]),
        ([[1,1],[1,0], [0,1], [0,0]], [0, 1, 1, 1], [0, 1, 1, 1])
        ])

def test_perceptron_parametrized(trainingset, labels, expected):
    # GIVEN perceptron object
    the_perceptron = Perceptron()

    # WHEN perceptron is trained with known data set and class labels
    the_perceptron.train(trainingset, labels)
    
    # THEN check prediction for data points if they match expected
    for i, expectedData in zip(trainingset, expected):
        assert the_perceptron.predict(i) == expectedData, f"Perceptron prediction failed for: {i}"

