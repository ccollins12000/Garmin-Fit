from garmin_fit_sdk import Decoder, Stream


exercise_lookup = {
'push_up': {
    0: "chest_press_with_band",
    1: "alternating_staggered_push_up",
    2: "weighted_alternating_staggered_push_up",
    3: "alternating_hands_medicine_ball_push_up",
    4: "weighted_alternating_hands_medicine_ball_push_up",
    5: "bosu_ball_push_up",
    6: "weighted_bosu_ball_push_up",
    7: "clapping_push_up",
    8: "weighted_clapping_push_up",
    9: "close_grip_medicine_ball_push_up",
    10: "weighted_close_grip_medicine_ball_push_up",
    11: "close_hands_push_up",
    12: "weighted_close_hands_push_up",
    13: "decline_push_up",
    14: "weighted_decline_push_up",
    15: "diamond_push_up",
    16: "weighted_diamond_push_up",
    17: "explosive_crossover_push_up",
    18: "weighted_explosive_crossover_push_up",
    19: "explosive_push_up",
    20: "weighted_explosive_push_up",
    21: "feet_elevated_side_to_side_push_up",
    22: "weighted_feet_elevated_side_to_side_push_up",
    23: "hand_release_push_up",
    24: "weighted_hand_release_push_up",
    25: "handstand_push_up",
    26: "weighted_handstand_push_up",
    27: "incline_push_up",
    28: "weighted_incline_push_up",
    29: "isometric_explosive_push_up",
    30: "weighted_isometric_explosive_push_up",
    31: "judo_push_up",
    32: "weighted_judo_push_up",
    33: "kneeling_push_up",
    34: "weighted_kneeling_push_up",
    35: "medicine_ball_chest_pass",
    36: "medicine_ball_push_up",
    37: "weighted_medicine_ball_push_up",
    38: "one_arm_push_up",
    39: "weighted_one_arm_push_up",
    40: "weighted_push_up",
    41: "push_up_and_row",
    42: "weighted_push_up_and_row",
    43: "push_up_plus",
    44: "weighted_push_up_plus",
    45: "push_up_with_feet_on_swiss_ball",
    46: "weighted_push_up_with_feet_on_swiss_ball",
    47: "push_up_with_one_hand_on_medicine_ball",
    48: "weighted_push_up_with_one_hand_on_medicine_ball",
    49: "shoulder_push_up",
    50: "weighted_shoulder_push_up",
    51: "single_arm_medicine_ball_push_up",
    52: "weighted_single_arm_medicine_ball_push_up",
    53: "spiderman_push_up",
    54: "weighted_spiderman_push_up",
    55: "stacked_feet_push_up",
    56: "weighted_stacked_feet_push_up",
    57: "staggered_hands_push_up",
    58: "weighted_staggered_hands_push_up",
    59: "suspended_push_up",
    60: "weighted_suspended_push_up",
    61: "swiss_ball_push_up",
    62: "weighted_swiss_ball_push_up",
    63: "swiss_ball_push_up_plus",
    64: "weighted_swiss_ball_push_up_plus",
    65: "t_push_up",
    66: "weighted_t_push_up",
    67: "triple_stop_push_up",
    68: "weighted_triple_stop_push_up",
    69: "wide_hands_push_up",
    70: "weighted_wide_hands_push_up",
    71: "parallette_handstand_push_up",
    72: "weighted_parallette_handstand_push_up",
    73: "ring_handstand_push_up",
    74: "weighted_ring_handstand_push_up",
    75: "ring_push_up",
    76: "weighted_ring_push_up",
    77: "push_up",
    78: "pilates_pushup"
},
'pull_up': {
    0: "banded_pull_ups",
    1: "30_degree_lat_pulldown",
    2: "band_assisted_chin_up",
    3: "close_grip_chin_up",
    4: "weighted_close_grip_chin_up",
    5: "close_grip_lat_pulldown",
    6: "crossover_chin_up",
    7: "weighted_crossover_chin_up",
    8: "ez_bar_pullover",
    9: "hanging_hurdle",
    10: "weighted_hanging_hurdle",
    11: "kneeling_lat_pulldown",
    12: "kneeling_underhand_grip_lat_pulldown",
    13: "lat_pulldown",
    14: "mixed_grip_chin_up",
    15: "weighted_mixed_grip_chin_up",
    16: "mixed_grip_pull_up",
    17: "weighted_mixed_grip_pull_up",
    18: "reverse_grip_pulldown",
    19: "standing_cable_pullover",
    20: "straight_arm_pulldown",
    21: "swiss_ball_ez_bar_pullover",
    22: "towel_pull_up",
    23: "weighted_towel_pull_up",
    24: "weighted_pull_up",
    25: "wide_grip_lat_pulldown",
    26: "wide_grip_pull_up",
    27: "weighted_wide_grip_pull_up",
    28: "burpee_pull_up",
    29: "weighted_burpee_pull_up",
    30: "jumping_pull_ups",
    31: "weighted_jumping_pull_ups",
    32: "kipping_pull_up",
    33: "weighted_kipping_pull_up",
    34: "l_pull_up",
    35: "weighted_l_pull_up",
    36: "suspended_chin_up",
    37: "weighted_suspended_chin_up",
    38: "pull_up"
},
'triceps_extension': {
    0: "bench_dip",
    1: "weighted_bench_dip",
    2: "body_weight_dip",
    3: "cable_kickback",
    4: "cable_lying_triceps_extension",
    5: "cable_overhead_triceps_extension",
    6: "dumbbell_kickback",
    7: "dumbbell_lying_triceps_extension",
    8: "ez_bar_overhead_triceps_extension",
    9: "incline_dip",
    10: "weighted_incline_dip",
    11: "incline_ez_bar_lying_triceps_extension",
    12: "lying_dumbbell_pullover_to_extension",
    13: "lying_ez_bar_triceps_extension",
    14: "lying_triceps_extension_to_close_grip_bench_press",
    15: "overhead_dumbbell_triceps_extension",
    16: "reclining_triceps_press",
    17: "reverse_grip_pressdown",
    18: "reverse_grip_triceps_pressdown",
    19: "rope_pressdown",
    20: "seated_barbell_overhead_triceps_extension",
    21: "seated_dumbbell_overhead_triceps_extension",
    22: "seated_ez_bar_overhead_triceps_extension",
    23: "seated_single_arm_overhead_dumbbell_extension",
    24: "single_arm_dumbbell_overhead_triceps_extension",
    25: "single_dumbbell_seated_overhead_triceps_extension",
    26: "single_leg_bench_dip_and_kick",
    27: "weighted_single_leg_bench_dip_and_kick",
    28: "single_leg_dip",
    29: "weighted_single_leg_dip",
    30: "static_lying_triceps_extension",
    31: "suspended_dip",
    32: "weighted_suspended_dip",
    33: "swiss_ball_dumbbell_lying_triceps_extension",
    34: "swiss_ball_ez_bar_lying_triceps_extension",
    35: "swiss_ball_ez_bar_overhead_triceps_extension",
    36: "tabletop_dip",
    37: "weighted_tabletop_dip",
    38: "triceps_extension_on_floor",
    39: "triceps_pressdown",
    40: "weighted_dip"
},
'shoulder_press': {
    0: "alternating_dumbbell_shoulder_press",
    1: "arnold_press",
    2: "barbell_front_squat_to_push_press",
    3: "barbell_push_press",
    4: "barbell_shoulder_press",
    5: "dead_curl_press",
    6: "dumbbell_alternating_shoulder_press_and_twist",
    7: "dumbbell_hammer_curl_to_lunge_to_press",
    8: "dumbbell_push_press",
    9: "floor_inverted_shoulder_press",
    10: "weighted_floor_inverted_shoulder_press",
    11: "inverted_shoulder_press",
    12: "weighted_inverted_shoulder_press",
    13: "one_arm_push_press",
    14: "overhead_barbell_press",
    15: "overhead_dumbbell_press",
    16: "seated_barbell_shoulder_press",
    17: "seated_dumbbell_shoulder_press",
    18: "single_arm_dumbbell_shoulder_press",
    19: "single_arm_step_up_and_press",
    20: "smith_machine_overhead_press",
    21: "split_stance_hammer_curl_to_press",
    22: "swiss_ball_dumbbell_shoulder_press",
    23: "weight_plate_front_raise",
    28: "dumbell_shoulder_press"
},
'lateral_raise': {
    0: "45_degree_cable_external_rotation",
    1: "alternating_lateral_raise_with_static_hold",
    2: "bar_muscle_up",
    3: "bent_over_lateral_raise",
    4: "cable_diagonal_raise",
    5: "cable_front_raise",
    6: "calorie_row",
    7: "combo_shoulder_raise",
    8: "dumbbell_diagonal_raise",
    9: "dumbbell_v_raise",
    10: "front_raise",
    11: "leaning_dumbbell_lateral_raise",
    12: "lying_dumbbell_raise",
    13: "muscle_up",
    14: "one_arm_cable_lateral_raise",
    15: "overhand_grip_rear_lateral_raise",
    16: "plate_raises",
    17: "ring_dip",
    18: "weighted_ring_dip",
    19: "ring_muscle_up",
    20: "weighted_ring_muscle_up",
    21: "rope_climb",
    22: "weighted_rope_climb",
    23: "scaption",
    24: "seated_lateral_raise",
    25: "seated_rear_lateral_raise",
    26: "side_lying_lateral_raise",
    27: "standing_lift",
    28: "suspended_row",
    29: "underhand_grip_rear_lateral_raise",
    30: "wall_slide",
    31: "weighted_wall_slide",
    32: "arm_circles",
    33: "shaving_the_head"
},
'flye': {
    0: "cable_crossover",
    1: "decline_dumbbell_flye",
    2: "dumbbell_flye",
    3: "incline_dumbbell_flye",
    4: "kettlebell_flye",
    5: "kneeling_rear_flye",
    6: "single_arm_standing_cable_reverse_flye",
    7: "swiss_ball_dumbbell_flye",
    8: "arm_rotations",
    9: "hug_a_tree"
}






 }


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
                'category': s.get('category',[None])[0],
                'category_subtype': exercise_lookup.get(s.get('category',[None])[0] , {}).get(s.get('category_subtype',[None])[0]),
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
            expand_sub_fields=True,
            expand_components=True
        )
