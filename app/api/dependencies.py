from fastapi import Header, HTTPException


async def get_token_header(token: str = Header(None)):
    if token is None:
        raise HTTPException(status_code=400, detail="No token provided")
    if len(token) != 64:
        raise HTTPException(status_code=400, detail="Token length must be 64")
    return token
