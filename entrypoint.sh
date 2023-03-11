
python manage.py makemigrations entries --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec "$@"
