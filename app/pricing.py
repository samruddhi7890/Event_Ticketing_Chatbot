def calculate_price(base_price, demand_factor, group_size):

    dynamic_price = base_price * demand_factor

    if group_size >= 5:
        dynamic_price *= 0.9

    return round(dynamic_price * group_size, 2)
