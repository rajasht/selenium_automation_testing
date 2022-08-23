# unit test case
import unittest
import allure

from Maoatv import ATV
from Maocommercialtruck import MAOcommercial
from Maocycle import CycleMao
from Maoequipment import maoequipment
from Maorv import rvmao
from Maopwc import PwcMao
from Maosnowmobile import snowmobile

class TestStringMethods(unittest.TestCase):
    # test function
    def test_positive(self):
        testValue = True
        # error message in case if test case got failed
        message = "Test value is not true."
        # assertTrue() to check true of test value
        self.assertTrue(testValue, message)

    @allure.story('User can buy their selected vehicle and also they can trade it with their old vehicle.')
    @allure.description('User can buy their selected vehicle and also they can trade it with their old vehicle.')
    @allure.step('1. Fill all the required details.')
    @allure.step('2. Select trade-in if required')
    @allure.step('3. Select payment and delivery option')
    
    
    def test_MaoAtv(self):
        objeMaoatv = ATV()
        objeMaoatv.execute()
        self.assertTrue('Hi', False)


    def test_MaoComTruck(self):
        objeMaocomtruck = MAOcommercial()
        objeMaocomtruck.execute()
        self.assertTrue('Hi', False)


    def test_Maocycle(self):
        objeMaocycle = CycleMao()
        objeMaocycle.execute()
        self.assertTrue('Hi', False)


    def test_MaoEquipment(self):
        objeMaoequipment = maoequipment()
        objeMaoequipment.execute()
        self.assertTrue('Hi', False)


    def test_MaoRv(self):
        objeMaorv = rvmao()
        objeMaorv.execute()
        self.assertTrue('Hi', False)


    def test_MaoPwc(self):
        objeMaopwc = PwcMao()
        objeMaopwc.execute()
        self.assertTrue('Hi', False)


    def test_MaoSnowmobile(self):
        objeMaosnowmobile = snowmobile()
        objeMaosnowmobile.execute()
        self.assertTrue('Hi', False)


if __name__ == '__main__':
    unittest.main()