from src.data_object import DataObject


class Contact(DataObject):

    def __init__(self, model):
        super().__init__(model, 'get_contact_by_id.sql', 'get_contact.sql', 'add_contact.sql')

