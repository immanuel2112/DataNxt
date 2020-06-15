from imichael.wipro.sapdmdq.utilities.applicationconstants import ApplicationConstants


def convert_resultset_to_list(resultset):
    result = []
    for record in resultset:
        for data in record:
            result.append(data)
    return result


def convert_table_result_to_tree(tree, resultset):
    appconstants = ApplicationConstants()
    header_columns = resultset[appconstants.TABLE_HEADER]
    print(header_columns)
    tree['columns'] = tuple(header_columns)
    for column in header_columns:
        tree.heading(column, text=column)

    data_values = resultset[appconstants.TABLE_DATA]
    for data in data_values:
        tree.insert("", "end", values=data[1:])
