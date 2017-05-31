from unittest import TestCase

from codekatas.countinglines.factory import line_counter_factory


class TestCountCode(TestCase):
    def _check(self, code_text, expected_code_lines):
        counter = line_counter_factory()
        self.assertEqual(expected_code_lines, counter.count(code_text))

    def test_two_code_line(self):
        self._check("System.print('asd');  // comment for this", 1)

    def test_single_line_comment(self):
        self._check("//System.print('asd');", 0)

    def test_single_line_comment_indented(self):
        self._check("   //System.print('asd');", 0)

    def test_empty_line(self):
        self._check("  ", 0)

    def test_code_block_one_line(self):
        self._check("/* comment */", 0)

    def test_code_block_one_line_multi(self):
        self._check("/* comment *//*asdfasdfasdf*/", 0)

    def test_block_in_line_with_code(self):
        self._check('System./*wait*/out./*for*/println/*it*/("Hello/*");', 1)

    def test_code_block_multiline(self):
        lines = """
        /*
        code = 3;
        */
        """
        self._check(lines, 0)

    def test_three_code_lines(self):
        lines = """
        System.print('asd');
        System.print('asd');
        System.print('asd');
        """
        self._check(lines, 3)

    def test_block_after_code(self):
        lines = """
        System.print('asd');/* ili

        */"""
        self._check(lines, 1)

    def test_easy_example_from_codekata(self):
        lines = """
        // This file contains 3 lines of code
         public interface Dave {
           /**
            * count the number of lines in a file
            */
           int countLines(File inFile); // not the real signature!
         }"""
        self._check(lines, 3)

    def test_example_from_codekata(self):
        lines = """
        /*****
        * This is a test program with 5 lines of code
        *  \/* no nesting allowed!
        //*****//***/// Slightly pathological comment ending...

        public class Hello {
           public static final void main(String [] args) { // gotta love Java
             // Say hello
            System./*wait*/out./*for*/println/*it*/("Hello/*");
          }

        }"""
        self._check(lines, 5)
