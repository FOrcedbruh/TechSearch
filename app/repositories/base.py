from typing import Protocol, Any, reveal_type
from tortoise import Model
from uuid import UUID


class RepositoryProtocol(Protocol):

    async def get_one(self, id: int | UUID) -> Any: ...

    async def create(self, data: dict) -> Any: ...

    async def update(self, data: dict, id: int | UUID) -> Any: ...

    async def delete(self, id: int | UUID) -> None: ...


class BaseRepository(RepositoryProtocol):
    model: Model

    async def get_one(self, id: int | UUID) -> Model:
        return await self.model.get_or_none(id=id)

    async def create(self, data: dict) -> Model:
        return await self.model.create(**data)

    async def update(self, data: dict, id: int | UUID) -> Model:
        row = await self.model.update_from_dict(data)
        await row.save()

        return row

    async def delete(self, id: int | UUID) -> None:
        row = await self.model.get_or_none(id=id)
        await row.delete()
