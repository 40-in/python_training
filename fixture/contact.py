from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if not wd.find_elements_by_name("maintable"):
            wd.find_element_by_link_text("home").click()

    def open_contact_adding_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_contact_adding_page()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd=self.app.wd
        self.open_contacts_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            cells = element.find_elements_by_tag_name("td")
            firstname = cells[2].text
            lastname = cells[1].text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return contacts
