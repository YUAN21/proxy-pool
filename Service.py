from flask import Flask
from DataBase import RedisClient

app = Flask(__name__)

@app.route('/proxy')
def get_proxy():
    db = RedisClient()
    proxy = db.get_proxy()
    return proxy

if __name__ == '__main__':
    app.run()