import random


quiz_data = [
    {
        'id': 0,
        'question': 'Какая самая длинная река в мире?',
        'options': [
            'Нил',
            'Амазонка',
            'Ганг',
            'Дон'
        ],
        'correct_option': 0
    },
    {
        'id': 1,
        'question': 'Какой танец считается самым страстным?',
        'options': [
            'Пасадобль',
            'Танго',
            'Вальс',
            'Румба'
        ],
        'correct_option': 1
    },
    {
        'id': 2,
        'question': 'Скульптура «Медный всадник» посвящена...',
        'options': [
            'Александру I',
            'Петру I',
            'Николаю I',
            'Петру II'
        ],
        'correct_option': 1
    },
    {
        'id': 3,
        'question': 'Кто стал мужем Дюймовочки из известной сказки?',
        'options': [
            'Ласточка',
            'Жук',
            'Крот',
            'Эльф'
        ],
        'correct_option': 3
    },
    {
        'id': 4,
        'question': 'Сколько километров в одной миле?',
        'options': [
            '1.4 км',
            '1.5 км',
            '1.6 км',
            '1.7 км'
        ],
        'correct_option': 2
    },
    {
        'id': 5,
        'question': 'Сколько длилась столетняя война?',
        'options': [
            '96 лет',
            '100 лет',
            '116 лет',
            '125 лет'
        ],
        'correct_option': 2
    },
    {
        'id': 6,
        'question': 'Как называется врач, который лечит вены на ногах?',
        'options': [
            'Сосудолог',
            'Общий хирург',
            'Торакальный хирург',
            'Флеболог'
        ],
        'correct_option': 3
    },
    {
        'id': 7,
        'question': 'Этот город – административный центр Арканзаса. Какой?',
        'options': [
            'Литл-Рок',
            'Денвер',
            'Детройт',
            'Литл-Гарден'
        ],
        'correct_option': 0
    },
    {
        'id': 8,
        'question': 'На какой вопрос не могу получить ответ Гамлет?',
        'options': [
            'Что на ужин?',
            'В чем смысл жизни?',
            'Быть или не быть?',
            'Жизнь ли это?'
        ],
        'correct_option': 2
    },
    {
        'id': 9,
        'question': 'Самый просматриваемый видео-хостинг интернета',
        'options': [
            'Netflix',
            'YouTube',
            'VKVideo',
            'RuTube'
        ],
        'correct_option': 1
    },
]


def get_question_list(shuffle: bool = False, number: int | None = None) -> dict:
    data = quiz_data[:]
    if shuffle:
        random.shuffle(data)
    if number and number <= len(quiz_data):
        data = data[:number]
    return {
        'list': data,
        'index_list': [x['id'] for x in data]
    }


def create_question_list_from_indexes(index_list):
    result = []
    for index in index_list:
        result.append(quiz_data[index])
    return result
    # return [quiz_data[index] for index in index_list]
