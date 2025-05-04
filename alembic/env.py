from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os

from app.models import Base

config = context.config
fileConfig(config.config_file_name)

# Configuração para usar o banco de dados do Docker
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL", "mysql+pymysql://user:password@db/estoque_db"))

target_metadata = Base.metadata
