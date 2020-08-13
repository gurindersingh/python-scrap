import time
import base64
import os
import utils
from webdriver_wrapper import WebDriverWrapper
from selenium.webdriver.common.keys import Keys

os.environ['API_ENV'] = 'local'

def lambda_handler(*args, **kwargs):
    driver = WebDriverWrapper()

    driver.get_url('https://www.gta-homes.com/')

    # body = driver.get_body()

    # print(body)

    driver.close()

    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!'),
    #     'name': base64.b64encode(body.encode("utf-8"))
    # }


def add_chromedriver_to_path():
    """
    Appends the directory of the chromedriver binary file to PATH.
    """
    # chromedriver_dir = os.path.abspath(os.path.dirname(__file__))
    local_lib = os.path.abspath(os.path.dirname(__file__)) + '/lib'

    os.environ['PATH'] = local_lib + utils.get_variable_separator() + os.environ['PATH']

    # if 'PATH' not in os.environ:
    #     os.environ['PATH'] = chromedriver_dir
    # elif chromedriver_dir not in os.environ['PATH']:
    #     os.environ['PATH'] = chromedriver_dir + utils.get_variable_separator() + os.environ['PATH']
    #     os.environ['PATH'] = local_lib + utils.get_variable_separator() + os.environ['PATH']

    print(os.environ.get('PATH'))
    lambda_handler()


# chromedriver_filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), utils.get_chromedriver_filename())

add_chromedriver_to_path()
