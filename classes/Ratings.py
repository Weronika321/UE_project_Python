class Ratings:
    def __init__(
        self, userId: int, movieId: int, rating: float, timestamp: int
    ) -> None:
        self._userId = userId
        self._movieId = movieId
        self._rating = rating
        self._timestamp = timestamp

    @property
    def userId(self):
        return self._userId

    @property
    def movieId(self):
        return self._movieId

    @property
    def rating(self):
        return self._rating

    @property
    def timestamp(self):
        return self._timestamp

    def __dict__(self):
        return {
            "userId": f"{self._userId}",
            "movieId": f"{self._movieId}",
            "rating": f"{self._rating}",
            "timestamp": f"{self._timestamp}",
        }
