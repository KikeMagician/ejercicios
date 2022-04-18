"""
Escriba un programa que muestre las noticias más recientes de Google News.
"""

from GoogleNews import GoogleNews

news = GoogleNews()
news.search('gundam')
result = news.result()
for n in range(len(result)):
    print(n)
    for y in result[n]:
        print(y, '\n', result[n][y])

