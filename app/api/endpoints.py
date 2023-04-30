from fastapi import APIRouter, Depends
from app.api.dependencies import get_token_header

router = APIRouter()


def test_dependency(token: str = Depends(get_token_header)):
    print(token)


@router.get("/test")
def test(token: str = Depends(get_token_header)):
    test_dependency(token)
    return {"message": "This is a test endpoint!"}
