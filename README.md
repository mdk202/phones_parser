# Парсер смартфонов с OZON

__Задание__

На сайте ozon.ru в категории “Электроника -> Телефоны и смарт-часы” с сортировкой “Высокий рейтинг” нужно собрать информацию о первых 100 смартфонах попавших в выборку. Перейти на страницу с каждым из них и забрать информацию о версии ОС из характеристик. По собранным данным построить распределение моделей по версиям ОС в порядке убывания.

Для обхода защиты от роботов на сайте использовался список бесплатных мобильных версий пользовательских агентов (user-agents), представленный в файле ___agents.py___, который переодически изменялся ([List of all Mobile Browsers](https://www.useragentstring.com/pages/Mobile%20Browserlist/), [Мобильные версии User Agents](https://useragents.ru/mobile.html)).

__Пример вывода__
```
iOS      17         32
         16         17
         15         12
Android  None       11
         13         10
         Global     10
         11          2
iOS      14          2
         JP          2
         None        2
```

У некоторых смартфонов в характеристиках отсутствует информация о версии ОС и присутствует только информация о версии смартфона (примеры из выборки: [Apple Смартфон iPhone 13 JP 4/128 ГБ, синий](https://www.ozon.ru/product/apple-smartfon-iphone-13-jp-4-128-gb-siniy-1409455675/features/) и [Xiaomi Смартфон Redmi Note 13 Pro Глобальная версия Global 12/512 ГБ, черный](https://www.ozon.ru/product/xiaomi-smartfon-redmi-note-13-pro-globalnaya-versiya-global-12-512-gb-chernyy-1042182421/features/)), принято решение для таких смартфонов в качестве версиии ОС взять версию смартфона.

Также есть смартфоны, у которых отсутствуют версии и ОС, и смартфона (примеры из выборки: [Poco Смартфон POCO F5 5G 12/256 ГБ, белый](https://www.ozon.ru/product/poco-smartfon-poco-f5-5g-12-256-gb-belyy-1042628622/features/) и [Apple Смартфон iPhone 14 Pro Max_eSIM+SIM 6/256 ГБ, фиолетовый](https://www.ozon.ru/product/apple-smartfon-iphone-14-pro-max-esim-sim-6-256-gb-fioletovyy-711972817/features/)), для таких смартфонов версии ОС присваивается значение _None_.
