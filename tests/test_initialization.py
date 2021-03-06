import numpy
from numpy.testing import assert_, assert_equal, assert_allclose, assert_raises
import theano

from blocks.initialization import Constant, IsotropicGaussian, Uniform


def test_constant():
    def check_constant(const, shape, ground_truth):
        # rng unused, so pass None.
        init = Constant(const).generate(None, ground_truth.shape)
        assert_(ground_truth.dtype == theano.config.floatX)
        assert_(ground_truth.shape == init.shape)
        assert_equal(ground_truth, init)

    # Test scalar init.
    yield (check_constant, 5, (5, 5),
           5 * numpy.ones((5, 5), dtype=theano.config.floatX))
    # Test broadcasting.
    yield (check_constant, [1, 2, 3], (7, 3),
           numpy.array([[1, 2, 3]] * 7, dtype=theano.config.floatX))
    yield (check_constant, numpy.array([[1], [2], [3]]), (3, 2),
           numpy.array([[1, 1], [2, 2], [3, 3]], dtype=theano.config.floatX))


def test_gaussian():
    rng = numpy.random.RandomState([2014, 1, 20])

    def check_gaussian(rng, mean, std, shape):
        weights = IsotropicGaussian(mean, std).generate(rng, shape)
        assert_(weights.shape == shape)
        assert_(weights.dtype == theano.config.floatX)
        assert_allclose(weights.mean(), mean, atol=1e-2)
        assert_allclose(weights.std(), std, atol=1e-2)
    yield check_gaussian, rng, 0, 1, (500, 600)
    yield check_gaussian, rng, 5, 3, (600, 500)


def test_uniform():
    rng = numpy.random.RandomState([2014, 1, 20])

    def check_uniform(rng, mean, width, std, shape):
        weights = Uniform(mean=mean, width=width,
                          std=std).generate(rng, shape)
        assert_(weights.shape == shape)
        assert_(weights.dtype == theano.config.floatX)
        assert_allclose(weights.mean(), mean, atol=1e-2)
        if width is not None:
            std_ = width / numpy.sqrt(12)
        else:
            std_ = std
        assert_allclose(std_, weights.std(), atol=1e-2)
    yield check_uniform, rng, 0, 0.05, None, (500, 600)
    yield check_uniform, rng, 0, None, 0.001, (600, 500)
    yield check_uniform, rng, 5, None, 0.004, (700, 300)

    assert_raises(ValueError, Uniform, 0, 1, 1)
