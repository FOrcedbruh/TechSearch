from pydantic import BaseModel, Field



class ManufacturerModel(BaseModel):
    id: int = Field(alias="MFA_ID")
    brand: str = Field(alias="MFA_BRAND")
    models_count: int = Field(alias="MFA_MODELS_COUNT")

    class Config:
        extra = True