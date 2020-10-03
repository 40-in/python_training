from model.contact import Contact
from random import randrange


def test_edit_random_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    id=old_contacts[index].id
    contact = Contact(id=id, firstname="111", middlename="222", lastname="333", nickname="444",
                      title="555", company="666", address="777", home="888", mobile="999", work="1010", fax="1111",
                      email="1212", email2="1313", email3="1414", homepage="1515")
    app.contact.edit_contact_by_id(id, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
