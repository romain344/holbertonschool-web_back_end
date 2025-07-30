#!/usr/bin/env python3
"""définie la fonction elment_length"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return à i """
    return [(i, len(i)) for i in lst]
