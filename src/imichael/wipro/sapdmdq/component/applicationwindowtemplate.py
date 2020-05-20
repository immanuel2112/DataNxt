from tkinter import messagebox, ttk, X, BOTH, Text

from imichael.wipro.sapdmdq.utilities.applicationconstants import ApplicationConstants


class ApplicationWindowTemplate(object):
    def __init__(self, master):
        self.master = master
        self.error = ""
        self.info = ""
        self.warning = ""
        self.headermessagelbl = ""
        self.sessiondetails = None
        self.appconstants = ApplicationConstants()

        #Styles
        style = ttk.Style()
        style.configure('Header.TFrame',
                        background=self.appconstants.APPLICATION_HEADER_FRAME_BGCOLOR)
        style.configure('Header.TLabel',
                        font=self.appconstants.APPLICATION_HEADER_LABEL_FONT,
                        foreground=self.appconstants.APPLICATION_HEADER_LABEL_FGCOLOR,
                        background=self.appconstants.APPLICATION_HEADER_LABEL_BGCOLOR)
        style.configure('Content.TFrame',
                        background=self.appconstants.APPLICATION_CONTENT_FRAME_BGCOLOR)
        style.configure('Content.TLabel',
                        font=self.appconstants.APPLICATION_CONTENT_LABEL_FONT,
                        foreground=self.appconstants.APPLICATION_CONTENT_LABEL_FGCOLOR,
                        background=self.appconstants.APPLICATION_CONTENT_LABEL_BGCOLOR)
        style.configure('Content.TRadiobutton',
                        foreground=self.appconstants.APPLICATION_CONTENT_LABEL_FGCOLOR,
                        background=self.appconstants.APPLICATION_CONTENT_LABEL_BGCOLOR)
        style.configure('ContentRTop.TFrame',
                        background=self.appconstants.APPLICATION_CONTENT_FRAME_BGCOLOR)

        # Define Frames
        self.header = ttk.Frame(self.master, style='Header.TFrame')
        self.content = ttk.Frame(self.master, style='Content.TFrame')
        self.contentleft = ttk.Frame(self.content, style='Content.TFrame')
        self.contentright = ttk.Frame(self.content)
        self.contentrighttop = ttk.Frame(self.contentright, height=20, style='ContentRTop.TFrame')
        self.install_frame = ttk.Frame(self.master, style='Content.TFrame')

        self.header.pack(fill=X)
        self.content.pack(fill=BOTH, expand=True)
        self.log = Text(self.install_frame, state='disabled')

    def show_header_message(self, text):
        # Build Header Frame
        self.headermessagelbl = ttk.Label(self.header, text=text, style='Header.TLabel')
        self.headermessagelbl.pack()
        # self.headermessagelbl.place(x=260,y=60)
        # self.header_image= ImageTk.PhotoImage(Image.open(self.appconstants.APPLICATION_WIPRO_LOGO))
        # self.header_image_lbl=Label(self.header, image=self.header_image)
        # self.header_image_lbl.place(x=450, y=5)

    def show_error(self):
        messagebox.showerror(self.appconstants.APPLICATION_MESSAGEBOX_TYPE_ERROR, self.error)

    def show_info(self):
        messagebox.showinfo(self.appconstants.APPLICATION_MESSAGEBOX_TYPE_INFO, self.info)

    def show_warning(self):
        messagebox.showwarning(self.appconstants.APPLICATION_MESSAGEBOX_TYPE_ERROR, self.warning)

    def reset_to_default(self):
        self.error = ""
        self.info = ""
        self.warning = ""

    def func_configuration(self):
        pass

    # adding a tag to a part of text specifying the indices
    def highlight_text(self, tag_name, lineno, start_char, end_char, bg_color=None, fg_color=None):
        log = self.sessiondetails.getLog()
        log['state'] = 'normal'
        log.tag_add(tag_name, f'{lineno}.{start_char}', f'{lineno}.{end_char}')
        log.tag_config(tag_name, background=bg_color, foreground=fg_color)
        log['state'] = 'disabled'
