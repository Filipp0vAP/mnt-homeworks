# Домашнее задание к занятию "09.06 GitLab"

## Подготовка к выполнению

1. Подготовьте к работе GitLab [по инструкции](https://cloud.yandex.ru/docs/tutorials/infrastructure-management/gitlab-containers).
2. Создайте свой новый проект.
3. Создайте новый репозиторий в GitLab, наполните его [файлами](./repository).
4. Проект должен быть публичным, остальные настройки по желанию.

## Основная часть

### DevOps

В репозитории содержится код проекта на Python. Проект — RESTful API сервис. Ваша задача — автоматизировать сборку образа с выполнением python-скрипта:

1. Образ собирается на основе [centos:7](https://hub.docker.com/_/centos?tab=tags&page=1&ordering=last_updated).
2. Python версии не ниже 3.7.
3. Установлены зависимости: `flask` `flask-jsonpify` `flask-restful`.
4. Создана директория `/python_api`.
5. Скрипт из репозитория размещён в /python_api.
6. Точка вызова: запуск скрипта.
7. Если сборка происходит на ветке `master`: должен подняться pod kubernetes на основе образа `python-api`, иначе этот шаг нужно пропустить.

### Product Owner

Вашему проекту нужна бизнесовая доработка: нужно поменять JSON ответа на вызов метода GET `/rest/api/get_info`, необходимо создать Issue в котором указать:

1. Какой метод необходимо исправить.
2. Текст с `{ "message": "Already started" }` на `{ "message": "Running"}`.
3. Issue поставить label: feature.

### Developer

Пришёл новый Issue на доработку, вам нужно:

1. Создать отдельную ветку, связанную с этим Issue.
2. Внести изменения по тексту из задания.
3. Подготовить Merge Request, влить необходимые изменения в `master`, проверить, что сборка прошла успешно.


### Tester

Разработчики выполнили новый Issue, необходимо проверить валидность изменений:

1. Поднять докер-контейнер с образом `python-api:latest` и проверить возврат метода на корректность.
2. Закрыть Issue с комментарием об успешности прохождения, указав желаемый результат и фактически достигнутый.

## Итог

В качестве ответа пришлите подробные скриншоты по каждому пункту задания:

- файл gitlab-ci.yml;
- Dockerfile; 
- лог успешного выполнения пайплайна;
- решённый Issue.

---

## Ответ
### Подготовка к выполнению
-  Установил: 
    - yandex сloud cli
    - jq
    - helm
    - kubectl
    <details>
    <summary> screenshot </summary>

    ![utilits](./img/utilits.png)
    </details>

- В Yandex.Cloud создал:
    - Сеть и подсети
    - Сервисные аккаунты
    - k8s кластер и группу узлов
    - Docker registry
    - настроил kubectl на работу с кластером

    <details>
    <summary> screenshot </summary>

    ![yc](./img/yc.png)
    </details>

- В гитлабе создал публичную группу и репозиторий

    <details>
    <summary> screenshot </summary>

    ![gitlab](./img/gitlab.png)

    </details>

### DevOps

- С помощью Helm поднял и зарегистрировал GitLab Runner 
    <details>
    <summary> screenshot </summary>

    ![runner](./img/runner.png)
    </details>

- Написал:
    - [Dockerfile](./repository/Dockerfile)
    - k8s манифест [k8s.yaml](./repository/k8s.yaml)
    - gitlab ci конфиг [.gitlab-ci.yml](./repository/.gitlab-ci.yml)

### Product Owner

- Создал задачу
    <details>
    <summary> screenshot </summary>

    ![new_issue](./img/new_issue.png)
    </details>

### Developer

- Открыл MR и создал новую ветку
    <details>
    <summary> screenshot </summary>

    ![open_mr](./img/open_mr.png)
    </details>

- Внес изменения
    <details>
    <summary> screenshot </summary>

    ![fix](./img/fix_new_branch.png)
    </details>

- Выполнил merge и закрыл MR
    <details>
    <summary> screenshot </summary>

    ![resolve_mr](./img/resolve_mr.png)
    </details>

- Проверил Pipeline 
    <details>
    <summary> screenshot </summary>

    ![pipeline](./img/pipeline_mr.png)

    </details>

- Билд прошел успешно
    <details>
    <summary> screenshot </summary>

    ![build_1](./img/build_1.png)
    ![build_2](./img/build_2.png)
    ![build_3](./img/build_3.png)
   </details>
    лог: 
    
    [build_log](./logs/build.log)
- Деплой тоже
    <details>
    <summary> screenshot </summary>

    ![deploy](./img/deploy.png)
   </details>
    лог: 
    
    [deploy_log](./logs/deploy.log)

### Tester
- Ответ от приложения проверил
    <details>
    <summary> screenshot </summary>

    ![curl](./img/curl_mr.png)
   </details>
- Issue закрыл
    <details>
    <summary> screenshot </summary>

    ![close_issue](./img/close_issue.png)
   </details>
---
### Важно 
После выполнения задания выключите и удалите все задействованные ресурсы в Yandex Cloud.

## Необязательная часть

Автоматизируйте работу тестировщика — пусть у вас будет отдельный конвейер, который автоматически поднимает контейнер и выполняет проверку, например, при помощи curl. На основе вывода будет приниматься решение об успешности прохождения тестирования.

---
