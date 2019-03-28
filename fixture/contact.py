class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_website()
        wd.find_element_by_link_text("add new").click()
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
        wd.find_element_by_name("submit").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first(self):
        wd = self.app.wd
        self.app.open_website()
        wd.find_element_by_xpath('//tr[2]/td[8]/a').click()
        wd.find_element_by_xpath("//*[@value='Delete']").click()

    def modify(self, contact):
        wd = self.app.wd
        self.app.open_website()
        wd.find_element_by_xpath('//tr[2]/td[8]/a').click()
        self.change_field_value("firstname", contact.first_name)
        wd.find_element_by_xpath("//*[@value='Update']").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

