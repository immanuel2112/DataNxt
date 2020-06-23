class Page:
    def __init__(self, title, table,
                 child_table=None, parent_child=None, events=None,
                 filter_field=None, filter_field_value=None):
        self.self = self
        self.title = title
        self.events = events
        self.table = table
        self.parent_child = parent_child
        self.child_table = child_table
        self.filter_field = filter_field
        self.filter_field_value = filter_field_value


class Table:
    def __init__(self, name):
        self.name = name
        self.fields = None
        self.data = None
        self.record_count = 0

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
        self.data = []
        for records in data:
            new_list = []
            for record in records:
                if (record is not None) and (str(record).startswith("b'")):
                    record1 = record.replace("b'","").replace("'","")
                    new_list.append(record1)
                else:
                    new_list.append(record)
            self.data.append(new_list)

    def get_record_count(self):
        return self.record_count

    def set_record_count(self, record_count):
        self.record_count = record_count