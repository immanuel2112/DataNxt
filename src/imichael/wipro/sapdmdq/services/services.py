from imichael.wipro.sapdmdq.persistence.persistence import Connection

def test_connection(sessiondetails):
    errormessage = ""
    connection = Connection(sessiondetails)
    errormessage = connection.test_connection()
    return errormessage


def check_application_installation_Status(sessiondetails):
    connection = Connection(sessiondetails)
    appdbexists = connection.check_application_installation_Status()
    print("appdbexists: " + str(appdbexists))
    return appdbexists


def install(sessiondetails):
    connection = Connection(sessiondetails)
    connection.install()

def get_sys_models(sessiondetails):
    connection = Connection(sessiondetails)
    sys_models = connection.get_sys_models()
    print("sys_models: " + str(sys_models))
    return sys_models
