from for_exam.questions_for_3_plus import *

wrong_answers = {}
right_answers = []

for question in questions_and_answers:
    print('===================================================================')
    print(question)  # Вывод вопроса на экран
    print('===================================================================')
    answer = None
    wrong = False
    while not answer:
        answer = input('Введите один или несколько вариантов ответа: ')
        if not answer.isdigit():
            answer = None
    answer = [int(i) for i in answer]
    if answer == [0]:
        break
    for i in answer:
        if i not in questions_and_answers[question]:
            wrong = True
    if len(questions_and_answers[question]) != len(answer):
        wrong = True
    if wrong:
        wrong_answers[question] = answer
    else:
        right_answers.append(question)

if wrong_answers:
    total = len(questions_and_answers.keys())
    success = len(right_answers)
    wrong_answers = [i + '\nВаш ответ: {0}, Верный ответ: {1}'.format(wrong_answers[i], questions_and_answers[i]) for i
                     in wrong_answers]
    wrong_answers = '\n\n'.join(wrong_answers)
    exception = '\n=======================================\n' \
                'Правильных ответов: {0} из {1}\n' \
                '=======================================\n' \
                'Вопросы, в которых допущены ошибки:\n{2}' \
                ''.format(success, total, wrong_answers)
    raise AssertionError(exception)
else:
    print('Тест успешно пройден')
