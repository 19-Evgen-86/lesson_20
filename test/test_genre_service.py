import pytest

from service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None

    def test_create(self):
        genre = self.genre_service.create({id: 3, 'name': "Kate"})

        assert genre.id is not None

    def test_update(self):
        genre = self.genre_service.update({id: 3, 'name': "Katerine"})

    def test_delete(self):
        genre = self.genre_service.delete(2)