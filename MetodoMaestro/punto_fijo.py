from typing import *


def punto_fijo(a: List[int]) -> Optional[int]:
    def rec(b: int, e: int) -> Optional[int]:
        num_elem = e - b
        if num_elem == 0:  # is_simple
            return None  # trivial_solution
        elif num_elem == 1:
            if a[b] == b:
                return b
            return None
        else:  # decrease
            h = (b + e) // 2
            if a[h] < h:
                return rec(h, e)
            elif a[h] > h:
                return rec(b, h)
            else:
                return h
    return rec(0, len(a))


if __name__ == '__main__':
    v = [-10, -5, 1, 3, 10]
    print(punto_fijo(v))
