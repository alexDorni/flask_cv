from portal.resources.cv import cv_bp, CvData, CvPdf
from settings import app
from util.util import swagger_docs_register

app.register_blueprint(cv_bp)

swagger_docs_register(CvData, cv_bp)
swagger_docs_register(CvPdf, cv_bp)

if __name__ == '__main__':
    app.run()
