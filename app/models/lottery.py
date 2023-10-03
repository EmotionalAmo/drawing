from pydantic import BaseModel


class LotteryResult(BaseModel):
    id: int
    numbers: str
