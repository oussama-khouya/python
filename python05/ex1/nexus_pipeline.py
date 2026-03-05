from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


# ─── BASE CLASS ────────────────────────────────────────────
class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        result = []
        for item in data_batch:
            if criteria in str(item):
                result.append(item)
        return result

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count
        }

    def format_output(self, result: str) -> str:
        pass


# ─── SENSOR STREAM ─────────────────────────────────────────
