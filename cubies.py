# cubies.py


def cubies_affected(rotation):
    if rotation in _cubies_after_rotation:
        return list(_cubies_after_rotation[rotation].keys())
    else:
        return []


def rotate_cuby(cuby, rotation):
    if rotation in _cubies_after_rotation:
        if cuby in _cubies_after_rotation[rotation]:
            return _cubies_after_rotation[rotation][cuby]
        else:
            return cuby
    else:
        return cuby


_cubies_after_rotation = {
    "U": {
        "ULF": "ULB",
        "UF": "UL",
        "URF": "ULF",
        "UR": "UF",
        "URB": "URF",
        "UB": "UR",
        "ULB": "URB",
        "UL": "UB",
    },
    "D": {
        "DLF": "DRF",
        "DF": "DR",
        "DRF": "DRB",
        "DR": "DB",
        "DRB": "DLB",
        "DB": "DL",
        "DLB": "DLF",
        "DL": "DF",
    },
    "L": {
        "ULF": "DLF",
        "UL": "LF",
        "ULB": "ULF",
        "LB": "UL",
        "DLB": "ULB",
        "DL": "LB",
        "DLF": "DLB",
        "LF": "DL",
    },
    "R": {
        "URF": "URB",
        "RF": "UR",
        "DRF": "URF",
        "DR": "RF",
        "DRB": "DRF",
        "RB": "DR",
        "URB": "DRB",
        "UR": "RB",
    },
    "F": {
        "ULF": "URF",
        "UF": "RF",
        "URF": "DRF",
        "RF": "DF",
        "DRF": "DLF",
        "DF": "LF",
        "DLF": "ULF",
        "LF": "UF",
    },
    "B": {
        "URB": "ULB",
        "UB": "LB",
        "ULB": "DLB",
        "LB": "DB",
        "DLB": "DRB",
        "DB": "RB",
        "DRB": "URB",
        "RB": "UB",
    }
}

_cubies = ["ULF", "ULB", "URB", "URF",
           "DLF", "DLB", "DRB", "DRF",
           "UF", "UL", "UR", "UB",
           "LF", "LB", "RB", "RF",
           "DF", "DL", "DB", "DR"]
