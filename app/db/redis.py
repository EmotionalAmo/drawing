from redis import Redis, ConnectionPool

pool = ConnectionPool(host="127.0.0.1", db=0)


def get_redis():
    db = Redis(
        connection_pool=pool,
        decode_responses=True
    )
    try:
        yield db
    finally:
        db.close()


def close(self):
    pool.disconnect()
