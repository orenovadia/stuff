from typing import List


class Edge(object):
    def __init__(self, from_, to, rule=None, count=0):
        super().__init__()
        self.from_ = from_
        self.to = to
        self.data = rule
        self.count = count


class Graph(object):
    def __init__(self, states, state_to_edges):
        super().__init__()
        self.states = states
        self._state_to_edges = state_to_edges

    def iter_edges(self, state: object) -> List[Edge]:
        assert isinstance(state, self.states), state
        return self._state_to_edges.get(state, [])


class GraphBuilder(object):
    def __init__(self, states):
        super().__init__()
        self.states = states
        self._state_to_edges = {state: [] for state in self.states}

    def add_edge(self, from_, to, rule, count=0):
        assert isinstance(from_, self.states), from_
        assert isinstance(to, self.states), to
        self._state_to_edges[from_].append(Edge(from_, to, rule, count))

    def build(self) -> Graph:
        return Graph(self.states, self._state_to_edges)
