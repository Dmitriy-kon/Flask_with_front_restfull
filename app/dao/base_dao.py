from typing import List

from flask import current_app
from sqlalchemy import desc, select, insert
from sqlalchemy.orm.scoping import scoped_session


class BaseDAO:

    def __init__(self, session: scoped_session, model):
        """Session and model need to be submitted when creating dao object"""
        self.session = session
        self.model = model

    def get_one(self, uid: int) -> object:
        """Get item by id"""
        stmt = select(self.model).where(self.model.id == uid)
        result = self.session.execute(stmt).scalar_one()
        return result

    def get_all(self, page: str = None, sort: bool = False) -> List[object]:
        """Get all items from the db"""

        stmt = select(self.model)

        if sort:
            stmt = stmt.order_by(desc(self.model.year))
        if page:
            stmt = stmt \
                .limit(current_app.config.get('ITEMS_PER_PAGE')) \
                .offset(page * current_app.config.get('ITEMS_PER_PAGE') - current_app.config.get('ITEMS_PER_PAGE'))

        result = self.session.scalars(stmt).all()

        return result

    def create(self, data: dict) -> object:
        """Add item to the database"""
        item = self.model(**data)
        self.session.add(item)
        self.session.commit()
        return item

    def delete(self, uid):
        item = self.get_one(uid)
        self.session.delete(item)
        self.session.commit()
