def convertResultSetToList(resultset):
    result = []
    for record in resultset:
        for data in record:
            result.append(data)
            print(data)
    return result