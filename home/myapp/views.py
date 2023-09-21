import logging
import random

from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return render(request, 'myapp/index.html')


def index2(request):
    return HttpResponse("<h1>hello world</h1>")


def index_wo_templates(request):
    html = """
    <!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Вымышленная компания</title>
</head>
<body>
    <header>
        <h1>Добро пожаловать в вымышленную компанию</h1>
        <nav>
            <ul>
                <li><a href="/home">Главная</a></li>
                <li><a href="/about">О компании</a></li>
                <!-- Другие ссылки на страницы вашего сайта -->
            </ul>
        </nav>
    </header>
    
    <main>
        <section>
            <h2>О нашей компании</h2>
            <p>Вымышленная компания - это инновационное предприятие, которое создает будущее сегодня. 
            Мы специализируемся на разработке передовых технологий, включая искусственный интеллект, машинное обучение 
            и робототехнику.</p>
            <p>Наши продукты и решения помогают улучшить качество жизни людей и повысить эффективность бизнеса. Мы 
            работаем с клиентами по всему миру, предоставляя инновационные решения для самых сложных задач.</p>
        </section>
        
        <section>
            <h2>Наши ценности</h2>
            <p>Мы гордимся тем, что наша компания руководствуется высокими ценностями. Наша работа основана на 
            инновациях, ответственности и стремлении к качеству. Мы уделяем внимание устойчивости и защите окружающей 
            среды, и наша деятельность направлена на создание положительных изменений в обществе.</p>
        </section>
    </main>
    
    <footer>
        <p>Свяжитесь с нами по адресу 
        <a href="mailto:info@vymyshlennayakompaniya.com">info@vymyshlennayakompaniya.com</a>
        </p>
    </footer>
</body>
</html>

    """
    return HttpResponse(html)


def bin_choices(request):
    lst = ['орел', 'решка']
    result = random.choices(lst)[0]
    logger.info(f'Монетка: {result}')
    return HttpResponse(f'<h1>{result}</h1>')


def dice(request):
    result = random.randint(1, 6)
    logger.info(f'Кубик {result}')
    return HttpResponse(f'<h1>Кубик: {result}</h1>')


def rand100(request):
    result = random.randint(1, 100)
    logger.info(f'Псевдослучайное число: {result}')
    return HttpResponse(f'<h1>Псевдослучайное число: {result}</h1>')


def lesson1(request):
    return render(request, 'myapp/lesson_1.html')


def zero(request):
    x = 1 / 0
    return


def about(request):
    html = """
    <!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Вымышленная компания</title>
</head>
<body>
    <header>
        <h1>Добро пожаловать в вымышленную компанию</h1>
    </header>
    
    <main>
        <section>
            <h2>О нашей компании</h2>
            <p>Мы - вымышленная компания, специализирующаяся на разработке искусственного интеллекта и инновационных 
            решений для будущего. Наша цель - изменить мир с помощью технологий и улучшить жизни людей.</p>
        </section>
    </main>
    
    <footer>
        <p>Свяжитесь с нами по адресу 
        <a href="mailto:info@vymyshlennayakompaniya.com">info@vymyshlennayakompaniya.com</a>
        </p>
    </footer>
</body>
</html>

    """
    return HttpResponse(html)
