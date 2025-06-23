#!/usr/bin/env python3
import os

from flask import Flask, request, Response, redirect, url_for
from markupsafe import escape          # ← для XSS-экранирования

app = Flask(__name__)

DEFAULT_NAME    = "Recruto"
DEFAULT_MESSAGE = "Давай дружить"

@app.route("/", methods=["GET"])
def root() -> Response:
   name    = request.args.get("name")
   message = request.args.get("message")

    # Если хотя бы одного параметра нет – делаем редирект на канонический URL
   if name is None or message is None:
      return redirect(
         url_for("root", name=DEFAULT_NAME, message=DEFAULT_MESSAGE),
         code=302,
      )
   text = f"Hello {escape(name)}! {escape(message)}"
   return Response(text, content_type="text/plain; charset=utf-8")

if __name__ == "__main__":
   port = int(os.getenv("PORT", 8000))
   app.run(host="0.0.0.0", port=port)
