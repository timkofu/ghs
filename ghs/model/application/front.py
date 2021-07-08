from typing import Any, cast

from asyncpg.connection import Connection

from ghs.model.infrastructure.repository.repository import Repository


class Pager:

    __slots__ = ("dbh", "limit", "conn_creds")

    def __init__(self, conn_creds: dict[str, str]) -> None:
        self.dbh: Connection
        self.limit: int = 100
        self.conn_creds: dict[str, str] = {}

    async def _set_dbh(self) -> None:
        self.dbh = cast(
            Connection, await Repository.get_database_handle(self.conn_creds)
        )

    async def page(self) -> Any:

        await self._set_dbh()

        for row in await self.dbh.read(  # type: ignore
            f"""
                SELECT add_time, project.name, description, pro_lang.name as language, url,
                initial_stars, current_stars, initial_fork_count, current_fork_count
                FROM project
                JOIN pr_pl ON pr_pl.pr_id = project.project_id
                JOIN pro_lang ON pro_lang.language_id = pr_pl.pl_id
                ORDER BY current_stars DESC
                LIMIT {self.limit}
            """.strip()
        ):
            yield row
