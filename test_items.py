# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_guest_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    browser.find_element_by_css_selector('button.btn-add-to-basket')

    assert 'Yes! Button was found!', 'Button not found'
