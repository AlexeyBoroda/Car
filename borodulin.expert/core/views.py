from django.shortcuts import render
from .models import Review, SeoSettings
import random
from types import SimpleNamespace
from .seo_defaults import SEO_DEFAULTS
import requests
from django.http import JsonResponse

# Create your views here.

def index(request):
    reviews = Review.objects.order_by('-created_at')[:3]
    seo = SeoSettings.objects.filter(url='/').first()
    if not seo:
        seo = SimpleNamespace(**SEO_DEFAULTS)
    return render(request, 'core/index.html', {'reviews': reviews, 'seo': seo})

def about(request):
    return render(request, 'core/about.html')

TELEGRAM_BOT_TOKEN = '7591843432:AAEJLg_lIZc7jZjmCDbG3XDgiJGwcAeASSg'
TELEGRAM_CHANNEL_ID = '-1002609540648'  # chat_id вашего канала

def services(request):
    # Обработка формы заявки
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        company = request.POST.get('company', '').strip()
        service = request.POST.get('service', '').strip()
        if not name or not phone:
            return JsonResponse({'error': 'Имя и телефон обязательны.'}, status=400)
        # Формируем текст сообщения
        service_map = {
            'coaching': 'Индивидуальный коучинг',
            'training': 'Корпоративные тренинги',
            'masterclass': 'Мастер-классы и семинары',
            'consulting': 'Консультации для предпринимателей',
        }
        service_text = service_map.get(service, 'Не выбрано')
        msg = f"\U0001F4DD Новая заявка с сайта\n" \
              f"Имя: {name}\n" \
              f"Телефон: {phone}\n" \
              f"Компания: {company or '-'}\n" \
              f"Услуга: {service_text}"
        # Отправляем сообщение в канал
        send_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        resp = requests.post(send_url, data={
            'chat_id': TELEGRAM_CHANNEL_ID,
            'text': msg
        })
        # Можно добавить логирование resp.text при необходимости
        return JsonResponse({'ok': True})
    # Получаем последний отзыв для каждой услуги
    reviews_by_type = {}
    for rtype in ['coaching', 'training', 'masterclass', 'consulting']:
        review = Review.objects.filter(review_type=rtype).order_by('-created_at').first()
        reviews_by_type[rtype] = review
    return render(request, 'core/services.html', {'reviews_by_type': reviews_by_type})

def books(request):
    return render(request, 'core/books.html')

def blog(request):
    return render(request, 'core/blog.html')

def videos(request):
    return render(request, 'core/videos.html')

def reviews(request):
    # Получаем параметры фильтрации
    review_type = request.GET.get('type', '')
    date_sort = request.GET.get('date', 'newest')
    
    # Базовый QuerySet
    reviews = Review.objects.all()
    
    # Фильтрация по типу
    if review_type and review_type != 'all':
        reviews = reviews.filter(review_type=review_type)
    
    # Сортировка по дате
    if date_sort == 'oldest':
        reviews = reviews.order_by('created_at')
    else:  # по умолчанию newest
        reviews = reviews.order_by('-created_at')
    
    # Получаем список всех типов отзывов для фильтра
    review_types = Review.REVIEW_TYPE_CHOICES
    
    return render(request, 'core/reviews.html', {
        'reviews': reviews,
        'review_types': review_types,
        'current_type': review_type,
        'current_date_sort': date_sort
    })

def faq(request):
    return render(request, 'core/faq.html')

def checklists(request):
    return render(request, 'core/checklists.html')

def tools(request):
    return render(request, 'core/tools.html')

def contacts(request):
    return render(request, 'core/contacts.html')

def cabinet(request):
    return render(request, 'core/cabinet.html')

def privacy(request):
    return render(request, 'core/privacy.html')

def consent(request):
    return render(request, 'core/consent.html')

def service_detail(request, service_slug):
    # Статический контент для каждой услуги
    services_content = {
        'coaching': {
            'title': 'Индивидуальный коучинг: рост начинается с себя',
            'subtitle': 'Для предпринимателей и руководителей, готовых меняться, расти и управлять по-другому.',
            'description': 'Персональная работа 1:1 — на ваши вопросы, вызовы, решения. Без шаблонов. Только то, что важно именно вам.',
            'topics': [
                'Принятие решений и стратегия',
                'Стресс и выгорание',
                'Лидерство и влияние',
                'Баланс: бизнес, семья, энергия',
            ],
            'format': [
                'Онлайн или офлайн',
                '60 минут',
                'Разовая или серия сессий',
            ],
            'advantages': [
                'Полная конфиденциальность',
                'Без теории — только практика',
                'Профессиональный взгляд с опытом в предпринимательстве и банкротстве',
            ],
            'price': None,  # Можно добавить цену
            'cta': 'Записаться на консультацию',
        },
        'training': {
            'title': 'Тренинги, которые делают команду сильнее',
            'subtitle': 'Практика, энергия и рост — для ваших сотрудников.',
            'description': 'Авторские корпоративные тренинги, адаптированные под специфику бизнеса: от управления до продаж и мотивации.',
            'topics': [
                'Управление без авторитарности',
                'Сильные продажи без давления',
                'Сервис как конкурентное преимущество',
                'Командные ценности и сплочение',
            ],
            'format': [
                'Очный или онлайн',
                'От 3 часов до 2 дней',
                'С предварительной диагностикой',
            ],
            'advantages': [
                'Настоящие кейсы и практики',
                'Геймификация и вовлечение',
                'Результаты, которые можно измерить',
            ],
            'price': None,
            'cta': 'Оставить заявку',
        },
        'masterclass': {
            'title': 'Энергия, практика и ответы — в одном зале',
            'subtitle': 'Для предпринимателей и команд, которым важно не стоять на месте.',
            'description': '2–4-часовые мероприятия по конкретным темам: личная эффективность, финансы, бизнес-подходы.',
            'topics': [
                'Как избежать банкротства и не сдаться',
                'Предпринимательство без иллюзий',
                'Психология продаж',
                'Деньги, которые рядом',
            ],
            'format': [
                'Онлайн или офлайн',
                'До 100 человек',
                'С возможностью Q&A',
            ],
            'advantages': [
                'Без воды — только важное',
                'Личный опыт и примеры',
                'Новые знакомства и идеи',
            ],
            'price': None,
            'cta': 'Хочу на следующий мастер-класс',
        },
        'consulting': {
            'title': 'Консультации, которые экономят годы',
            'subtitle': 'Если у вас есть бизнес — или только идея, приходите с вопросами. Уйдёте с решением.',
            'description': 'Персональная встреча или звонок, на котором вы получаете конкретные ответы и план действий.',
            'topics': [
                'Бизнес-модель и стратегия',
                'Финансы и расчёты',
                'Найм и управление командой',
                'Личный ресурс предпринимателя',
            ],
            'format': [
                'Онлайн/офлайн',
                '60–90 минут',
                'Разовая или серия консультаций',
            ],
            'advantages': [
                'Я сам проходил банкротство и запускал бизнес с нуля',
                'Без мотивации — только конкретика',
                'Понятный план и фокус',
            ],
            'price': None,
            'cta': 'Записаться на консультацию',
        },
    }
    service = services_content.get(service_slug)
    if not service:
        return render(request, '404.html', status=404)
    # 3 последних отзыва по типу
    reviews = Review.objects.filter(review_type=service_slug).order_by('-created_at')[:3]
    return render(request, 'core/service_detail.html', {
        'service': service,
        'service_slug': service_slug,
        'reviews': reviews,
    })
