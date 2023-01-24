### Make and set a value( float ) for control rig
value = unreal.RigHierarchy.make_control_value_from_float(0.0)
unreal.RigHierarchy.set_control_value(ctrl_key, value, unreal.RigControlValueType.INITIAL) 
