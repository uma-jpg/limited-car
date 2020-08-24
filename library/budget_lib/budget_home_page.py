from library.BrowserInitialize.initialize_browser import InitializeBrowser
from library.budget_lib.budget_variable import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import logging
import datetime





class BUDGET(InitializeBrowser):
    def __init__(self):
        super(BUDGET, self).__init__()
        self.url = None

    def verify_launch_pahe(self):
        pass

    def select_location(self,location):
        """
        Method to select location from Budget Page
        :param location: Location to be selected
        :return:
        """

        try:
            WebDriverWait(self.driver,30
                                        ).until(EC.visibility_of_element_located(By.XPATH(WEBELEMENT_INPUT_LOCATION)))
            self.driver.find_element_by_xpath(WEBELEMENT_INPUT_LOCATION).send_keys(location)
            location_element = WebDriverWait(self.driver,30
                                            ).until(EC.visibility_of_element_located(By.XPATH(WEBELEMENT_LOCATION_SUGGESTIONS)))
            location_element.click()
            location_value = self.driver.find_element_by_xpath(WEBELEMENT_INPUT_LOCATION).text
            return location_value
        except Exception:
            logging.error("issue in selecting the location")
            return False

    def selct_pick_up_date_fpr_journey(self):
        """
        Method to select pickupdate from budget page
        :param date:
        :return:
        """
        try:
            WebDriverWait(self.driver, 30
                          ).until(EC.visibility_of_element_located(By.XPATH(INPUT_DATE)))
            self.driver.find_element_by_xpath(INPUT_DATE).click()
            WebDriverWait(self.driver, 30
                          ).until(EC.visibility_of_element_located(By.XPATH(WEBELEMENt_INPUT_CALENDER_WIDGET)))
            current_date = datetime.date.today()
            pick_up_date = (current_date+ datetime.timedelta(days = 7)).strftime("%d %B %Y")
            date = pick_up_date.split(" ")[0]
            month = pick_up_date.split(" ")[1]
            year =  pick_up_date.split(" ")[2]
            month_year = month+year
            self.driver.find_element_by_xpath(WEBELEMENT_MONTH_DROPDOWN.format(month_year)).click()
            calendar_rows = self.driver.find_elements_by_xpath(WEBELEMET_CALENDAR_ROWS)
            for row in calendar_rows:
                calendar_columns = self.driver.find_elements_by_xpath(row.find_elements_by_xpath("./td/a"))
                for col in calendar_columns:
                    col_value = col.text
                    if col_value == date:
                        col.click()
            return pick_up_date
        except Exception as err:
            logging.error("Issue in selecting pickup date")


    def select_return_date_for_journey(self,pick_up_date):
        try:
            pick_up_date = pick_up_date.strptime("%d %B %Y")
            return_date = (pick_up_date+datetime.timedelta(days = 7)).strftime("%d %B %Y")
            date = pick_up_date.split(" ")[0]
            month = pick_up_date.split(" ")[1]
            year = pick_up_date.split(" ")[2]
            month_year = month + year
            WebDriverWait(self.driver, 30
                          ).until(EC.visibility_of_element_located(By.XPATH(INPUT_DATE)))
            self.driver.find_element_by_xpath(INPUT_DATE).click()
            WebDriverWait(self.driver, 30
                          ).until(EC.visibility_of_element_located(By.XPATH(WEBELEMENt_INPUT_CALENDER_WIDGET)))
            self.driver.find_element_by_xpath(WEBELEMENT_MONTH_DROPDOWN.format(month_year)).click()
            calendar_rows = self.driver.find_elements_by_xpath(WEBELEMET_CALENDAR_ROWS)
            for row in calendar_rows:
                calendar_columns = self.driver.find_elements_by_xpath(row.find_elements_by_xpath("./td/a"))
                for col in calendar_columns:
                    col_value = col.text
                    if col_value == date:
                        col.click()
            return return_date
        except Exception as err:
            logging.error("issue in clicking return date")

    def select_car_type(self,car_type):
        """
        Method to select a car type based on the input
        :return:
        """
        try:
            temp_dict = {}
            price_list = []
            lowest_price_vehicle_key= 0
            self.driver.find_element_by_xpath(WEB_ELEMENt_VEHICLE_LIST_ARROW).click()
            self.driver.implicitly_wait(40)
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(By.XPATH(SELECT_VEHICLE.format(car_type))))
            self.driver.find_element_by_xpath(SELECT_VEHICLE).click()
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(By.XPATH(LIST_FILTERED_SUV_VEHICLES_ONLY)))
            filtered_vehicles = self.driver.find_elements_by_xpath(LIST_FILTERED_SUV_VEHICLES_ONLY)
            for vehilcle in filtered_vehicles:
                i =1
                seat_Numbers = filtered_vehicles.find_element_by_xpath(WEB_ELEMENT_FOUR_DOORS_LIST)
                DOOR_NUMBERS = filtered_vehicles.find_element_by_xpath(WEB_ELEMENT_FOUR_DOORS_LIST)
                PRICE = filtered_vehicles.find_element_by_xpath(PRICE_TEXT)
                temp_dict.update({i:PRICE})
                price_list.append(PRICE)
                i =i+1
            min_price = min(price_list)
            for key in temp_dict.keys():
                if temp_dict[key]== min_price:
                    lowest_price_vehicle_key= key
            selected_vehicle_name = filtered_vehicles[lowest_price_vehicle_key].find_element_by_xpath(SELECTED_VEHICLE_NAME).text
            select_vehicle = filtered_vehicles[lowest_price_vehicle_key].find_element_by_xpath(SELECT_LOWEST_BUTTON).click()

            return selected_vehicle_name
        except Exception as err:
            logging.error("Issue in selecting the lowest price vehicle")
            return False

    def validate_details_rental_options_page(self, start_location, end_location,vehicle_name):
        """

        :param start_location:
        :param send_location:
        :param vehicle_name:
        :return:
        """

        try:
            start_location_match = False
            return_location_match= False
            vehicle_name_match= False
            if (start_location == self.driver.find_element_by_xpath(WEBELEMENt_PICKUP_LOCATION).text) and \
                    (end_location == self.driver.find_element_by_xpath(WEBELEMENT_DROP_LOCATION).text) and\
                    (vehicle_name == self.driver.find_element_by_xpath(VEHICLE_NAME_RENTAl_OPTION).text()) :
                estimated_total = self.driver.find_element_by_xpath(WEBELEMENt_TOTAL).text
                return estimated_total
            else:
                raise Exception
        except Exception as err:
            logging.error("The entered details are not correctly reflected in the rentaloptions page")
            return False


















        




