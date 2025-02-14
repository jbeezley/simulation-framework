from math import ceil
from typing import Iterator

import attr

from simulation.state import State
from simulation.validation import context as validation_context


def initialize(state: State) -> State:
    """Initialize a simulation state."""
    for m in state.config.modules:
        with validation_context(f'{m.name} (initialization)'):
            state = m.initialize(state)

    # run validation after all initialization is done otherwise validation
    # could fail on a module's private state before it can initialize itself
    with validation_context('global initialization'):
        attr.validate(state)
    return state


def advance(state: State, target_time: float) -> Iterator[State]:
    """Advance a simulation to the given target time."""
    dt = state.config.getfloat('simulation', 'time_step')
    n_steps = ceil((target_time - state.time) / dt)
    initial_time = state.time

    for i in range(n_steps):
        previous_time = state.time
        state.time = min(initial_time + (i + 1) * dt, target_time)

        for m in state.config.modules:
            with validation_context(m.name):
                state = m.advance(state, previous_time)
                attr.validate(state)

        yield state
