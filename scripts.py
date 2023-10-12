import random

from django.core.exceptions import ObjectDoesNotExist

from datacenter.models import (Schoolkid, Mark, Subject,
                               Lesson, Commendation, Chastisement)


def create_commendation(schoolkid, subject):
    try:
        kid = Schoolkid.objects.get(full_name__contains=f'{schoolkid}')
        subj = Subject.objects.filter(title=f'{subject}',
                                      year_of_study=kid.year_of_study)[0]
    except ObjectDoesNotExist:
        print('Имя или название предмета введены неверно. '
              'Пример:"Имя Фамилия Отчество", "Математика"')
    else:
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
    try:
        kid = Schoolkid.objects.get(full_name__contains=f'{schoolkid}')
    except ObjectDoesNotExist:
        print('Имя введено неверно. Пример:"Имя Фамилия Отчество"')
    else:
        chastisements = Chastisement.objects.filter(schoolkid=kid)
        chastisements.delete()


def fix_marks(schoolkid):
    try:
        kid = Schoolkid.objects.get(full_name__contains=f'{schoolkid}')
    except ObjectDoesNotExist:
        print('Имя введено неверно. Пример:"Имя Фамилия Отчество"')
    else:
        bad_marks = Mark.objects.filter(schoolkid=kid, points__lte=3)
        for bad_mark in bad_marks:
            bad_mark.points = 5
            bad_mark.save()
