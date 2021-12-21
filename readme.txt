Активация venv:
cd scrapper_vi
source venv/bin/activate

Установка зависимостей:
pip3 install -r requirements.txt

Разовый запуск:
python3
import main
main.fetch()

Запуск обновления по расписанию
python3 scheduler.py

Дашборд:
python3 dash_app.py
