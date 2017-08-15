
from traitlets import (
    Unicode, Int, CInt, Instance, Enum, List, Dict, Float, CFloat,
    Bool, Tuple, Undefined, TraitError,
)

from ipydatawidgets import DataUnion, NDArrayWidget

def Vector2(trait_type=CFloat, default=None, **kwargs):
    if default is None:
        default = [0, 0]
    return List(trait_type, default_value=default, minlen=2, maxlen=2, **kwargs)

def Vector3(trait_type=CFloat, default=None, **kwargs):
    if default is None:
        default = [0, 0, 0]
    return List(trait_type, default_value=default, minlen=3, maxlen=3, **kwargs)

def Vector4(trait_type=CFloat, default=None, **kwargs):
    if default is None:
        default = [0, 0, 0, 0]
    return List(trait_type, default_value=default, minlen=4, maxlen=4, **kwargs)

def Matrix3(trait_type=CFloat, default=None, **kwargs):
    if default is None:
        default = [
            1, 0, 0,
            0, 1, 0,
            0, 0, 1
        ]
    return List(trait_type, default_value=default, minlen=9, maxlen=9, **kwargs)

def Matrix4(trait_type=CFloat, default=None, **kwargs):
    if default is None:
        default = [
            1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1
        ]
    return List(trait_type, default_value=default, minlen=16, maxlen=16, **kwargs)

def Face3(**kwargs):
    return Tuple(CInt(), CInt(), CInt(), Vector3(), Unicode(), CInt(), Tuple(), Tuple())

def Euler(default=None, **kwargs):
    if default is None:
        default = [0, 0, 0, 'XYZ']
    return Tuple(CFloat(), CFloat(), CFloat(), Unicode(), default_value=default, **kwargs)


class WebGLDataUnion(DataUnion):
    def validate(self, obj, value):
        value = super(WebGLDataUnion, self).validate(obj, value)
        array = value.array if isinstance(value, NDArrayWidget) else value

        if array is not Undefined and str(array.dtype) == 'float64':
            if isinstance(value, NDArrayWidget):
                raise TraitError('Cannot use a float64 data widget as a BufferAttribute source.')
            else:
                # 64-bit not supported, coerce to 32-bit
                value = value.astype('float32')
        return value
