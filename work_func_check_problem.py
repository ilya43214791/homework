
def import_mile_in_km(mile: float | int) -> float:
    mile_in_km = mile * 1.609
    if mile < 0:
        raise ValueError
    else:
        return mile_in_km