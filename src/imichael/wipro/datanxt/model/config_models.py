class Page:
    def __init__(self, title, table, child_table=None, parent_child=None, events=None):
        self.self = self
        self.title = title
        self.events = events
        self.table = table
        self.parent_child = parent_child
        self.child_table = child_table


class Table:
    def __init__(self, name):
        self.name = name
        self.fields = None
        self.data = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_fields(self):
        return self.fields

    def set_fields(self, fields):
        self.fields = fields

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


class BaseObject:

    def __init__(self, id):
        self.id = id
        self.added_on = None
        self.added_by = None
        self.changed_on = None
        self.changed_by = None
        self.fields = None

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_added_on(self):
        return self.added_on

    def set_added_on(self, added_on):
        self.added_on = added_on

    def get_added_by(self):
        return self.added_by

    def set_added_by(self, added_by):
        self.added_by = added_by

    def get_changed_on(self):
        return self.changed_on

    def set_changed_on(self, changed_on):
        self.changed_on = changed_on

    def get_changed_by(self):
        return self.changed_by

    def set_changed_by(self, changed_by):
        self.changed_by = changed_by

    def get_fields(self):
        return self.fields

    def set_fields(self, fields):
        self.fields = fields

    def __str__(self) -> str:
        return super().__str__()


class SysModel(BaseObject):

    def __init__(self, id):
        super().__init__(id)
        self.sys_model = None
        self.sys_model_description = None

    def get_sys_model(self):
        return self.sys_model

    def set_sys_model(self, sys_model):
        self.id = sys_model

    def get_sys_model_description(self):
        return self.sys_model_description

    def set_sys_model_description(self, sys_model_description):
        self.sys_model_description = sys_model_description
