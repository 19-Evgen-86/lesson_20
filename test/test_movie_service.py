import pytest

from service.movie import MovieService


class TestmovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None

    def test_create(self):
        movie = self.movie_service.create({'id': 3, 'title': "title-1",
                                           'description': "description",
                                           'trailer': "trailer",
                                           'year': 2022,
                                           'rating': 15.5,
                                           'genre_id': 1,
                                           'director_id': 1})

        assert movie.id is not None

    def test_update(self):
        movie = self.movie_service.update({id: 2, 'title': "title-4"})

    def test_delete(self):
        movie = self.movie_service.delete(2)
