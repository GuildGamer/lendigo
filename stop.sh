
echo "ENDING CELERY PROCCESSES"
kill -9 $(ps aux | grep celery | grep -v grep | awk '{print $2}' | tr '\n'  ' ') > /dev/null 2>&1

echo "CLOSING SERVER"
fuser -k 8000/tcp
