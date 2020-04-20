# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                    action='store',
                    default='chrome',
                    help='Выберите браузер: chrome или firefox')
    parser.addoption('--language',
                    action='store',
                    default=None,
                    help='Выберите язык: ru, en-gb, ..., (etc)')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    browser = None
    if browser_name == 'chrome':
        print('\nStart chrome browser for test......')
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language}, )
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print('\nStart firefox browser for test......')
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_language', user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError(
            '--browser_name должно быть chrome или firefox')
    yield browser
    print('\nQuit browser....')
    browser.quit()
