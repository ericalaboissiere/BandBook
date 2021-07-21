from app.models.band_model import BandModel
from app.models.band_profile_model import BandProfileModel


def BandProfileSerializer(band_id: int):  # esperando receber o id da banda

    band = BandModel.query.get(band_id)
    """
        * BandModel.query: iniciando uma query na tabela 'bands'
        * get(band_id): utilizamos o get quando queremos pegar 
        a primary key da tabela, que no nosso caso é o id
    """
    profile = BandProfileModel.query.filter_by(band_id=band_id).first()
    """
        * BandProfileModel.query: iniciando uma query na tabela 'band_profiles'
        * filter_by(band_id=band_id): estamos fazendo uma filtragem
        para pegar a linha na qual, nesse caso, o band_id da tabela é
        igual o band_id que foi passado por parâmetro da nossa função
        * first(): retorna o primeiro resultado
    """

    return {
        "id": profile.id,
        "state": profile.state,
        "country": profile.country,
        "ein": profile.ein,
        "band": band.name,
    }


"""
    * Montando o dicionario que irá retornar para a nossa view.
    Note que, agora, temos o nome da banda no atributo band invés de só o seu id !
"""
