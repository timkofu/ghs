
class ModelTemplate:

    async def create(self) -> None:
        raise NotImplementedError

    async def read(self) -> None:
        raise NotImplementedError

    async def update(self) -> None:
        raise NotImplementedError

    async def delete(self) -> None:
        raise NotImplementedError
