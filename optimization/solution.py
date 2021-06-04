"""Solution of the exercises of Optimization of compute bound Python code"""
import math
import cmath
import numpy as np
import numexpr as ne
import numba as nb

# Needed here since it is used as global variables
# Maximum strain at surface
e0 = 0.01
# Width of the strain profile below the surface
w = 5.0


# Python: Circular crystal ###


def circ_python_1(N, h, k):
    x = (np.arange(N) - N / 2).reshape(-1, 1)
    y = (np.arange(N) - N / 2).reshape(1, -1)
    omega = x * x + y * y <= (N / 2) ** 2
    result = np.zeros((h.size, k.size))
    for i_h, v_h in enumerate(h):  # loop over the reciprocal space coordinates
        for i_k, v_k in enumerate(k):
            # One should discard bad values
            tmp = 0.0
            for n in range(N):  # loop and sum over unit-cells
                for m in range(N):
                    if omega[n, m]:
                        tmp += cmath.exp(2j * np.pi * (v_h * n + v_k * m))
            result[i_h][i_k] = abs(tmp) ** 2
    return result


# Alternative using Python `sum`
def circ_python_1_alt(N, h, k):
    # Filter-out position outside crystal once for all
    inside_pos = [
        (n, m)
        for n in range(N)
        for m in range(N)
        if ((n - N / 2) ** 2 + (m - N / 2) ** 2) <= (N / 2) ** 2
    ]

    result = np.zeros((h.size, k.size))
    for i_h, v_h in enumerate(h):  # loop over the reciprocal space coordinates
        for i_k, v_k in enumerate(k):
            result[i_h][i_k] = (
                abs(
                    sum(  # Sum over positions inside the crystal
                        cmath.exp(2j * np.pi * (v_h * n + v_k * m))
                        for n, m in inside_pos
                    )
                )
                ** 2
            )
    return result


# Python: Circular strained crystal ###


def circ_python(N, h, k):
    N_2 = N / 2
    positions = {}
    for i in range(N):
        x = i - N_2
        for j in range(N):
            y = j - N_2
            r = (x * x + y * y) ** 0.5
            if r <= N_2:
                strain = e0 * (1 + math.tanh((r - N_2) / w))
                positions[(i, j)] = (i + strain * x, j + strain * y)
    result = np.zeros((h.size, k.size))
    for i_h, v_h in enumerate(h):  # loop over the reciprocal space coordinates
        for i_k, v_k in enumerate(k):
            # One should discard  bad values
            tmp = 0.0
            for i_n in range(N):  # loop and sum over unit-cells
                for i_m in range(N):
                    pos = positions.get((i_n, i_m))
                    if pos:
                        n_s, m_s = pos
                        tmp += cmath.exp(2j * np.pi * (v_h * n_s + v_k * m_s))
            result[i_h, i_k] = abs(tmp) ** 2
    return result


# Alternative computing list of strained position
def circ_python_alt(N, h, k):
    # Compute strained position inside the crystal once for all
    strained_pos = []
    crystal_radius = N / 2
    for n in range(N):
        for m in range(N):
            # Center is at (N/2, N/2)
            x = n - crystal_radius
            y = m - crystal_radius
            radius = (x ** 2 + y ** 2) ** 0.5
            if radius <= crystal_radius:
                delta = e0 * (1 + math.tanh((radius - crystal_radius) / w))
                strained_pos.append((n + delta * x, m + delta * y))

    result = np.zeros((h.size, k.size))
    for i_h, v_h in enumerate(h):  # loop over the reciprocal space coordinates
        for i_k, v_k in enumerate(k):
            result[i_h][i_k] = (
                abs(
                    sum(
                        cmath.exp(2j * np.pi * (v_h * n_s + v_k * m_s))
                        for n_s, m_s in strained_pos
                    )
                )
                ** 2
            )
    return result


# numpy ###


def circ_numpy(N, h, k):
    N_2 = N / 2
    h = h.reshape(-1, 1, 1, 1)
    k = k.reshape(1, -1, 1, 1)
    n = np.arange(N).reshape(1, 1, -1, 1)
    m = np.arange(N).reshape(1, 1, 1, -1)
    radius = np.sqrt((n - N_2) ** 2 + (m - N_2) ** 2)
    strain = e0 * (1.0 + np.tanh((radius - N_2) / w))
    p_n = n + strain * (n - N_2)
    p_m = m + strain * (m - N_2)
    omega = radius <= N_2
    tmp = omega * np.exp(2j * np.pi * (h * p_n + k * p_m))
    return np.abs(tmp.sum(axis=(2, 3))) ** 2


# numexpr ###


def circ_numexpr(N, h, k):
    N_2 = N / 2
    h = h.reshape(-1, 1, 1, 1)
    k = k.reshape(1, -1, 1, 1)
    n = np.arange(N).reshape(1, 1, -1, 1)
    m = np.arange(N).reshape(1, 1, 1, -1)
    radius = ne.evaluate("sqrt((n - N_2)**2 + (m - N_2)**2)")
    strain = ne.evaluate("e0 * (1 + tanh((radius-N_2) / w))")
    j2pi = np.pi * 2j
    tmp = ne.evaluate(
        "where(radius > N_2, 0, exp(j2pi*(h*(n+strain*(n-N_2)) + k*(m+strain*(m-N_2)))))"
    )
    result = abs(tmp.sum(axis=(2, 3))) ** 2
    return result


# numba ###


@nb.jit(parallel=True)
def circ_numba(N, h, k):
    result = np.zeros((h.size, k.size), dtype=np.float64)
    N_2 = N / 2
    for h_i in nb.prange(h.size):  # loop over the reciprocal space coordinates
        for k_i in range(k.size):
            tmp = 0j
            for n in range(N):  # loop and sum over unit-cells
                for m in range(N):
                    radius = math.sqrt((n - N_2) ** 2 + (m - N_2) ** 2)
                    if radius > (N_2):
                        value = 0j
                        # continue  # Numba isn't working using the same continue pattern as below
                    else:
                        strain = e0 * (1 + math.tanh((radius - N_2) / w))
                        p_n = n + strain * (n - N_2)
                        p_m = m + strain * (m - N_2)
                        value = np.exp(2j * cmath.pi * (h[h_i] * p_n + k[k_i] * p_m))
                    tmp += value
            result[h_i, k_i] = abs(tmp) ** 2
    return result
