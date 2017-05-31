from codekatas.countinglines.graph import GraphBuilder
from codekatas.countinglines.line_counter import LineCounter
from codekatas.countinglines.rules import RegexRule
from codekatas.countinglines.states import States, Patterns


def graph_factory():
    blank_rule = RegexRule(Patterns.blank)
    enter_block = RegexRule(Patterns.cb_enter)
    exit_block = RegexRule(Patterns.cb_exit)
    new_line = RegexRule('\n')
    one_line_comment = RegexRule(Patterns.one_line_comment_to_end_line)
    any_character = RegexRule('.')
    builder = GraphBuilder(States)

    # from start:
    builder.add_edge(States.START, States.START, blank_rule)
    builder.add_edge(States.START, States.START, new_line)
    builder.add_edge(States.START, States.START, one_line_comment)
    builder.add_edge(States.START, States.COMMENT_BLOCK, enter_block)
    builder.add_edge(States.START, States.CODE, any_character)

    # comment block
    builder.add_edge(States.COMMENT_BLOCK, States.START, exit_block)
    builder.add_edge(States.COMMENT_BLOCK, States.COMMENT_BLOCK, any_character)
    builder.add_edge(States.COMMENT_BLOCK, States.COMMENT_BLOCK, new_line)

    # from code
    builder.add_edge(States.CODE, States.START, new_line, count=1)
    builder.add_edge(States.CODE, States.START, one_line_comment, count=1)
    builder.add_edge(States.CODE, States.COMMENT_BLOCK_AFTER_CODE, enter_block)
    builder.add_edge(States.CODE, States.CODE, RegexRule(Patterns.string_literal))
    builder.add_edge(States.CODE, States.CODE, any_character)

    # code block after code:
    builder.add_edge(States.COMMENT_BLOCK_AFTER_CODE, States.COMMENT_BLOCK, new_line, count=1)
    builder.add_edge(States.COMMENT_BLOCK_AFTER_CODE, States.CODE, exit_block)
    builder.add_edge(States.COMMENT_BLOCK_AFTER_CODE, States.COMMENT_BLOCK_AFTER_CODE, any_character)
    return builder.build()


def line_counter_factory():
    return LineCounter(graph_factory(), States.START)
