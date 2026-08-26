from logging.config import fileConfig
import sys
from pathlib import Path

from alembic import context

from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.engine import create_engine

# Permite importar nuestra aplicación desde la raíz del proyecto.
BACKEND_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_DIR))

from app.core.config import settings
from app.db.database import Base
from app import models


config = context.config

# Configuración de logging de Alembic.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# Metadata de SQLAlchemy utilizada por Alembic
# para detectar cambios en nuestros modelos.
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Ejecuta las migraciones en modo offline."""

    context.configure(
        url=settings.database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Ejecuta las migraciones conectándose a PostgreSQL."""

    connectable = create_engine(
        settings.database_url,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        run_migrations_with_connection(connection)

    connectable.dispose()


def run_migrations_with_connection(connection: Connection) -> None:
    """Configura Alembic utilizando una conexión existente."""

    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()