Активация venv:
cd scrapper_vi
source venv/bin/activate

Установка зависимостей:
pip3 install -r requirements.txt

Разовый запуск:
import main
main.fetch()

Запуск обновления по расписанию
cd scrapper_vi/scrapper_vi
python3
import scheduler
scheduler.perform_schedule()

Дашборд:
python3 dash_app.py
