from pydantic import BaseModel


class SignUpRequest(BaseModel):
    username: str
    password: str


class SignInRequest(BaseModel):
    username: str
    password: str


class CredentialsResponse(BaseModel):
    access_token: str
    refresh_token: str
