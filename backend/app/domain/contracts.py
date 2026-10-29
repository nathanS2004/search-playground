"""Extension points only: no game rules or search algorithms are implemented."""
from dataclasses import dataclass
from typing import Callable, Generic, Hashable, Iterable, Protocol, TypeVar

State = TypeVar("State", bound=Hashable)


@dataclass(frozen=True)
class Transition(Generic[State]):
    state: State
    action: str
    cost: float = 1.0


class SearchProblem(Protocol[State]):
    @property
    def initial_state(self) -> State: ...
    def is_goal(self, state: State) -> bool: ...
    def neighbors(self, state: State) -> Iterable[Transition[State]]: ...


@dataclass(frozen=True)
class SearchLimits:
    max_expansions: int = 100_000
    timeout_seconds: float = 10.0


@dataclass(frozen=True)
class SearchResult(Generic[State]):
    path: tuple[State, ...]
    actions: tuple[str, ...]
    expanded: int
    elapsed_ms: float
    status: str


class Solver(Protocol[State]):
    def solve(self, problem: SearchProblem[State], heuristic: Callable[[State], float], limits: SearchLimits) -> SearchResult[State]: ...
