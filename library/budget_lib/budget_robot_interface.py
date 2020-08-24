from robot.api.deco import keyword
from library.budget_lib.budget_home_page import BUDGET
from library.budget_lib.budget_variable import *
from robot.errors import RemoteError
import time

@keyword('Launch Budget Site')
def budget_login(url, browser_type):
    """
    Keyword to Launch the budget site
    :param url:
    :param user_name:
    :param password:
    :return:
    """
    global invoker
    retry_count = 0
    invoker = BUDGET()
    invoker.initialize_driver(browser_type)

    try:
        while retry_count<3:
            retry_count = retry_count+1
            invoker.driver.get(url)
            invoker.driver.implicitly_wait(30)
            icons_status  = invoker.driver.find_element_by_xpath(budget_icon)
            button_status = invoker.driver.find_element_by_xpath(WEB_ELEMENT_SELECT_CAR)
            if icons_status.is_displayed() and button_status.is_enabled():
                return True
            else:
                time.sleep(20)
                if retry_count>3:
                    raise Exception
    except Exception as err:
        raise RemoteError("issue in launching Budget Site")


@keyword('Select Location')
def select_locattion(location):
    """
    Keyword to select location
    :param location: <string> location tobe selected
    :return:
    """
    try:
        location_value = invoker.select_location(location)
        if location_value is not False:
            return location_value
        else:
            raise Exception
    except Exception as err:
        raise RemoteError("Issue in selecting location", fatal= False,continuable= False)


@keyword('Select PickupDate')
def select_pick_up_date():
    """
    Method to select pickupdate
    :return:
    """
    try:
        pick_up_date = invoker.selct_pick_up_date_fpr_journey()
        return pick_up_date
    except Exception as err:
        raise RemoteError("Issue in getting the pickup date")


@keyword('Select Return_date')
def select_return_date(pick_up_date):
    """
    Method to select return date
    :param pick_up_date:
    :return:
    """
    try:
        return_date = invoker.select_return_date_for_journey(pick_up_date)
        return return_date
    except Exception as err:
        raise RemoteError("Issue in selecting  return date")


@keyword('Select A CAR')
def select_a_car():
    """
    Keyword to select a car
    :return:
    """
    try:
        invoker.driver.find_element_by_xpath(BUTTON_CLICK_CAR).click()
    except Exception as err:
        raise RemoteError("Issue in selecting a car")

@keyword('SELECT CAR TYPE')
def select_vehicle_type(car_type):
    """
    Keyword to select a vehicle type based on the input
    :return:
    """
    try:
        selected_vehicl_name = invoker.select_car_type(car_type)
        if selected_vehicl_name is False:
            raise Exception
        else :
            return selected_vehicl_name
    except Exception as err:
        raise RemoteError("Issue in selecting a car type")


@keyword('Validate Selected Details')
def validate_selected_details(start_location, send_location,vehicle_name):

    try:
        estimated_total= invoker.validate_details_rental_options_page(start_location, send_location,vehicle_name)
        if estimated_total is False:
            raise Exception
        else:
            return estimated_total
    except Exception as err:
        raise RemoteError("Issue in validating the details in rental options")


@keyword('Close Browser')
def close_browser():
    """
    Keyword to close browser
    :return: N/A
    """
    try:
        invoker.driver.close()
        invoker.driver.quit()
    except Exception as err:
        raise RemoteError("Issue in closing the browser")
