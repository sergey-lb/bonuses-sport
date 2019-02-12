def calculate_bonuses(purchase_sum, purchases_total):

    """
    >>> calculate_bonuses(1000, 0)
    0

    >>> calculate_bonuses(100, 1)
    0

    >>> calculate_bonuses(1000, 1)
    50

    >>> calculate_bonuses(2000, 15_000)
    140

    >>> calculate_bonuses(3300.50, 150_000)
    300
    """

    if purchases_total == 0:
        return 0

    if purchases_total < 15_000:
        bonus_level = 50
    elif 15_000 <= purchases_total < 150_000:
        bonus_level = 70
    else:
        bonus_level = 100

    bonus_cost = 1000

    result = int(purchase_sum // bonus_cost) * bonus_level
    return result
