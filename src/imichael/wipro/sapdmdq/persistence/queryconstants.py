import textwrap

APPLICATION_SYSTEM_DATABASE_VALUE = "sapdmdq"
APPLICATION_SYSTEM_MASTER_DATABASE = "master"

EXECUTE_QUERY = textwrap.dedent(""" EXEC('{query}')""")
EXECUTE_QUERY_IN_DB = textwrap.dedent(""" USE [{DatabaseName}]; EXEC('{query}')""")

APPLICATION_DB_EXISTS_SQL = textwrap.dedent("""SELECT Name FROM sys.databases 
                                               WHERE Name = '{APPLICATION_SYSTEM_DATABASE}'""")

CREATE_DATABASE = textwrap.dedent("""CREATE DATABASE {DatabaseName};""")
DATABASE_COLLATE_PROPERTY = textwrap.dedent(
    """ ALTER DATABASE [{DatabaseName}] COLLATE SQL_Latin1_General_CP1_CS_AS """)
DATABASE_ENABLE_BROKER_PROPERTY = textwrap.dedent(""" ALTER DATABASE [{DatabaseName}] SET ENABLE_BROKER """)
