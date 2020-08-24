# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(
        Contact(firstname="111", middlename="222", lastname="333", nickname="444", title="555",
                company="666", address="777", home="888", mobile="999", work="1010", fax="1111",
                email="1212", email2="1313", email3="1414", homepage="1515"))
    app.session.logout()