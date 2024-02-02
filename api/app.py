from flask_cors import CORS
from flask import Flask

from db import db

from config import DevelopmentDatabaseConfig as Dev
from routes import project_routes, transcript_route, thumbnail_route

app = Flask(__name__)
CORS(app)
app.config.from_object(Dev)

db.init_app(app)

# Register all route blueprints
app.register_blueprint(project_routes.bp)
app.register_blueprint(thumbnail_route.bp)
app.register_blueprint(transcript_route.bp)

if __name__ == "__main__":
    app.run()
