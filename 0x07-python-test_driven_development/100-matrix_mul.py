#!/usr/bin/python3
"""Module `100-matrix_mul`

This module supplies one function, `matrix_mul()`.
"""


def matrix_mul(m_a, m_b):
    """Multiplies 2 matrices `m_a` and `m_b`.

    Args:
        m_a (:obj:`int` of :obj:`list` of :obj:`list`): First matrix
        m_b (:obj:`int` of :obj:`list` of :obj:`list`): Second matrix

    Returns:
        (:obj:`int` of :obj:`list` of :obj:`list`): Product of `m_a` and `m_b`.
    """

    lol_a = lol_b = len_amsg = len_bmsg = None
    len_a = len_b = a_col = b_row = 0

    if (type(m_a) is not list):
        raise TypeError("m_a must be a list")
    if (type(m_b) is not list):
        raise TypeError("m_b must be a list")
    for el in m_a:
        if type(el) is not list:
            raise TypeError("m_a must be a list of lists")
        else:
            len_a = len_a if len_a != 0 else len(el)

        if len(el) != len_a:
            len_amsg = "each row of m_a must be of the same size"

        for num in el:
            if type(num) not in [int, float]:
                lol_a = "m_a should contain only integers or floats"
    for el in m_b:
        if type(el) is not list:
            raise TypeError("m_b must be a list of lists")
        else:
            len_b = len_b if len_b != 0 else len(el)

        if len(el) != len_b:
            len_bmsg = "each row of m_b must be of the same size"

        for num in el:
            if type(num) not in [int, float]:
                lol_b = "m_b should contain only integers or floats"
    # O((n^2)^2) Abominable time complexity :D
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    if lol_a:
        raise TypeError(lol_a)
    if lol_b:
        raise TypeError(lol_b)
    if len_amsg:
        raise TypeError(len_amsg)
    if len_bmsg:
        raise TypeError(len_bmsg)
    for _ in m_a[0]:
        a_col += 1
    for _ in m_b:
        b_row += 1
    if a_col != b_row:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[sum(a * b for a, b in zip(A_row, list(B_col)))
               for B_col in zip(*m_b)] for A_row in m_a]

    return result
