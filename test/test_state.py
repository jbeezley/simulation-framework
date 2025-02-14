from tempfile import TemporaryFile

from simulation.state import State


def test_save_state(state: State):
    with TemporaryFile('wb') as f:
        state.save(f)
        assert f.tell() > 0


def test_serialize_state(state: State):
    serialized = state.serialize()
    assert isinstance(serialized, bytes)
    assert len(serialized) > 0


def test_load_state(state: State):
    state.advection.concentration[:] = 1
    new_state = state.load(state.serialize())
    assert new_state is not state
    assert (new_state.advection.concentration == state.advection.concentration).all()
