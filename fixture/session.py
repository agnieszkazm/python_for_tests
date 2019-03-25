class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, name, password):
        wd = self.app.wd
        self.app.open_website()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(name)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_loged_in():
            self.logout()

    def is_loged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_loged_in_as(self, name):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "("+name+")"

    def ensure_login(self, name, password):
        wd = self.app.wd
        if self.is_loged_in():
            if self.is_loged_in_as(name):
                return
            else:
                self.logout()
        self.login(name, password)

