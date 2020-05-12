class ApplicationConstants:
    def __init__(self):
        self.APPLICATION_TITLE = "SAP Data Migration - Data Quality Assessment - Wipro Limited"
        self.APPLICATION_WIPRO_LOGO = "..\..\..\icons\wiprologo.jpg"
        self.APPLICATION_LOGIN_GEOMETRY = "660x400+450+200"
        self.APPLICATION_HEADER_FRAME_BGCOLOR = "#1A99A2"
        self.APPLICATION_CONTENT_FRAME_BGCOLOR = "#47B6BE"
        self.APPLICATION_HEADER_FRAME_LABEL = "SAP Data Migration - Data Quality Assessment"
        self.APPLICATION_HEADER_LABEL_FONT = "arial 15 bold"
        self.APPLICATION_HEADER_LABEL_FGCOLOR = "#FFFFFF"
        self.APPLICATION_HEADER_LABEL_BGCOLOR = "#1A99A2"
        self.APPLICATION_CONTENT_LABEL_FONT = "arial 12"
        self.APPLICATION_CONTENT_LABEL_FGCOLOR = "#FFFFFF"
        self.APPLICATION_CONTENT_LABEL_BGCOLOR = "#47B6BE"
        self.APPLICATION_ERROR_FONT = "arial 10"
        self.APPLICATION_ERROR_FGCOLOR = "#F70404"
        self.APPLICATION_ERROR_BGCOLOR = "#47B6BE"
        self.APPLICATION_AUTHENTICATION_SQL = 'SQL Server Authentication'
        self.APPLICATION_AUTHENTICATION_WINDOWS = 'Windows Authentication'
        self.APPLICATION_AUTHENTICATION_CHOICES = {self.APPLICATION_AUTHENTICATION_SQL,
                                                   self.APPLICATION_AUTHENTICATION_WINDOWS}
        self.APPLICATION_LABEL_WIDTH = 15
        self.APPLICATION_LABEL_ENTRY_BUTTON_WIDTH = self.APPLICATION_LABEL_WIDTH * 2
        self.APPLICATION_BUTTON_WIDTH = (self.APPLICATION_LABEL_WIDTH * 2) - 5
        self.APPLICATION_BUTTON_FGCOLOR = "#FFFFFF"
        self.APPLICATION_BUTTON_BGCOLOR = "#136A71"
        self.APPLICATION_BUTTON_FONT_UNDERLINE = "arial 10 underline"
        self.APPLICATION_HOME_GEOMETRY = "700x600+450+100"
        self.APPLICATION_MESSAGEBOX_TYPE_ERROR = "Error"
        self.APPLICATION_MESSAGEBOX_TYPE_INFO = "Info"
        self.APPLICATION_MESSAGEBOX_TYPE_WARNING = "Warning"
        self.APPLICATION_HOME_HEADER_FRAME_LABEL = "SAP Data Migration - Data Quality Assessment"
        self.APPLICATION_INSTALL_HEADER_FRAME_LABEL = "SAP Data Migration - Data Quality Assessment"

        self.HOME_TAB_PROJECTS = "Projects"
        self.HOME_TAB_NEWPROJECT = "New Project"
        self.HOME_TAB_CONFIGURATION = "Configuration"
        self.HOME_TAB_ABOUT = "About"
