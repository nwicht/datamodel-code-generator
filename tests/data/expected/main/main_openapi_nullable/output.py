# generated by datamodel-codegen:
#   filename:  nullable.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import AnyUrl, BaseModel, Field


class Cursors(BaseModel):
    prev: str
    next: Optional[str] = 'last'
    index: float
    tag: Optional[str] = None


class TopLevel(BaseModel):
    cursors: Cursors


class Info(BaseModel):
    name: str


class User(BaseModel):
    info: Info


class Api(BaseModel):
    apiKey: Optional[str] = Field(
        None, description='To be used as a dataset parameter value'
    )
    apiVersionNumber: Optional[str] = Field(
        None, description='To be used as a version parameter value'
    )
    apiUrl: Optional[AnyUrl] = Field(
        None, description="The URL describing the dataset's fields"
    )
    apiDocumentationUrl: Optional[AnyUrl] = Field(
        None, description='A URL to the API console for each API'
    )


class Apis(BaseModel):
    __root__: Optional[List[Api]] = None


class EmailItem(BaseModel):
    author: str
    address: str = Field(..., description='email address')
    description: Optional[str] = 'empty'
    tag: Optional[str] = None


class Email(BaseModel):
    __root__: List[EmailItem]


class Id(BaseModel):
    __root__: int


class Description(BaseModel):
    __root__: Optional[str] = 'example'


class Name(BaseModel):
    __root__: Optional[str] = None


class Tag(BaseModel):
    __root__: str


class Notes(BaseModel):
    comments: List[str] = Field(default_factory=list)
