import os

import pypdf
import yaml

path_example = f'{os.getcwd()}/fixtures'


def get_yaml_data() -> dict:
    yaml_example = f'{path_example}/cv_example.yaml'
    with open(yaml_example, 'r') as stream:
        data = yaml.load(stream, Loader=yaml.FullLoader)
        return data


def get_pdf_data() -> str:
    pdf_example = f'{path_example}/example/self_cv.pdf'
    reader = pypdf.PdfReader(pdf_example)

    pdf_data = ''
    for page in range(len(reader.pages)):
        pdf_data += reader.pages[page].extract_text()
    pdf_data = pdf_data.replace('\n', ' ')

    return pdf_data
