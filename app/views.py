from django.shortcuts import render

developments = [
    {
        "id": 1,
        "name": "МОБИЛЬНЫЕ ПРИЛОЖЕНИЯ",
        "description": "Мы разрабатываем мобильные приложения, которые помогают бизнесам взаимодействовать с клиентами на платформах Android и iOS. Наша команда создает интуитивно понятные интерфейсы, обеспечивает высокую производительность и интеграцию с серверной частью, чтобы ваши клиенты получали лучшее мобильное решение для своих нужд.",
        "price": 100000,
        "image": "http://localhost:9000/images/1.png"
    },
    {
        "id": 2,
        "name": "WEB СЕРВИСЫ",
        "description": "Мы предлагаем разработку высоконадежных веб-сервисов, которые помогут вашему бизнесу работать эффективно. От простых сайтов до сложных веб-приложений с интеграцией данных и пользовательскими интерфейсами — мы создаем решения, которые работают быстро, надежно и безопасно.",
        "price": 50000,
        "image": "http://localhost:9000/images/2.png"
    },
    {
        "id": 3,
        "name": "VK MINI APPS",
        "description": "Мы специализируемся на разработке VK Mini Apps — приложений, которые позволяют вам взаимодействовать с миллионами пользователей ВКонтакте. Эти приложения интегрируются непосредственно с платформой VK, предоставляя пользователям уникальные сервисы без выхода из социальной сети. Это может быть как удобный инструмент для вашего бизнеса, так и развлекательный контент.",
        "price": 25000,
        "image": "http://localhost:9000/images/3.png"
    },
    {
        "id": 4,
        "name": "DEV0PS",
        "description": "Наша команда DevOps помогает оптимизировать процесс разработки и развертывания программного обеспечения. Мы внедряем практики автоматизации, настройку CI/CD, управление инфраструктурой, что позволяет ускорить релизы, повысить стабильность систем и сократить время на рутинные операции.",
        "price": 250000,
        "image": "http://localhost:9000/images/4.png"
    },
    {
        "id": 5,
        "name": "HR TECH",
        "description": "Мы разрабатываем решения для автоматизации HR-процессов. Это включает системы управления персоналом, платформы для рекрутинга, оценки сотрудников и многое другое. Наши решения помогают упростить управление кадрами, сократить время на рутинные задачи и повысить эффективность взаимодействия с персоналом",
        "price": 75000,
        "image": "http://localhost:9000/images/5.png"
    },
    {
        "id": 6,
        "name": "EDU TECH",
        "description": "Мы предлагаем решения для цифрового образования: системы управления учебными процессами (LMS), платформы для проведения онлайн-курсов и интерактивных занятий. Наши образовательные технологии помогают учебным заведениям и компаниям предоставлять качественные образовательные услуги с использованием современных цифровых инструментов.",
        "price": 150000,
        "image": "http://localhost:9000/images/6.png"
    }
]

draft_service = {
    "id": 123,
    "name": "Дмитрий",
    "company": "OOO 'ТелекомСервисКомплект'",
    "email": "info@tsk74.ru",
    "info": "хотим закончить проект до нГ",
    "developments": [
        {
            "id": 1,
            "value": "Веб-сайт"
        },
        {
            "id": 2,
            "value": "Мобильное приложение"
        },
        {
            "id": 3,
            "value": "Десктопное приложение"
        }
    ]
}


def getDevelopmentsById(development_id):
    for development in developments:
        if development["id"] == development_id:
            return development


def getDevelopmentss():
    return developments


def searchDevelopmentss(development_name):
    res = []

    for development in developments:
        if development_name.lower() in development["name"].lower():
            res.append(development)

    return res


def getDraftService():
    return draft_service


def getServiceById(service_id):
    return draft_service


def index(request):
    development_name = request.GET.get("development_name", "")
    if development_name:
        developments = searchDevelopmentss(development_name) 
    else:
        developments = getDevelopmentss()
    draft_service = getDraftService()

    context = {
        "developments": developments,
        "development_name": development_name,
        "developments_count": len(draft_service["developments"]),
        "draft_service": draft_service
    }

    return render(request, "developments_page.html", context)


def development(request, development_id):
    draft_service = getDraftService()

    context = {
        "id": development_id,
        "development": getDevelopmentsById(development_id),
        "developments_count": len(draft_service["developments"]),
        "draft_service": draft_service
    }

    return render(request, "development_page.html", context)


def service(request, service_id):
    service = getServiceById(service_id)
    draft_service = getDraftService()
    developments = [
        {**getDevelopmentsById(development["id"]), "value": development["value"]}
        for development in service["developments"]
    ]

    context = {
        "service": service,
        "developments": developments,
        "developments_count": len(draft_service["developments"]),
        "draft_service": draft_service
    }

    return render(request, "service_page.html", context)
