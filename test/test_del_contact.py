from model.contact import Contact
from random import randrange
import time


def test_delete_random_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    id = old_contacts[index].id
    app.contact.delete_contact_by_id(id)
    time.sleep(2)
    new_contacts = db.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
