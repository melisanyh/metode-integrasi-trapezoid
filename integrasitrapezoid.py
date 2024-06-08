import time
import numpy as np

def f(x):
    return 4 / (1 + x**2)

def trapezoid_integration(N):
    delta_x = 1 / N
    x_values = np.linspace(0, 1, N+1)
    integral_sum = sum(0.5 * (f(x_values[i]) + f(x_values[i+1])) for i in range(N))
    return delta_x * integral_sum

def calculate_pi(N):
    integral_value = trapezoid_integration(N)
    return integral_value

def calculate_error(approx_pi):
    return abs(np.pi - approx_pi)

# Testing
N_values = [10, 100, 1000, 10000]
for N in N_values:
    start_time = time.time()
    approx_pi = calculate_pi(N)
    end_time = time.time()

    execution_time = end_time - start_time
    error = calculate_error(approx_pi)

    print(f"N = {N}, Approximated Pi = {approx_pi}, RMS Error = {error}, Execution Time = {execution_time} seconds")
