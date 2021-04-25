from typing import Any, Union

from asyncpg import Record

from ghs.model.database.database import Database


class Pager:

    __slots__ = ("dbh", "offset", "limit", "total_pages", "conn_creds")

    def __init__(self, conn_creds: Union[dict[str, str], None] = None) -> None:
        self.limit: int = 20
        self.offset: int = 0
        # self.dbh: Union[Database, None] = None
        self.total_pages: Union[int, Record, None] = None
        self.conn_creds: Union[dict[str, str], None] = conn_creds

    async def _set_dbh(self) -> None:
        self.dbh: Database = await Database.get_database_handle()
        if isinstance(self.conn_creds, dict):
            self.dbh = await Database.get_database_handle(self.conn_creds)

    async def page(self) -> Any:

        await self._set_dbh()

        self.total_pages = await self.dbh.read("SELECT count(*) FROM project")
        self.total_pages = int(self.total_pages[0]["count"]) // self.limit

        for row in await self.dbh.read(
            f"""
                SELECT add_time, project.name, description, pro_lang.name as language, url,
                initial_stars, current_stars, initial_fork_count, current_fork_count
                FROM project
                JOIN pr_pl ON pr_pl.pr_id = project.project_id
                JOIN pro_lang ON pro_lang.language_id = pr_pl.pl_id
                ORDER BY current_stars DESC
                LIMIT {self.limit}
                OFFSET {self.offset}
            """.strip()
        ):
            yield row

        self.offset += 20
