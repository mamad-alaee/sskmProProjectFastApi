from fastapi import FastAPI
from initiators.db_initiator import init_db
from initiators.setRoutes import setRoutes
from initiators.inti_data import init_base_data

originalApp = FastAPI(
    description="this is sskm project",
    title="sskm project",
    version="0.1.0"
)

init_db()
init_base_data()
setRoutes(originalApp)






