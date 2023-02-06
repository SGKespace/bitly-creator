# main
Скрипт для сокращения ссылок в командной строке с помощью ресурса bitly.com - требуется регистрация! 


Полученный токен надо поместить в переменные окружения. Например в файл .env
<img width="703" alt="image" src="https://user-images.githubusercontent.com/55636018/216776142-725dc191-b820-492f-9766-d3f02cc30f2c.png">


Документация по API https://dev.bitly.com/api-reference/#createBitlink


## Примеры запуска скрипта 

## 1. Вариант - диалоговый, код в программе
<img width="323" alt="image" src="https://user-images.githubusercontent.com/55636018/216811237-fb7291d5-2ec9-48b6-b65a-baa187d5cd8d.png">


Запуск в командной строке

```
python3 main.py 
```

Результат

<img width="362" alt="image" src="https://user-images.githubusercontent.com/55636018/216755753-c335d97e-92cc-403c-a114-183398837529.png">

<img width="373" alt="image" src="https://user-images.githubusercontent.com/55636018/216755800-a7fcdb25-9589-4bad-8ea4-13a0c2e38c8c.png">


## 2. Вариант - отладочный, код в программе
<img width="357" alt="image" src="https://user-images.githubusercontent.com/55636018/216811359-847bc279-ca14-4485-a262-82e3eeecca03.png">


Запуск в командной строке
```
python3 main.py https://www.google.com 
```

Следует иметь ввиду, что в отладочном варианте, если Вы забыли ввести ссылку, то подставится значение по умолчанию https://google.com

Результат

<img width="554" alt="image" src="https://user-images.githubusercontent.com/55636018/216811685-39825988-f7d5-496c-907e-f4130062c7ac.png">


## Требования к окружению

Python 3.xx и выше (должен быть уже установлен)

requests 2.24.0

dotenv 0.21.1

Можно установить командой  
``` 
PIP install -r requirement.txt
```


## Отказ от ответственности

Автор ппрограммы не несет никакой ответственности за то, как вы используете этот код или как вы используете сгенерированные с его помощью данные. Эта программа была написана для обучения автора и других целей не несет. Не используйте данные, сгенерированные с помощью этого кода в незаконных целях.
