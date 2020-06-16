def convert_resultset_to_list(resultset) -> list:
    result = []
    for record in resultset:
        for data in record:
            result.append(data)
    return result


def convert_table_result_to_tree(tree, table) -> None:
    header_columns = table.get_fields()
    print(header_columns)
    tree['columns'] = tuple(header_columns)

    for column in header_columns:
        tree.heading(column, text=column)

    data_values = table.get_data()
    for data in data_values:
        tree.insert("", "end", text=data[0], values=data)