from imichael.wipro.datanxt.utilities.application_constants import ApplicationConstants

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

    appconstants = ApplicationConstants()
    displaycolumns=[]
    for col in tree["columns"]:
        print("%s"%col)
        if not any(word in "%s"%col for word in appconstants.EXCLUDE_FIELDS_LIST):
            # if not "%s"%col in self.appconstants.EXCLUDE_FIELDS_LIST:
            displaycolumns.append(col)
    tree["displaycolumns"]=displaycolumns