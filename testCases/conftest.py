import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
import pandas as pd
import pyodbc
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Type in browser name e.g. chrome or edge")


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class")
def browser_setup(browser):
    if browser == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--ignore-certificate-errors")
        edge_options.add_argument("--allow-running-insecure-content")  # Allow HTTP content instead of https content
        edge_options.add_argument("--disable-features=BlockInsecurePrivateNetworkRequests")
        edge_options.add_argument("--disable-features=SSLHandshake")
        driver = webdriver.Edge(options=edge_options)
    elif browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-features=SSLHandshake")
        chrome_options.add_argument("--allow-running-insecure-content")  # Allow HTTP content instead of https content
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-features=BlockInsecurePrivateNetworkRequests")
        driver = webdriver.Chrome(options=chrome_options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


########## PyTest HTML Report ############
def pytest_configure(config):
    # Check if pytest-html is being used
    if hasattr(config, 'metadata'):
        config.metadata['Project Name'] = 'MITR'
        config.metadata['Module Name'] = 'LoginTesting'
        config.metadata['Tester'] = 'Mani'


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    # Your existing hook logic
    pass


@pytest.fixture(scope="class")
def pandas_excel():
    def _load_data(sheet_name):
        file_path = r"C:\Users\Ah$admin\PycharmProjects\Project_AIG\TestData\HIS_DATA_WorkBook.xlsx"
        return pd.read_excel(file_path, sheet_name=sheet_name)
    return _load_data


