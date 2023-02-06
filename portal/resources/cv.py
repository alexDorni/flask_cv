from flask import Blueprint
from flask_apispec import doc
from flask_apispec.views import MethodResource
from flask_restful import Resource, Api
from marshmallow import ValidationError

from mockup.example import get_yaml_data, get_pdf_data
from portal.schemas.cv_schema import CvSchema, CvPdfSchema, CvPdfDetailsSchema

cv_bp = Blueprint('cv_bp', __name__)
api = Api(cv_bp)
cv_schema = CvSchema()


class CvData(MethodResource, Resource):
    @doc(description='CV endpoints: data, profile, experience, education, courses, hobbies, language',
         tags=['CV REST API'])
    def get(self, endpoint: str) -> dict:
        """Get CV data by endpoints:

        :param endpoint: str
            cv data endpoint: 'data', 'profile', 'experience', 'education', 'courses', 'hobbies', 'language'

        :return: dict[str, str]
            str: cv item or error
            str: cv item value or error value
        """
        try:
            data = get_yaml_data()
            cv_data = cv_schema.load(data)

            if 'data' == endpoint:
                return cv_schema.dump(cv_data)
            return cv_data[endpoint]
        except OSError:
            return {'error': 'Invalid path for yaml file'}
        except ValidationError as err:
            return {'error': str(err)}
        except KeyError:
            return {'error': 'Incorrect endpoint'}


class CvPdf(MethodResource, Resource):
    @doc(description='CV pdf partial data', tags=['CV REST API'])
    def get(self):
        """Get CV pdf data

        :return: dict[str, str]
            str: cv item or error
            str: cv item value or error value
        """
        try:
            pdf_data = {
                'pdf_data': get_pdf_data()
            }
            details = CvPdfDetailsSchema().dump(pdf_data)
            return CvPdfSchema().dump({'profile': details})
        except OSError:
            return {'error': 'Invalid path for pdf file'}


api.add_resource(CvData, '/cv/<endpoint>')
api.add_resource(CvPdf, '/cv/pdf')
