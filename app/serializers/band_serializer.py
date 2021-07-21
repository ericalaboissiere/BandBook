from app.models.band_model import BandModel


def BandSerializer(band_id: int):
    band = BandModel.query.get(band_id)
    albums = band.albums
    music_list = band.music_list
    genre_list = band.genre_list
    """
        * Utilizamos o BandModel para conseguir o id e nome da banda a ser referenciada 
          a partir do band_id passado por parametro, além de conseguir acesso a music_list
          e genre_list que já foram declaradas lá atrás pensando numa listagem simples.
    """
    return {
        "id": band.id,
        "name": band.name,
        "albums": [album.name for album in albums],
        "musics": [music.name for music in music_list],
        "genres": [genre.name for genre in genre_list],
    }
    """
      * Fazemos um list comprehension para listar todas as musicas guardadas dentro do objeto MusicModel music_list
      * Fazemos um list comprehension para listar todos os generos guardados dentro do objeto GenreModel genre_list
      * Retornamos as informações de uma maneira agradável para o usuario que faz a requisição
    """
