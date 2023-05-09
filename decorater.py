import webbrowser

def validator(func):
    def wrapper(url):
        if '.' in url:
            func(url)
        else:
            print('неверный url')
    return wrapper

@validator
def open_url(url):
    webbrowser.open(url)

open_url('https://translate.yandex.ru/?source_lang=en&target_lang=ru')