# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__

def read_func_name_and_args(func_name, *args):
    func_name = func_name.__name__
    arguments = '; '.join(args)
    print(f'Function name: {func_name}\nArguments: {arguments if len(arguments) else "Zero arguments assigned"}')


def open_browser(browser_name):
    read_func_name_and_args(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    read_func_name_and_args(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    read_func_name_and_args(find_registration_button_on_login_page, page_url, button_text)


open_browser('Chrome')
go_to_companyname_homepage('https://www.google.com/')
find_registration_button_on_login_page('https://www.google.com/', 'login')
