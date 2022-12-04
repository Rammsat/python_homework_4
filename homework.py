def replace(name, *args):
    replace_name = name.__name__.title().replace('_', ' ').__add__(":")
    print(replace_name, *args)


def open_browser(browser_name):
    replace(open_browser, browser_name)


def go_to_company_name_homepage(page_url):
    replace(go_to_company_name_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    replace(find_registration_button_on_login_page, page_url, button_text)


open_browser('Opera')
go_to_company_name_homepage('https://goodgame.ru')
find_registration_button_on_login_page('https://goodgame.ru', 'Вход')