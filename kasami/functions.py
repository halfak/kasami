from math import exp, log


def sum_log_product(iterable):
    log_sum = sum(log(v) for v in iterable)
    return exp(log_sum)
