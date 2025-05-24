from garmin_fit_sdk import Decoder, Stream


class StrengthWorkout:
    """
    A parser for extracting strength training data from Garmin FIT files.
    """

    def __init__(self, fit_file_path: str):
        """
        Initializes the parser with a FIT file path.
        """
        self._fit_file_path = fit_file_path
        self._messages = None
        self._errors = None

    def parse_strength_sets(self):
        """
        Parses the strength training sets from the FIT file.

        Returns:
            list[dict]: A list of dictionaries, each representing a strength set.
        """
        self._read_fit_file()

        sets = [
            {
                'reps': s.get('repetitions'),
                'weight': s.get('weight'),
                'category': s.get('category'),
                'category_subtype': s.get('category_subtype'),
                'set_type': s.get('set_type')
            }
            for s in self._messages.get('set_mesgs', [])
            if s.get('set_type') == 'active'
        ]

        return sets

    def _read_fit_file(self):
        """
        Reads and decodes the FIT file into messages and errors.
        """
        stream = Stream.from_file(self._fit_file_path)
        decoder = Decoder(stream)
        self._messages, self._errors = decoder.read(
            convert_types_to_strings=True,
            expand_sub_fields=True,
            expand_components=True
        )
