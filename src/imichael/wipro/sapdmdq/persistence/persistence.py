import pypyodbc as pyodbc

from imichael.wipro.sapdmdq.persistence import queryconstants
from imichael.wipro.sapdmdq.utilities import applicationutility
from imichael.wipro.sapdmdq.utilities.applicationconstants import ApplicationConstants


class Connection:
    def __init__(self, sessiondetails):
        self.sessiondetails = sessiondetails
        self.buildconnectionstring()
        self.appconstants = ApplicationConstants()

    def buildconnectionstring(self):
        if len(self.sessiondetails.getUser()) == 0:
            self.connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server=' + self.sessiondetails.getHost() + ';Database=master;Trusted_Connection=yes;'
        else:
            self.connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server=' + self.sessiondetails.getHost() + ';Database=master;UID=' + self.sessiondetails.getUser() + ';PWD=' + self.sessiondetails.getPassword() + ';'

    def test_connection(self):
        errormessage = ""
        try:
            self.connection = pyodbc.connect(self.connection_string)
            self.connection.close()
        except (Exception) as error:
            errormessage = str(error)
        return errormessage

    def check_application_installation_Status(self):
        returnvalue = 0
        self.connection = pyodbc.connect(self.connection_string)
        cursor = self.connection.cursor()
        row = cursor.execute(
            queryconstants.APPLICATION_DB_EXISTS_SQL.format(
                APPLICATION_SYSTEM_DATABASE=queryconstants.APPLICATION_SYSTEM_DATABASE_VALUE)).fetchone()
        if row:
            print("db_name: " + str(row[0]))
            returnvalue = 1
        cursor.close()
        self.connection.close()
        return returnvalue

    def install(self):
        try:
            # Step 1: Create sdvSystemMaster database
            self.sessiondetails.writeToLog(
                msg="Start: Create application database: " + queryconstants.APPLICATION_SYSTEM_DATABASE_VALUE)
            self.create_database()
            self.sessiondetails.writeToLog(msg="Stop: Application database created successfully.")
            # Step 2: Create sdv System Master tables
            # self.sessiondetails.writeToLog("Create application tables.")
            # self.sessiondetails.writeToLog("Application tables created successfully.")
            # Step 2: Insert sdv System Master tables data
            # self.sessiondetails.writeToLogm,writeToLogm("Populate application default data.")
            # self.sessiondetails.writeToLog("Application default data populated successfully.")
        except (Exception) as error:
            errormessage = str(error)
            self.sessiondetails.writeToLog(msg=errormessage, error=True)

    def create_database(self):
        try:
            connection = pyodbc.connect(self.connection_string, autocommit=True)
            cursor = connection.cursor()
            # 1. Creating database
            self.sessiondetails.writeToLog(msg="1. Creating database")
            query = queryconstants.CREATE_DATABASE.format(DatabaseName=queryconstants.APPLICATION_SYSTEM_DATABASE_VALUE)
            SQL = queryconstants.EXECUTE_QUERY_IN_DB.format(
                DatabaseName=queryconstants.APPLICATION_SYSTEM_MASTER_DATABASE, query=query)
            print("SQL: " + SQL)
            cursor.execute(SQL)
            # 2. Set Collation property for the database
            self.sessiondetails.writeToLog(msg="2. Setting database collation property")
            query = queryconstants.DATABASE_COLLATE_PROPERTY.format(
                DatabaseName=queryconstants.APPLICATION_SYSTEM_DATABASE_VALUE)
            SQL = queryconstants.EXECUTE_QUERY_IN_DB.format(
                DatabaseName=queryconstants.APPLICATION_SYSTEM_MASTER_DATABASE, query=query)
            print("SQL: " + SQL)
            cursor.execute(SQL)
            # 3. Enable broker property for the database
            self.sessiondetails.writeToLog(msg="3. Setting database Enable broker property")
            query = queryconstants.DATABASE_ENABLE_BROKER_PROPERTY.format(
                DatabaseName=queryconstants.APPLICATION_SYSTEM_DATABASE_VALUE)
            SQL = queryconstants.EXECUTE_QUERY_IN_DB.format(
                DatabaseName=queryconstants.APPLICATION_SYSTEM_MASTER_DATABASE, query=query)
            print("SQL: " + SQL)
            cursor.execute(SQL)
            connection.close()
        except (Exception) as error:
            errormessage = str(error)
            self.sessiondetails.writeToLog(msg=errormessage, error=True)

    def get_sys_models(self):
        returnvalue = {}
        self.connection = pyodbc.connect(self.connection_string)
        cursor = self.connection.cursor()

        query = queryconstants.GET_SYS_MODEL_VIEW_COLUMNS.format(
            DatabaseName=queryconstants.APPLICATION_SYSTEM_DATABASE_VALUE, Object=queryconstants.CONFIGURATION_SYS_MODEL_VIEW)
        header_row = cursor.execute(query).fetchall()
        formatted_header_row = applicationutility.convert_resultset_to_list(header_row)
        returnvalue[self.appconstants.TABLE_HEADER] = formatted_header_row

        query = queryconstants.GET_SYS_MODEL.format(
            DatabaseName=queryconstants.APPLICATION_SYSTEM_DATABASE_VALUE, Object=queryconstants.CONFIGURATION_SYS_MODEL_VIEW)
        data_row = cursor.execute(query).fetchall()
        returnvalue[self.appconstants.TABLE_DATA] = data_row

        cursor.close()
        self.connection.close()
        return returnvalue