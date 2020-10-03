from model.group import Group
from model.contact import Contact
from random import randrange
from fixture.orm import ORMFixture

orm = ORMFixture(host="localhost", name="addressbook", user="root", password="")

def test_add_contact_to_group(app, db):

    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))

    contacts = db.get_contact_list()
    groups = db.get_group_list()

    while True:
        contact_index = randrange(len(contacts))
        group_index = randrange(len(groups))
        contact_id = contacts[contact_index].id
        group_id = groups[group_index].id
        if contacts[contact_index] not in orm.get_contacts_in_group(groups[group_index]):
            break

    app.contact.add_contact_to_group(contact_id, group_id)

    assert contacts[contact_index] in orm.get_contacts_in_group(groups[group_index])