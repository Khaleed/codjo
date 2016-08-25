# class Human(object):
#     num_arms = 2
#     def __init__(self, value):
#         self.name = value
# khalid = Human("khalid")
# print(khalid.num_arms)

class Recurser(object):
    fav_lang = "Scala"
    @staticmethod
    def get_second_fav_lang():
        return "JS"
    def __init__(self, name):
        self.name = name

andy = Recurser("andy")
print(andy.get_second_fav_lang() == Recurser.get_second_fav_lang())
