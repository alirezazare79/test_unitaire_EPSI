from src.palindrome import Palindrome
from tests.utilities.LangueStub import LangueStub
from src.moment import Moment



class PalindromeBuilder:
    __langue = LangueStub()
    __moment = Moment.INCONNU


    def build(self):
        return Palindrome(self.__langue, self.__moment)

    def set_langue(self, langue):
        self.__langue = langue
        return self

    def set_moment(self, moment):
        self.__moment = moment
        return self