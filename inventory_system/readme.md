

#Tortoise 和SQLAlchemy的区别
##Tortoise ORM:是一个异步ORM，专门为异步框架（如FAST API,SANIC,TORNADO）设计。它完全支持Python的asyncio,以便在高并发的应用场景下提高性能
##SQLAlchemy:是一个功能强大且灵活的ORM，它可以支持同步和异步操作。在SQLAlchemy 1.4及其后面版本中，SQLAlchemy引入了对异步操作的支持（通过asyncio和asyncpg)， 但这种支持是在其核心同步模型之上进行的扩展，复杂度较高。