import random

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from datacenter.models import (Schoolkid, Mark, Subject,
                               Lesson, Commendation, Chastisement)


def create_commendation(schoolkid, subject):
    kid = get_schoolkid(schoolkid)
    if kid:
        subj = get_subject(kid, subject)
        if subj:
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
    if kid:
        chastisements = Chastisement.objects.filter(schoolkid=kid)
        chastisements.delete()


def fix_marks(schoolkid):
    kid = get_schoolkid(schoolkid)
    if kid:
        bad_marks = Mark.objects.filter(schoolkid=kid, points__lte=3)
        bad_marks.update(points=5)


def get_schoolkid(schoolkid):
    try:
        kid = Schoolkid.objects.get(full_name__contains=f'{schoolkid}')
    except Schoolkid.DoesNotExist:
        print('Имя введено неверно. Пример:"Имя Фамилия Отчество"')
        return None
    except Schoolkid.MultipleObjectsReturned:
        print('Найдено несколько имен, введите полное имя.')
        return None
    else:
        return kid


def get_subject(kid, subject):
    try:
        subj = Subject.objects.get(title=f'{subject}',
                                   year_of_study=kid.year_of_study)
    except Subject.DoesNotExist:
        print('Название предмета введено неверно. Пример:"Математика"')
        return None
    else:
        return subj.first()
