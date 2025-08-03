# 엔트리포인트

from flask import Flask
from routes.cohort_routes import cohort_bp
from routes.segment_routes import segment_bp
from routes.shap_routes import shap_bp
from routes.insight_routes import insight_bp

app = Flask(__name__)

# 블루프린트 등록
app.register_blueprint(cohort_bp)
app.register_blueprint(segment_bp)
app.register_blueprint(shap_bp)
app.register_blueprint(insight_bp)

if __name__ == "__main__":
    app.run(debug=True)
