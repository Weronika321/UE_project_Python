class Movie:
    def __init__(self, movieId: int, title: str, genres: str) -> None:
        self._movieId = movieId
        self._title = title
        self._genres = genres

    @property
    def movieId(self):
        return self._movieId

    @property
    def title(self):
        return self._title

    @property
    def genres(self):
        return self._genres

    def __dict__(self):
        return {
            "id": f"{self._movieId}",
            "title": f"{self._title}",
            "genres": f"{self._genres.rstrip()}",
        }
