# Домашнее задание к занятию "10.04 Система сбора логов Elastic Stack"

## Дополнительные ссылки

При выполнении задания используйте дополнительные ресурсы:

- [поднимаем elk в docker](https://www.elastic.co/guide/en/elastic-stack-get-started/current/get-started-docker.html);
- [поднимаем elk в docker с filebeat и docker-логами](https://www.sarulabs.com/post/5/2019-08-12/sending-docker-logs-to-elasticsearch-and-kibana-with-filebeat.html);
- [конфигурируем logstash](https://www.elastic.co/guide/en/logstash/current/configuration.html);
- [плагины filter для logstash](https://www.elastic.co/guide/en/logstash/current/filter-plugins.html);
- [конфигурируем filebeat](https://www.elastic.co/guide/en/beats/libbeat/5.3/config-file-format.html);
- [привязываем индексы из elastic в kibana](https://www.elastic.co/guide/en/kibana/current/index-patterns.html);
- [как просматривать логи в kibana](https://www.elastic.co/guide/en/kibana/current/discover.html);
- [решение ошибки increase vm.max_map_count elasticsearch](https://stackoverflow.com/questions/42889241/how-to-increase-vm-max-map-count).

В процессе выполнения в зависимости от системы могут также возникнуть не указанные здесь проблемы.

Используйте output stdout filebeat/kibana и api elasticsearch для изучения корня проблемы и её устранения.

## Задание повышенной сложности

Не используйте директорию [help](./help) при выполнении домашнего задания.

## Задание 1

Вам необходимо поднять в докере и связать между собой:

- elasticsearch (hot и warm ноды);
- logstash;
- kibana;
- filebeat.

Logstash следует сконфигурировать для приёма по tcp json-сообщений.

Filebeat следует сконфигурировать для отправки логов docker вашей системы в logstash.

В директории [help](./help) находится манифест docker-compose и конфигурации filebeat/logstash для быстрого 
выполнения этого задания.

Результатом выполнения задания должны быть:

- скриншот `docker ps` через 5 минут после старта всех контейнеров (их должно быть 5);
- скриншот интерфейса kibana;
- docker-compose манифест (если вы не использовали директорию help);
- ваши yml-конфигурации для стека (если вы не использовали директорию help).

## Задание 2

Перейдите в меню [создания index-patterns в kibana](http://localhost:5601/app/management/kibana/indexPatterns/create) и создайте несколько index-patterns из имеющихся.

Перейдите в меню просмотра логов в kibana (Discover) и самостоятельно изучите, как отображаются логи и как производить поиск по логам.

В манифесте директории help также приведено dummy-приложение, которое генерирует рандомные события в stdout-контейнера.
Эти логи должны порождать индекс logstash-* в elasticsearch. Если этого индекса нет — воспользуйтесь советами и источниками из раздела «Дополнительные ссылки» этого задания.

---

## Ответы

### Задание 1

Использовал файлы из директории help, ```но все равно потратил два дня на настройку logstash (боже)```

- Поднятые контейнеры:
![docker_ps](./img/docker_ps.png)

- Kibana:
![kibana](./img/kibana.png)

- [docker-compose манифест](./help/docker-compose.yml)
- [ваши yml-конфигурации для стека](./help/configs/)

### Задание 2

Резюмирую все что помогло добиться результата

- Прописал всем контейнерам сеть elastic
- Поправил volume у logstash
- Указал всем образам последнюю 7 версию 
- Убрал флаг :Z из всех volume
- добавил HealthCheck в эластики чтоб дожидаться полного их поднятия
- Видимо после обновления logstash до последней версии он начал случать другой порт, пришлось править это во всех конфигах
- Так же в конфиге Logstash исправил имя индекса и фильтр
- Поправил питон скрипт что бы были видны info сообщения и что бы исключения выводились корректно
- так же еще несколько мелочей вроде поднятия версии docker compose файла и тд
 
Вот на это я потратил уже очень много времени

И вот наконец то результат
![logstash_index](./img/logstash_index.png)
![some_app_logs](./img/some_app_logs.png)

---

### Как оформить решение задания

Выполненное домашнее задание пришлите в виде ссылки на .md-файл в вашем репозитории.

---

 
