# rtkgenerator


pip3 install -r requirements.txt

Для того, чтобы добавить удалённый репозиторий и присвоить ему имя (shortname), 
просто выполните команду git remote add <shortname> <url>:

git remote add rtkgenerator https://github.com/margiemar/rtkproject.git

Перезапись ссылки: 
git remote set-url origin git://new.url.here

Удаление репозитория из списка:
git remote remove rtkgenerator

Просмотр добавленного репозитория:

D:\GENERATOR_RTK_GIT>git remote -v
rtkgenerator    https://github.com/margiemar/rtkproject.git (fetch)
rtkgenerator    https://github.com/margiemar/rtkproject.git (push)



Git clone - команда клонирования репозитория - используется для первоначального копирования репозитория, 
т.е. для создания копии на вашей машине, когда у вас вообще ничего нет - скачает всю информацию.
Делает git init автоматом.

Git pull - команда для получения последних изменений - используется именно для получения последних изменений, 
т.е. для получения той информации, что добавили ваши коллеги - скачает только последние изменения.

D:\GENERATOR_RTK_GIT>git pull rtkgenerator master

Шаги по заливке проекта.
1. Создать репозиторий с gitignore python
2. 
git init
git remote add rtkgenerator https://github.com/margiemar/rtkgenerator.git
git pull rtkgenerator master - скопировать gitignore локально.
Скопировать или создать рабочий каталог.
git add .
git commit -m "First model"
git push rtkgenerator master
