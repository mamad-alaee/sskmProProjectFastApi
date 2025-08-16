from fastapi import FastAPI,HTTPException
from initiators.db_initiator import init_db
from initiators.setRoutes import setRoutes
from initiators.inti_data import init_base_data
from initiators.init_logger import create_logger, log_exception
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from initiators.init_env import load_env_var
from initiators.init_job import copy_files_every_5s,copy_files,say_hello_5s,say_hello_5Am,say_hello_mon_8Am


originalApp = FastAPI(
    description="this is sskm project",
    title="sskm project",
    version="0.1.0"
)

init_db()
init_base_data()
setRoutes(originalApp)
load_env_var()
logger = create_logger(originalApp)
originalApp.middleware("http")(log_exception)
# say_hello_5s()
# say_hello_5Am()
# say_hello_mon_8Am()
copy_files_every_5s()

# origins = [
#     "https://your-frontend-domain.com"
# ]

# originalApp.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["post","get","put","delete"],
#     allow_headers=["*"],
# )

# @originalApp.middleware("http")
# async def block_dissAlowed_origins(request, call_next):
#     origin = request.headers.get("origin")
#     if origin not in origins:
#         return JSONResponse(status_code=403, content={"message": "Dissallowed origin"})
#     else:
#         response = await call_next(request)
#         return response


