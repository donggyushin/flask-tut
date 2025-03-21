from flask import Flask, request

# __name__ == "__main__"
# 해당 파일이 직접 실행될 때만 실행되도록 만듭니다.
# 다른 파일에서 import 하면 실행되지 않아요.
app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]

    }
]

@app.get("/store")
def get_stores():
    return {"stores": stores}

@app.post("/store")
def create_store():
    body = request.get_json()
    new_store = {
        "name": body["name"],
        "items": []
    }
    stores.append(new_store)
    return new_store, 201

if __name__ == "__main__":
    app.run()
