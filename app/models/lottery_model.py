from sqlalchemy import Column, Integer, DateTime, Text
from datetime import datetime, timedelta
from pydantic import BaseModel
from typing import List
import json

from app.db.database import Base


class Lottery(Base):
    __tablename__ = "lottery"
    id = Column(Integer, primary_key=True, index=True)
    generated_numbers = Column(Text, nullable=False)
    generated_time = Column(DateTime, nullable=False, default=datetime.now())
    start_date = Column(
        DateTime, nullable=False,
        default=(
            datetime.now() - timedelta(
                days=(datetime.now()).weekday()
            )
        ).date(),
        unique=True
    )
    end_date = Column(
        DateTime, nullable=False,
        default=(
            datetime.now() - timedelta(
                days=(datetime.now()).weekday()
            ) + timedelta(days=6)
        ).date(),
        unique=True
    )
    total_money = Column(Integer, nullable=False)

    @property
    def generated_numbers_list(self):
        return json.loads(self.generated_numbers)

    @generated_numbers_list.setter
    def generated_numbers_list(self, value):
        self.generated_numbers = json.dumps(value)


class User_Lottery_Record(Base):
    __tablename__ = "user_lottery_record"
    id = Column(Integer, primary_key=True, index=True)
    lottery_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    selected_numbers = Column(Text, nullable=False)
    selected_time = Column(DateTime, nullable=False, default=datetime.now())
    start_date = Column(
        DateTime, nullable=False,
        default=(
            datetime.now() - timedelta(
                days=(datetime.now()).weekday()
            )
        ).date(),
        unique=True
    )

    @property
    def selected_numbers_list(self):
        return json.loads(self.selected_numbers)

    @selected_numbers_list.setter
    def selected_numbers_list(self, value):
        self.selected_numbers = json.dumps(value)


class Compera(BaseModel):
    common_numbers: List[int]
    match: int


class ComperaResponse(BaseModel):
    common_numbers: List[int]
    generated_time: datetime
    match: int


class LotteryResponse(BaseModel):
    lottery_id: int
    user_result: List[ComperaResponse]
