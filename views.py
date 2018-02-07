from app import app, status
from models import ZipToGeo, GiveMeBacon
from helpers import logger


@app.route('/<code>', methods=['GET'])
@logger
def get_country_by_zip_code(code):
    try:
        return {'values': ZipToGeo(code).get_country}, status.HTTP_200_OK
    except(IndexError, AttributeError):
        return {'ERROR': f'{code} not found'}, status.HTTP_404_NOT_FOUND


@app.route('/talk/<request>', methods=['GET'])
@logger
def talk(request):
    bacon = GiveMeBacon(request)
    return {
        'You say:': bacon.request,
        'Bacon says:': bacon.get_meat
    }, status.HTTP_200_OK
