import attr
import pytest

from simulation.validation import context, ValidationError


def test_validate_initial_state(config, state):
    attr.validate(state)


def test_validation_context(config):
    with pytest.raises(ValidationError) as excinfo, \
            context('test context'):
        raise ValidationError('')

    error = excinfo.value
    assert 'After execution of "test context":' in str(error)
