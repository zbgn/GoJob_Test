def closest_to_zero(lst = None):
    return min(lst, key=abs) if lst is not None and len(lst) > 0 else 0