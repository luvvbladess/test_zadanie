import os
from flask import Flask, request, escape, Response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
   """Обрабатываем GET /?name=…&message=…"""
   name    = request.args.get("name",    "Recruto")
   message = request.args.get("message", "Давай дружить")
   text = f"Hello {escape(name)}! {escape(message)}"
   return Response(text, content_type="text/plain; charset=utf-8")

if __name__ == "__main__":
   port = int(os.getenv("PORT", 8000))
   app.run(host="0.0.0.0", port=port)
