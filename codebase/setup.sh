sudo amazon-linux-extras install python3.8
python3.8 -m venv venv
source venv/bin/activate
pip install psycopg2-binary
pip install -r requirements.txt
python -m pip install cx_Oracle --upgrade
npm install pm2@latest -g
pm2 start pm2_config.json
