text = "Hello world!"
print(text[6])
print(text[3:7])

new_txt = text.replace('l', 'L', 2)
print(text, new_txt, sep='\n')

print(text.count('l'))
print(text.index('l'))
print(text.find('l'))
print(text.find('z'))

print(text[::-1])


link = 'https://habr.com/ru/articles/671602/'
urls = link.split('/')
print(urls)


a, b, c = input('Введите три числа через пробел: ').split()
print(a, b, c)

a, b, c, *_ = input('Введите три числа через пробел: ').split()
print(a, b, c,*_)


data = ['https:', '', 'habr.com', 'ru', 'articles', '671602', '']
url = '/'.join(data)
print(url)



text = 'однаЖды в СТУДЕНУЮ зИмнЮЮ ПоРУ'
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.startswith('однаЖды'))
print(text.endswith('зИмнЮЮ', 0, -5))



text = 'Привет, мир!'
print(text.find(' '))
print(text.title())
print(text.split())
print(f'{text = :>25}')
