kill -TERM $(cat /home/box/web/gu.pid)
cd /home/box/web/ask/ask/
gunicorn -c /home/box/web/etc/gunicorn.conf wsgi
