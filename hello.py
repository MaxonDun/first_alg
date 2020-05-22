import requests
i=500000
while i < 503400:
    try:
        response = requests.get(f'https://habr.com/ru/post/{i}/', timeout=5)
        if 'class="inline-list__item-link post__tag  ">python</a></li>' in response.text:
            print(response.url)
    except:
        print("Страницы не существует")
    i+=1
    print(i)
# 'class="inline-list__item-link post__tag  ">программирование</a></li>'
