from mockup.example import get_yaml_data
from portal.schemas.cv_schema import CvSchema


def test_yaml_fixtures():
    response_data = {
        'profile': 'Profile test',
        'experience': 'Employment history or experience test',
        'education': 'Education test',
        'courses': 'Courses test',
        'hobbies': 'Hobbies test',
        'language': 'Language test',
    }
    yaml_data = get_yaml_data()
    cv_data = CvSchema().load(yaml_data)

    assert cv_data == response_data
