Numpy
=====

Numpy is the de facto standard for efficient matrix representations and
(BLAS level 1-3) computations.  Scipy implements more high-level
algorithms for scientific computing (Lapack, statistics,...).

What is it?
-----------
1. `data_plot.py`: reads a CSV file containing data, performs linear
    regression, and plots the data and the line representing the regression;
    numpy is used to represent the data, scipy to perform the linear
    regression, matplotlib for plotting the result
1. `data_writer.py`: produces data for the `data_plot.py` script, linear
    with noise added
1. `data.csv`: example data set for `data_plot.py`
1. `fft.py`: creates a signal consisting of a sum of cosine functions
    with specified amplitudes and frequencies, adding noise; plots the
    resulting function, uses FFT to determine the frequency spectrum, and
    plot the latter
1. `numba_test.py`: some timing tests for numpy constructs, including the
    use of numba.  Note that this requires installing numba, which is, due
    to its dependencies, perhaps non-trivial
1. `optimization.py`: illustration of how to use the `scipy.optimize` for
    unconstrained multivariate optimization
1. `target_function_plot.py`: script that creates a surface plot of the
    target function in `optimization.py`