from fastapi import APIRouter
from starlette.responses import RedirectResponse

router = APIRouter()


@router.get('/', summary='Redirect home page to docs', include_in_schema=False)
def router_docs_redirect():
    return RedirectResponse(url='/docs')
