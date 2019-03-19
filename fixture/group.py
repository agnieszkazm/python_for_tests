class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        # open group page
        wd.find_element_by_link_text("groups").click()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill out group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def delete_first(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath('//input[@name = "delete"]').click()
        self.return_to_group_page()

    def modify(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//*[@value='Edit group']").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_xpath("//*[@value='Update']").click()
        self.return_to_group_page()


    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
