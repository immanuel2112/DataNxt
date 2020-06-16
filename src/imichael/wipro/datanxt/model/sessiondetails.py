from imichael.wipro.datanxt.utilities.applicationconstants import ApplicationConstants

class SessionDetails:
    def __init__(self, host, authenticationopt, user, password):
        self.host = host
        self.authenticationopt = authenticationopt
        self.user = user
        self.password = password
        self.appconstants = ApplicationConstants()
        self.log = None
        self.log_line_number = 0
        self.error_lines = {}
        self.install_status = None

    def getError_Lines(self):
        return self.error_lines

    def getHost(self):
        return self.host

    def getAuthenticationOpt(self):
        return self.authenticationopt

    def getUser(self):
        return self.user

    def getPassword(self):
        return self.password

    def isWindowsAuthenticated(self):
        if self.authenticationopt == self.appconstants.APPLICATION_AUTHENTICATION_WINDOWS:
            return True

    def getLog(self):
        return self.log

    def setLog(self, log):
        self.log = log

    def writeToLog(self, msg, error=False):
        self.log['state'] = 'normal'
        if self.log.index('end-1c') != '1.0':
            self.log.insert('end', '\n')
            self.setLog_Line_number()
        if error:
            self.log.insert('end', """Error:""")
            self.setLog_Line_number()
            self.error_lines[str(self.getLog_Line_number())] = self.getLog_Line_number()
            print("Line Number 1:" + str(self.getLog_Line_number()))
            self.log.insert('end', '\n')
            self.setLog_Line_number()
            self.error_lines[str(self.getLog_Line_number())] = self.getLog_Line_number()
            print("Line Number 2:" + str(self.getLog_Line_number()))
        self.log.insert('end', msg)
        self.setLog_Line_number()
        # print("Line number 3: "+str(self.getLog_Line_number()))
        self.log['state'] = 'disabled'

    def setLog_Line_number(self):
        self.log_line_number += 1

    def getLog_Line_number(self):
        return self.log_line_number

    def __str__(self):
        return '\n'.join(self.getHost()).join('\n').join(self.getAuthenticationOpt()).join('\n').join(self.getUser())\
            .join('\n').join(self.install_status).join('\n').join(self.getError_Lines())
