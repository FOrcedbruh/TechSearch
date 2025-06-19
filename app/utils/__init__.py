__all__ = (
    "lifespan",
    "TecDocClient",
    "VehicleType"
)


from app.utils.lifespan.lifespan import lifespan
from app.utils.http_client.tec_doc_client import TecDocClient, VehicleType