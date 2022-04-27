import pytest

from service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None

    def test_create(self):
        director = self.director_service.create({id: 3, 'name': "Kate"})

        assert director.id is not None

    def test_update(self):
        director = self.director_service.update({id: 3, 'name': "Katerine"})

    def test_delete(self):
        director = self.director_service.delete(2)
