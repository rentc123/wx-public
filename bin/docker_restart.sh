sudo docker stop wx_pub
sudo docker run -idt --rm -p 80:80 -v /home/docker/apps/wx-public:/home/docker --network bot --name wx_pub rentc123/dialogue_base python wx-pub.py