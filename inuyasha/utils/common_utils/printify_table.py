from prettytable import PrettyTable

from inuyasha.utils.log_utils.core import log


def printify_table(data, align='c'):
    x = PrettyTable()
    x.field_names = list(data.keys())
    x.align = align
    x.add_row(list(data.values()))
    log.info('\n' + str(x))
