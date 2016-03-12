sudo apt-get update
sudo apt-get install nginx
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/qa_service
sudo /etc/init.d/nginx start
sudo /etc/init.d/mysql start
mysql -u root -e "CREATE DATABASE mydb;"
