class Links:
    def __init__(self, movieId: int, imdbld: int, tmdbld: int) -> None:
        self._movieId = movieId
        self._imdbld = imdbld
        self._tmdbld = tmdbld

    @property
    def movieId(self):
        return self._movieId

    @property
    def imdbld(self):
        return self._imdbld

    @property
    def tmdbld(self):
        return self._tmdbld

    def __dict__(self):
        return {
            "movieId": f"{self._movieId}",
            "imdbld": f"{self._imdbld}",
            "tmdbld": f"{self._tmdbld}",
        }
