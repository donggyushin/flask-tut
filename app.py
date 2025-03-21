from flask import Flask

# __name__ == "__main__"
# 해당 파일이 직접 실행될 때만 실행되도록 만듭니다.
# 다른 파일에서 import 하면 실행되지 않아요.
app = Flask(__name__)

if __name__ == "__main__":
    app.run()
