from typing import Any, Union

from ghs.model.database.database import Database


class Pager:

    __slots__ = ("dbh", "limit", "conn_creds")

    def __init__(self, conn_creds: Union[dict[str, str], None] = None) -> None:
        self.limit: int = 100
        # self.dbh: Union[Database, None] = None
        self.conn_creds: Union[dict[str, str], None] = conn_creds

    async def _set_dbh(self) -> None:
        self.dbh: Database = await Database.get_database_handle()
        if isinstance(self.conn_creds, dict):
            self.dbh = await Database.get_database_handle(self.conn_creds)

    async def page(self) -> Any:

        await self._set_dbh()

        for row in await self.dbh.read(
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
