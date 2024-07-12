from pydantic import BaseModel


class HTTPExceptionSchemas(BaseModel):
    details: str

    class Config:
        from_attributes = True
