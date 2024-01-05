from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface import HIGH_PRIORITY
from ableton.v3.control_surface.mode import MomentaryBehaviour

def create_mappings(control_surface):
    mappings = {}

    # session box display
    mappings['Session'] = dict()

    # needed for session box control
    mappings['Session_Navigation'] = dict(  
        left_button='left_button',
        right_button='right_button')
    
    mappings['Mixer'] = dict(
        pan_controls='pan_controls',
        mute_buttons='mute_buttons',
        solo_buttons='solo_buttons',
        track_select_buttons='rec_arm_buttons',
        volume_controls='volume_controls',
        master_track_volume_control='master_volume_control')

    mappings['Encoder_Modes'] = dict(
        send=dict(component='Mixer', send_a_controls='send_a_controls',
            send_b_controls='send_b_controls'),
        device=dict(component='Device', parameter_controls='encoders'))
    
    
    mappings['Main_Modes'] = dict(
        shift_button='shift_button',

        default=dict(
            modes=[
                dict(component='Session'),
                dict(component='Session_Navigation', priority=HIGH_PRIORITY),
                dict(component='Mixer')]),

        shift=dict(
            modes=[
                dict(component='Session'),
                dict(component='Session_Navigation'),
                dict(component='Mixer'),
                dict(component='Encoder_Modes',
                    send_button='left_button',
                    device_button='right_button',
                    priority=HIGH_PRIORITY)],
            behaviour=(MomentaryBehaviour())))

    return mappings
