import sys


class Contact:

    def __init__(self, first_name=None, midle_name=None, surmane=None, nickname=None, home_no=None, mobile=None, work=None, fax=None, mail=None, homepage=None, id=None):
        self.first_name = first_name
        self.midle_name = midle_name
        self.surname = surmane
        self.nickname = nickname
        self.home_no = home_no
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.mail = mail
        self.homepage = homepage
        self.id = id

    def __repr__(self):
        return '%s: %s %$' % (self.id, self.first_name, self.surname)

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) and self.first_name == other.first_name and self.surname == other.surname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return sys.maxsize
