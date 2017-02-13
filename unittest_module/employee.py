import requests


class Employee:
    hike_rate = 1.3

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def hike_pay(self):
        self.pay = int(self.pay * self.hike_rate)

    def monthly_schedule(self, month):
        response = requests.get(
            f"http://company.com/{self.first_name}_{self.last_name}/{month}/"
        )
        if response.ok:
            return response.text
        else:
            return "Bad Response!"
