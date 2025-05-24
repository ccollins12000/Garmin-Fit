from garmin_fit_sdk import Decoder, Stream
from typing import Optional, Dict, List


class RunningWorkout:
    """
    A class to parse and represent a running workout from a Garmin FIT file.
    """

    def __init__(self, fit_file_path: str):
        """
        Initialize the RunningWorkout parser.

        Args:
            fit_file_path (str): Full path to the Garmin FIT file.
        """
        self._fit_file_path = fit_file_path
        self._messages: Optional[Dict] = None
        self._errors: Optional[List] = None
        self._metrics: Optional[Dict] = None

    def parse(self) -> None:
        """
        Reads and decodes the FIT file, storing session metrics.
        """
        self._read_fit_file()
        self._metrics = self._extract_session_metrics()

    def get_metrics(self) -> Optional[Dict]:
        """
        Returns:
            dict: A dictionary of average session metrics, or None if not yet parsed.
        """
        return self._metrics

    def get_errors(self) -> Optional[List]:
        """
        Returns:
            list: Any decoding errors encountered.
        """
        return self._errors

    def _read_fit_file(self) -> None:
        """
        Internal method to read and decode the FIT file.
        """
        stream = Stream.from_file(self._fit_file_path)
        decoder = Decoder(stream)
        self._messages, self._errors = decoder.read()

    def _extract_session_metrics(self) -> Optional[Dict]:
        """
        Extracts average metrics from the session messages.

        Returns:
            dict: A dictionary of selected session metrics, or None if missing.
        """
        session_mesgs = self._messages.get('session_mesgs', [])
        if not session_mesgs:
            return None

        # Assuming one session per file — use the first message
        message = session_mesgs[0]

        return {
            'avg_cadence': message.get('avg_cadence'),
            'avg_heart_rate': message.get('avg_heart_rate'),
            'avg_vertical_ratio': message.get('avg_vertical_ratio'),
            'avg_power': message.get('avg_power'),
            'avg_speed': message.get('avg_speed'),
            'enhanced_avg_speed': message.get('enhanced_avg_speed'),
            'total_elapsed_time': message.get('total_elapsed_time'),
            'total_distance': message.get('total_distance')
        }