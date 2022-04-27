from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


# фикстуры для director
@pytest.fixture
def director_test():
    director_test_1 = Director(id=1, name="Mike")
    director_test_2 = Director(id=2, name="Jon")
    return {1: director_test_1, 2: director_test_2}


@pytest.fixture
def director_dao(director_test):
    director_dao: DirectorDAO = DirectorDAO(None)

    director_dao.get_all = MagicMock(return_value=director_test.values())
    director_dao.get_one = MagicMock(side_effect=director_test.get)
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


# фикстуры для genre

@pytest.fixture
def genre_test():
    genre_test_test_1 = Director(id=1, name="Mike")
    genre_test_test_2 = Director(id=2, name="Jon")
    return {1: genre_test_test_1, 2: genre_test_test_2}


@pytest.fixture
def genre_dao(genre_test):
    genre_dao: GenreDAO = GenreDAO(None)

    genre_dao.get_all = MagicMock(return_value=genre_test.values())
    genre_dao.get_one = MagicMock(side_effect=genre_test.get)
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


# фикстуры для movie
@pytest.fixture
def movie_test():
    movie_test_test_1 = Movie(id=1, title="title-1",
                              description="description",
                              trailer="trailer",
                              year=2022,
                              rating=15.5,
                              genre_id=1,
                              director_id=1
                              )
    movie_test_test_2 = Movie(id=1, title="title-2",
                              description="description",
                              trailer="trailer",
                              year=2022,
                              rating=15.5,
                              genre_id=1,
                              director_id=1
                              )
    return {1: movie_test_test_1, 2: movie_test_test_2}


@pytest.fixture
def movie_dao(movie_test):
    movie_dao: MovieDAO = MovieDAO(None)

    movie_dao.get_all = MagicMock(return_value=movie_test.values())
    movie_dao.get_one = MagicMock(side_effect=movie_test.get)
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao
