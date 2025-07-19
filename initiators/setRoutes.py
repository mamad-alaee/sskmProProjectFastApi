from routers.userRouter import userRouter
from routers.authRouter import authRouter

def setRoutes(app):
    app.include_router(userRouter)
    app.include_router(authRouter)