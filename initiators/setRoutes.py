from routers.userRouter import userRouter
from routers.authRouter import authRouter
from routers.errorRouter import error_router

def setRoutes(app):
    app.include_router(userRouter)
    app.include_router(error_router)
    app.include_router(authRouter)