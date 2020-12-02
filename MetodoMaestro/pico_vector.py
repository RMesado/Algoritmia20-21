from typing import *


def busca_pico(a: List[int]) -> Optional[int]:
    def rec(b: int, e: int) -> Optional[int]:
        num_elem = e - b
        if num_elem == 0:  # is_simple
            return None  # trivial_solution
        elif num_elem == 1:
            return b
        elif num_elem == 2:
            if a[b] >= a[b + 1]:
                return b
            return b + 1
        else:                   # decrease
            h = (b + e) // 2
            if a[h] <= a[h + 1]:
                return rec(h + 1, e)
            else:
                return rec(b, h + 1)

    return rec(0, len(a))


if __name__ == '__main__':
    v = [-10, -1, -1, -1]
    print(busca_pico(v))
