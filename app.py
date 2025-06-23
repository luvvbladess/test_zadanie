   #!/usr/bin/env python3
   import os
   from flask import Flask, request, escape

   app = Flask(__name__)

   @app.route("/", methods=["GET"])
   def root():
       name    = request.args.get("name",    "Recruto")
       message = request.args.get("message", "Давай дружить")
       return f"Hello {escape(name)}! {escape(message)}"

   if __name__ == "__main__":
       port = int(os.getenv("PORT", 8000))
       app.run(host="0.0.0.0", port=port)
