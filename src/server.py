from app import app
import os
import controllers.chat_controller

PORT = int(os.environ.get('PORT', 5000))

app.run("0.0.0.0", PORT, debug=True)