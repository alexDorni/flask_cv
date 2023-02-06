import re

from marshmallow import Schema, fields, post_dump


class CvSchema(Schema):
    profile = fields.Str()
    experience = fields.Str()
    education = fields.Str()
    courses = fields.Str()
    hobbies = fields.Str()
    language = fields.Str()


class CvPdfTextSchema(Schema):
    pdf_data = fields.Str()


class CvPdfDetailsSchema(CvPdfTextSchema):
    data = fields.Dict()

    @post_dump
    def preprocess_data(self, data, **kwargs):
        details = re.search('(?<=DETAILS ).*.(?<=LINKS)', data['pdf_data'])
        details = details.group(0)
        data['data'] = dict(list(zip(*[iter(details.split(' '))] * 2)))

        del data['data']['DATE']
        del data['pdf_data']

        return data


class CvPdfSchema(CvPdfTextSchema):
    profile = fields.Dict(dump_default='Pdf profile dummy')
    experience = fields.Str(dump_default='Pdf experience dummy')
    education = fields.Str(dump_default='Pdf education dummy')
    courses = fields.Str(dump_default='Pdf courses dummy')
    hobbies = fields.Str(dump_default='Pdf hobbies dummy')
    language = fields.Str(dump_default='Pdf language dummy')
