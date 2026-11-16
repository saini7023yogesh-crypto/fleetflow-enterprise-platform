import os

os.environ.setdefault("DATABASE_URL", "sqlite:///./fleetflow_local.db")

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app
from app.models.order import Order

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL", "sqlite:///./fleetflow_test.db")

connect_args = (
    {"check_same_thread": False} if TEST_DATABASE_URL.startswith("sqlite") else {}
)

engine = create_engine(TEST_DATABASE_URL, connect_args=connect_args)

TestingSessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    join_transaction_mode="create_savepoint",
)


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    connection = engine.connect()
    transaction = connection.begin()

    TestingSession = sessionmaker(
        bind=connection,
        autoflush=False,
        autocommit=False,
        join_transaction_mode="create_savepoint",
    )

    def override_get_db():
        db = TestingSession()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
    transaction.rollback()
    connection.close()
