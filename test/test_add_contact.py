# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="fsdafdsfds", middlename="sdfsdfds", lastname="dfsdfdsf", nickname="sfsfsd",
                      title="sdfsfwf", company="sfsfs", address="xvxvxv", home="xvvx", mobile="sfdfdf", work="sfdsfdsf",
                      fax="sfsfsf", email="sfsfsfsf", email2="sfsffvxv", email3="xvxvxv", homepage="cbcbgg")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert old_contacts == new_contacts
