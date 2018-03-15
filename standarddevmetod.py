
D = {'Veronica': 24.70, 'Caroline': 22.47, 'Tommy': 19.85, 'Stefanie': 15.68, 'Lydia': 14.31}


def standard_dev_calc (dictionary_to_analyze):
    import statistics
    numbers_to_deviate = list(dictionary_to_analyze.values())
    dict_standard_dev = statistics.stdev((numbers_to_deviate))
    return dict_standard_dev

print(standard_dev_calc(D))
