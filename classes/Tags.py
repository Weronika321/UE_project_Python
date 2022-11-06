class Tags:
    def __init__(
        self, userId: int, movieId: int, tag: str, timestamp: int
    ) -> None:
        self._userId = userId
        self._movieId = movieId
        self._tag = tag
        self._timestamp = timestamp

    @property
    def userId(self):
        return self._userId

    @property
    def movieId(self):
        return self._movieId

    @property
    def tag(self):
        return self._tag

    @property
    def timestamp(self):
        return self._timestamp

    def __dict__(self):
        return {
            "userId": f"{self._userId}",
            "movieId": f"{self._movieId}",
            "tag": f"{self._tag}",
            "timestamp": f"{self._timestamp}",
        }
