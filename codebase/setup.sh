sudo amazon-linux-extras install python3.8
python3.8 -m venv venv
source venv/bin/activate
pip install psycopg2-binary
pip install -r requirements.txt
python -m pip install cx_Oracle --upgrade
npm install pm2@latest -g
sudo su
wget https://download.oracle.com/otn_software/linux/instantclient/218000/instantclient-basic-linux.x64-21.8.0.0.0dbru.zip
tar –xvzf instantclient-basic-linux.x64-21.8.0.0.0dbru.zip
exit

export LD_LIBRARY_PATH=/home/instantclient_21_8
pm2 start pm2_config.json


