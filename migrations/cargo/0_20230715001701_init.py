from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "cargo" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "cargo_type" VARCHAR(255) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "rate" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "date" DATE NOT NULL,
    "rate" DOUBLE PRECISION NOT NULL,
    "cargo_type_id" INT NOT NULL REFERENCES "cargo" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
