import numpy as np
import scipy.integrate

def calc_trap_integral(func, a, b, n):
    """
    Calculate the integral of a function using the trapezoidal rule.

    Parameters:
    func : callable
        The function to integrate.
    a : float
        The lower limit of integration.
    b : float
        The upper limit of integration.
    n : int
        The number of subintervals.

    Returns:
    float
        The approximate value of the integral.
    """

    integral = scipy.integrate.trapz([func(x) for x in np.linspace(a, b, n+1)], np.linspace(a, b, n+1))
    return round(integral, 4)

# Example usage:
def example_function(x):
    return np.exp(x) * np.sin(x)

print(calc_trap_integral(example_function, 0, np.pi, 8))  