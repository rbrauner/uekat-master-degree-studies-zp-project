from fastapi import FastAPI
from src.app.prime.prime import prime_router
from src.app.picture_invert.picture_invert import picture_invert_router
from src.app.current_time.current_time import current_time_router

app = FastAPI(
    title="ue-nsi-zp-project",
    description="""
    Authorize data:

    - Enabled user:
    Login: test
    Password: zaq1@WSX

    - Disabled user:
    Login: test2
    Password: cde3$RFV
    """,
    version="0.0.1",
    license_info={
        "name": "MIT",
        "url": "https://github.com/rbrauner/uekat-studies-zp-project/blob/main/LICENSE",
    },
)
app.include_router(prime_router)
app.include_router(picture_invert_router)
app.include_router(current_time_router)
