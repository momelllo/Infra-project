from pydantic import BaseModel, field_validator
from typing import Literal

class MachineSchema(BaseModel):
    name: str
    os: Literal["CentOS", "Ubuntu"]
    cpu: int
    ram: float
    storage: float

    @field_validator("cpu")
    def cpu_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("CPU cores must be greater than 0")
        return value

    @field_validator("ram")
    def ram_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("RAM must be greater than 0")
        return value

    @field_validator("storage")
    def storage_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Storage must be greater than 0")
        return value