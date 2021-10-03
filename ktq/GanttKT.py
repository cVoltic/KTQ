# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class GanttKT(Component):
    """A GanttKT component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- tasks (list; required):
    items that will be rendered when this component is rendered.

- title (string; required):
    A title that will be rendered when this component is rendered."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, title=Component.REQUIRED, tasks=Component.REQUIRED, **kwargs):
        self._prop_names = ['id', 'tasks', 'title']
        self._type = 'GanttKT'
        self._namespace = 'ktq'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'tasks', 'title']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['title', 'tasks']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(GanttKT, self).__init__(**args)
