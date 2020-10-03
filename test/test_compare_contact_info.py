import re
from model.contact import Contact

def test_contact_info_on_home_page(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for number in range(len(db.get_contact_list())):
        assert contacts_from_home_page[number].firstname == contacts_from_db[number].firstname
        assert contacts_from_home_page[number].lastname == contacts_from_db[number].lastname
        assert contacts_from_home_page[number].address == contacts_from_db[number].address
        assert contacts_from_home_page[number].all_phones_from_home_page == merge_phones_like_on_homepage(contacts_from_db[number])
        assert contacts_from_home_page[number].all_emails_from_home_page == merge_emails_like_on_homepage(contacts_from_db[number])

# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.home == contact_from_edit_page.home
#     assert contact_from_view_page.work == contact_from_edit_page.work
#     assert contact_from_view_page.mobile == contact_from_edit_page.mobile

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work]))))

def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))