from collections.abc import AsyncIterator

import sqlalchemy as sa
import sqlalchemy.ext.asyncio as saa

from app import config

settings = config.get_settings()


# echo: if True, the Engine will log all statements as well as a repr() of their
# parameter lists to the default log handler, which defaults to sys.stdout for output.
#
# hide_parameters: Boolean, when set to True, SQL statement parameters will not be
# displayed in INFO logging nor will they be formatted into the string representation
# of StatementError objects.
engine = saa.create_async_engine(
    str(settings.db_uri), echo=settings.db_echo, hide_parameters=settings.db_hide_params
)

# https://alembic.sqlalchemy.org/en/latest/naming.html
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
metadata = sa.MetaData(naming_convention=convention)


async def get_db() -> AsyncIterator[saa.AsyncSession]:
    # https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#preventing-implicit-io-when-using-asyncsession
    # expire_on_commit=False will prevent attributes from being expired after commit
    async_session = saa.AsyncSession(engine, expire_on_commit=False)
    try:
        yield async_session
    finally:
        await async_session.close()
