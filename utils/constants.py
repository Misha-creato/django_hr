EXPERIENCE_CHOICES = (
    ('0_', 'Без опыта',),
    ('1_3', 'От 1 до 3 лет',),
    ('3_6', 'От 3 до 6 лет',),
    ('6_', 'От 6 лет',),
)
EMPLOYMENT_CHOICES = (
    ('full', 'Полная занятость',),
    ('part', 'Частичная занятость',),
    ('probation', 'Стажировка',),
)
SCHEDULE_CHOICES = (
    ('full_day', 'Полный день',),
    ('shift', 'Сменный график',),
    ('flexible', 'Гибкий график',),
    ('remote', 'Удаленная работа',),
    ('fly_in_fly_out', 'Вахтовый метод',),
)
RESUME_VALID_EXTENSIONS = [
    '.doc',
    '.docx',
    '.pdf',
]
