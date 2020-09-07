# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_contact_by_index(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="111", middlename="222", lastname="333", nickname="444", title="555",
                      company="666", address="777", home="888", mobile="999", work="1010", fax="1111",
                      email="1212", email2="1313", email3="1414", homepage="1515")
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert old_contacts == new_contacts
