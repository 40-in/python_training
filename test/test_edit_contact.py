# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="111", middlename="222", lastname="333", nickname="444", title="555",
                      company="666", address="777", home="888", mobile="999", work="1010", fax="1111",
                      email="1212", email2="1313", email3="1414", homepage="1515")
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert old_contacts == new_contacts
