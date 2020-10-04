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

    pair_found = False

    for C in range(len(contacts)):
        for G in range(len(groups)):
            if contacts[C] not in orm.get_contacts_in_group(groups[G]):
                pair_found = True
                contact_id = contacts[C].id
                group_id = groups[G].id
                break
        if pair_found:
            break

    if not pair_found:
        app.group.create(Group(name="test"))
        groups = db.get_group_list()
        G = -1
        group_id = groups[G].id
        C = randrange(len(contacts))
        contact_id = contacts[C].id
        app.contact.open_contacts_page()

    app.contact.add_contact_to_group(contact_id, group_id)

    assert contacts[C] in orm.get_contacts_in_group(groups[G])