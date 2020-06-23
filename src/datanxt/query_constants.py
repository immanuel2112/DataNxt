import textwrap

APPLICATION_SYSTEM_DATABASE_VALUE = "datanxt"
APPLICATION_SYSTEM_MASTER_DATABASE = "master"

EXECUTE_QUERY = textwrap.dedent(""" EXEC('{query}')""")
EXECUTE_QUERY_IN_DB = textwrap.dedent(""" USE [{DatabaseName}]; EXEC('{query}')""")

APPLICATION_DB_EXISTS_SQL = textwrap.dedent("""SELECT Name FROM sys.databases 
                                               WHERE Name = '{APPLICATION_SYSTEM_DATABASE}'""")

CREATE_DATABASE = textwrap.dedent("""CREATE DATABASE {DatabaseName};""")
DATABASE_COLLATE_PROPERTY = textwrap.dedent(
    """ ALTER DATABASE [{DatabaseName}] COLLATE SQL_Latin1_General_CP1_CS_AS """)
DATABASE_ENABLE_BROKER_PROPERTY = textwrap.dedent(""" ALTER DATABASE [{DatabaseName}] SET ENABLE_BROKER """)

GET_OBJECT_DATA = textwrap.dedent("""
                                    SELECT   * 
                                    FROM {DatabaseName}.dbo.{Object} 
                                    {WhereClause}
                                """)

GET_OBJECT_COLUMNS = textwrap.dedent("""
                                    SELECT {DatabaseName}.sys.columns.name 
                                    FROM {DatabaseName}.sys.objects 
                                            INNER JOIN {DatabaseName}.sys.columns 
                                            ON {DatabaseName}.sys.objects.object_id = {DatabaseName}.sys.columns.object_id 
                                    WHERE {DatabaseName}.sys.objects.name = '{Object}' 
                                    ORDER by {DatabaseName}.sys.columns.column_id ASC
                                """)