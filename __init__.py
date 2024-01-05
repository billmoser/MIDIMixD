from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface import ControlSurfaceSpecification, create_control_surface, create_skin
from ableton.v3.control_surface.capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, SCRIPT, \
    controller_id, inport, outport
from .elements import Elements
from .mappings import create_mappings

def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(vendor_id=2536, product_ids=[49], model_name=['MIDI Mix']), 
        PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT]), outport(props=[NOTES_CC, SCRIPT])]}

def create_instance(c_instance):
    return create_control_surface(
        name='MIDI Mix',
        specification=Specification,
        c_instance=c_instance)


class Specification(ControlSurfaceSpecification):
    elements_type = Elements
    control_surface_skin = create_skin()
    num_tracks = 8
    num_scenes = 1
    include_returns = True
    identity_response_id_bytes = (71, 49, 0, 25)
    create_mappings_function = create_mappings
