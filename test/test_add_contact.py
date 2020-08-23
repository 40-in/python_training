# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(
        Contact(firstname="fsdafdsfds", middlename="sdfsdfds", lastname="dfsdfdsf", nickname="sfsfsd", title="sdfsfwf",
                company="sfsfs", address="xvxvxv", home="xvvx", mobile="sfdfdf", work="sfdsfdsf", fax="sfsfsf",
                email="sfsfsfsf", email2="sfsffvxv", email3="xvxvxv", homepage="cbcbgg"))
    app.session.logout()
