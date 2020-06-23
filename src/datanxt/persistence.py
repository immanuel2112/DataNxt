import pypyodbc as pyodbc

from datanxt.app_models import Table
from datanxt import query_constants, application_utility
from datanxt.application_constants import ApplicationConstants


class Connection:
    def __init__(self, session_details):
        self.session_details = session_details
        self.build_connection_string()
        self.app_constants = ApplicationConstants()
        self.connection = None

    def build_connection_string(self) -> None:
        if len(self.session_details.getUser()) == 0:
            self.connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server=' + self.session_details.getHost() + ';Database=master;Trusted_Connection=yes;'
        else:
            self.connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server=' + self.session_details.getHost() + ';Database=master;UID=' + self.session_details.getUser() + ';PWD=' + self.session_details.getPassword() + ';'

    def test_connection(self) -> str:
        error_message = ""
        try:
            self.connection = pyodbc.connect(self.connection_string)
            self.connection.close()
        except Exception as error:
            error_message = str(error)
        return error_message

    def check_application_installation_status(self) -> int:
        return_value = 0
        self.connection = pyodbc.connect(self.connection_string)
        cursor = self.connection.cursor()
        row = cursor.execute(
            query_constants.APPLICATION_DB_EXISTS_SQL.format(
                APPLICATION_SYSTEM_DATABASE=query_constants.APPLICATION_SYSTEM_DATABASE_VALUE)).fetchone()
        if row:
            print("db_name: " + str(row[0]))
            return_value = 1
        cursor.close()
        self.connection.close()
        return return_value

    def install(self) -> None:
        try:
            # Step 1: Create sdvSystemMaster database
            self.session_details.writeToLog(
                msg="Start: Create application database: " + query_constants.APPLICATION_SYSTEM_DATABASE_VALUE)
            self.create_database()
            self.session_details.writeToLog(msg="Stop: Application database created successfully.")
            # Step 2: Create sdv System Master tables
            # self.sessiondetails.writeToLog("Create application tables.")
            # self.sessiondetails.writeToLog("Application tables created successfully.")
            # Step 2: Insert sdv System Master tables data
            # self.sessiondetails.writeToLogm,writeToLogm("Populate application default data.")
            # self.sessiondetails.writeToLog("Application default data populated successfully.")
        except Exception as error:
            error_message = str(error)
            self.session_details.writeToLog(msg=error_message, error=True)

    def create_database(self) -> None:
        try:
            connection = pyodbc.connect(self.connection_string, autocommit=True)
            cursor = connection.cursor()
            # 1. Creating database
            self.session_details.writeToLog(msg="1. Creating database")
            query = query_constants.CREATE_DATABASE.format(DatabaseName=query_constants.APPLICATION_SYSTEM_DATABASE_VALUE)
            sql = query_constants.EXECUTE_QUERY_IN_DB.format(
                DatabaseName=query_constants.APPLICATION_SYSTEM_MASTER_DATABASE, query=query)
            print("sql: " + sql)
            cursor.execute(sql)
            # 2. Set Collation property for the database
            self.session_details.writeToLog(msg="2. Setting database collation property")
            query = query_constants.DATABASE_COLLATE_PROPERTY.format(
                DatabaseName=query_constants.APPLICATION_SYSTEM_DATABASE_VALUE)
            sql = query_constants.EXECUTE_QUERY_IN_DB.format(
                DatabaseName=query_constants.APPLICATION_SYSTEM_MASTER_DATABASE, query=query)
            print("sql: " + sql)
            cursor.execute(sql)
            # 3. Enable broker property for the database
            self.session_details.writeToLog(msg="3. Setting database Enable broker property")
            query = query_constants.DATABASE_ENABLE_BROKER_PROPERTY.format(
                DatabaseName=query_constants.APPLICATION_SYSTEM_DATABASE_VALUE)
            sql = query_constants.EXECUTE_QUERY_IN_DB.format(
                DatabaseName=query_constants.APPLICATION_SYSTEM_MASTER_DATABASE, query=query)
            print("sql: " + sql)
            cursor.execute(sql)
            connection.close()
        except Exception as error:
            error_message = str(error)
            self.session_details.writeToLog(msg=error_message, error=True)

    def get_table(self, page) -> Table:
        name = page.table
        table = Table(name)
        self.connection = pyodbc.connect(self.connection_string)
        cursor = self.connection.cursor()

        query = query_constants.GET_OBJECT_COLUMNS.format(
            DatabaseName=query_constants.APPLICATION_SYSTEM_DATABASE_VALUE, Object=name)
        header_row = cursor.execute(query).fetchall()
        formatted_header_row = application_utility.convert_resultset_to_list(header_row)
        table.set_fields(formatted_header_row)

        where_clause = ""
        if page.filter_field is not None:
            where_clause = "WHERE " + page.filter_field + " = '" + page.filter_field_value + "'"

        query = query_constants.GET_OBJECT_DATA.format(
            DatabaseName=query_constants.APPLICATION_SYSTEM_DATABASE_VALUE, Object=name,
            WhereClause=where_clause)

        print(query)
        data_row = cursor.execute(query).fetchall()
        table.set_data(data_row)

        if data_row is not None:
            table.set_record_count(len(data_row))

        cursor.close()
        self.connection.close()
        return table
