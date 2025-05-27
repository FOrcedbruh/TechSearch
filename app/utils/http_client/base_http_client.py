from abc import ABC, abstractmethod
from typing import Self


class BaseHttpClient(ABC):

    @abstractmethod
    async def __aenter__(self, base_url: str) -> Self: ...


    @abstractmethod
    async def __aexit__(self, *args) -> None: ...