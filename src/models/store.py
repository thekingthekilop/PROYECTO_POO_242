class Store:
    def __init__(self, store_id, name, address):
        self.store_id = store_id
        self.name = name
        self.address = address
        self.sections = []

    def add_section(self, section):
        self.sections.append(section)

    def remove_section(self, section_id):
        self.sections = [sec for sec in self.sections if sec.section_id != section_id]

    def find_section_by_name(self, name):
        return next((sec for sec in self.sections if sec.name == name), None)

    def find_section_by_id(self, section_id):
        return next((sec for sec in self.sections if sec.section_id == section_id), None)

    def list_sections(self):
        return [sec.name for sec in self.sections]
