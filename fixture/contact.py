from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_website()
        wd.find_element_by_link_text("add new").click()
        self.fill_form(contact)
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

    def fill_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.midle_name)
        self.change_field_value("lastname", contact.surname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("home", contact.home_no)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.mail)
        self.change_field_value("homepage", contact.homepage)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
            self.contact_cache = None

    def delete_random(self, index):
        wd = self.app.wd
        self.app.open_website()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        self.contact_cache = None

    def delete_first(self):
        self.delete_random(0)

    def modify(self, contact):
        self.modify_random(contact, 0)

    def modify_random(self, index, contact):
        wd = self.app.wd
        self.app.open_website()
        self.select_contact_by_index(index)
        # self.change_field_value("firstname", contact.first_name)
        self.fill_form(contact)
        wd.find_element_by_xpath("//*[@value='Update']").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_name("selected[]"):
                id = element.get_attribute("value")
                name = element.get_attribute("title")[8:-1].split()
                self.contact_cache.append(Contact(first_name=name[0], surmane=name[1], id=id))
        return list(self.contact_cache)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath('//tr[2]/td[8]/a')[index].click()
