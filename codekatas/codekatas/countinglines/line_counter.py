from codekatas.countinglines.graph import Graph
from codekatas.countinglines.states import States


class LineCounter(object):
    def __init__(self, graph: Graph, start_state: States) -> None:
        super().__init__()
        self._start_state = start_state
        self._graph = graph

    def count(self, code_text):
        state = self._start_state
        text = code_text
        if text[-1] != '\n':
            text += '\n'
        counter = 0
        while text:
            # print('In state {} text: {}...'.format(state, repr(text[:20])))
            for edge in self._graph.iter_edges(state):
                rule = edge.data
                if rule.applies(text):
                    text = rule.apply(text)
                    state = edge.to
                    counter += edge.count
                    # if edge.count:
                        # print('Adding ', edge.count)
                    break
            else:
                raise ValueError("No valid state from {} with text {}...".format(state, repr(text[:5])))
        return counter
