from itertools import combinations, permutations, tee
from comch import SymmetricGroupElement, SymmetricGroup


def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def ainfty(i, console=False, latex=True):
    for k in range(1, i + 1):
        for n in range(i - k + 1):
            x = k + n + k * n
            y = i - k - n
            z = i - k + 1

            if console:
                print(f'i={i}, k={k}, n={n}')
                print('k+n+kn =', x)
                print('i-k-n  =', y)
                print('k      =', k)
                print('n      =', n)
                print('i-k+1  =', z)

            if latex:
                print(fr'\noindent $i={i}, k={k}, n={n}$:')
                print(r'\begin{align*}')
                print(fr'(-1)^{x} \big( \id_C^{{\otimes {y}}} \otimes '
                      fr'\Delta_{k} \otimes \id_C^{{\otimes {n}}} \big) ' +
                      fr'\Delta_{z}(c)')
                print(r'\end{align*}')
                print()


def delta(i):
    r"""Action of \Delta_i on degree 1 generator c"""
    deltas = []
    delta1 = 'y-z'
    deltas.append(delta1)
    delta2 = r'-\frac{1}{2} \Big( c \otimes (y+z) + (y+z) \otimes c \Big)'
    deltas.append(delta2)
    delta3 = r'\frac{1}{12} \ (y-z) \otimes c \otimes c + ' + \
        r'\frac{1}{6} \ c \otimes (y-z) \otimes c + ' + \
        r'\frac{1}{12} \ c \otimes c \otimes (y-z)'
    deltas.append(delta3)

    return deltas[i - 1]


# print(delta(3))
# ainfty(3, latex=False, console=True)

# n = 3
# for i in range(1, n):
#     print('i =', i)
#     for sigma in SymmetricGroup.shuffles(i, n - i):
#         print(sigma.sign * (-1)**i, sigma)

for sigma in SymmetricGroup.shuffles(2, 1):
    print(sigma)
