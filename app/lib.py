def calculate_bonuses(purchase_sum, purchases_total):

    """
    >>> calculate_bonuses(100, 1)
    0

    >>> calculate_bonuses(1_000, 0)
    50

    >>> calculate_bonuses(1_000, 1)
    50

    >>> calculate_bonuses(2_000, 15_000)
    140

    >>> calculate_bonuses(3_300.50, 150_000)
    300

    >>> calculate_bonuses(30_000, 1_500)
    2100

    >>> calculate_bonuses(5_000, 145_000)
    500
    """

    bonus_cost = 1_000

    if purchase_sum < bonus_cost:
        return 0

    purchases_total += purchase_sum

    if purchases_total < 15_000:
        bonus_level = 50
    elif 15_000 <= purchases_total < 150_000:
        bonus_level = 70
    else:
        bonus_level = 100

    result = int(purchase_sum // bonus_cost) * bonus_level
    return result
