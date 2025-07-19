from fastapi import FastAPI
from initiators.db_initiator import init_db
from initiators.setRoutes import setRoutes


originalApp = FastAPI(
    description="this is sskm project",
    title="sskm project",
    version="0.1.0"
)

init_db()
setRoutes(originalApp)






