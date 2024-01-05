from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface import MIDI_NOTE_TYPE, MIDI_CC_TYPE, ElementsBase

class Elements(ElementsBase):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self.add_button(25, 'Left_Button', msg_type=MIDI_NOTE_TYPE)
        self.add_button(26, 'Right_Button', msg_type=MIDI_NOTE_TYPE)
        self.add_modifier_button(27, 'Shift_Button', msg_type=MIDI_NOTE_TYPE)
        self.add_encoder_matrix([
            (16, 20, 24, 28, 46, 50, 54, 58),
             (17, 21, 25, 29, 47, 51, 55, 59)],
            'encoders', msg_type=MIDI_CC_TYPE)
        self.add_submatrix((self.encoders), 'Send_A_Controls', rows=(0, 1))
        self.add_submatrix((self.encoders), 'Send_B_Controls', rows=(1, 2))
        self.add_encoder_matrix([range(18, 31, 4)], 'Pan_Controls', msg_type=MIDI_CC_TYPE)
        self.add_button_matrix([range(1, 23, 3)], 'Mute_Buttons', msg_type=MIDI_NOTE_TYPE)
        self.add_button_matrix([range(2, 24, 3)], 'Solo_Buttons', msg_type=MIDI_NOTE_TYPE)
        self.add_button_matrix([range(3, 25, 3)], 'Rec_Arm_Buttons', msg_type=MIDI_NOTE_TYPE)
        self.add_encoder_matrix([(*range(19, 32, 4), *range(49, 62, 4))], 'Volume_Controls', msg_type=MIDI_CC_TYPE)
        self.add_encoder(62, 'Master_Volume_Control', msg_type=MIDI_CC_TYPE)
