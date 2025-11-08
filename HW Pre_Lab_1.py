import numpy as np
import scipy.integrate as spi
from scipy.integrate import trapz
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

    integral = trapz([func(x) for x in np.linspace(a, b, n+1)], np.linspace(a, b, n+1))
    return integral

# Example usage:
print(calc_trap_integral(np.exp(x)*np.sin(x), 0, np.pi, 8))  