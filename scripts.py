import random

from datacenter.models import (Schoolkid, Mark, Subject,
                               Lesson, Commendation, Chastisement)


def create_commendation(schoolkid, subject):
    kid = get_schoolkid(schoolkid)
    subj = get_subject(kid, subject)
    lessons = Lesson.objects.filter(
        year_of_study=kid.year_of_study,
        group_letter=kid.group_letter,
        subject=subj
    )
    last_lesson = lessons.order_by('date').last()

    with open('commends.txt', 'r') as file:
        commend = random.choice([x.strip() for x in file])

    Commendation.objects.create(
        text=commend, created=last_lesson.date, schoolkid=kid,
        subject=subj, teacher=last_lesson.teacher)


def remove_chastisements(schoolkid):
    kid = get_schoolkid(schoolkid)
    chastisements = Chastisement.objects.filter(schoolkid=kid)
    chastisements.delete()


def fix_marks(schoolkid):
    kid = get_schoolkid(schoolkid)
    bad_marks = Mark.objects.filter(schoolkid=kid, points__lte=3)
    bad_marks.update(points=5)


def get_schoolkid(schoolkid):
    try:
        kid = Schoolkid.objects.get(full_name__contains=f'{schoolkid}')
    except Schoolkid.DoesNotExist:
        raise Schoolkid.DoesNotExist(
            'Имя введено неверно. Пример:"Имя Фамилия Отчество"') from None
    except Schoolkid.MultipleObjectsReturned:
        raise Schoolkid.MultipleObjectsReturned(
            'Найдено несколько имен, введите полное имя.') from None
    else:
        return kid


def get_subject(kid, subject):
    try:
        subj = Subject.objects.get(title=f'{subject}',
                                   year_of_study=kid.year_of_study)
    except Subject.DoesNotExist:
        raise Subject.DoesNotExist(
            'Название предмета введено неверно. Пример:"Математика"') \
            from None
    else:
        return subj
