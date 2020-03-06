def docs_feedback_hexadecimal_numbers_v4(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()

    text = get_text(link)

    test1a = exact_answer('1a. B  ', [r'1a\. .*? tabledata .*? 1011 .*? 2a\.'], text, points=3)
    test2a = exact_answer('2a. 3E ', [r'2a\. .*? tabledata .*? 11  \s* 1110 .*? 3a\.'], text, points=3)
    test3a = exact_answer('3a. D6 ', [r'3a\. .*? tabledata .*? 1101 \s* 0110 .*?  4a\.'], text, points=3)
    test4a = exact_answer('4a. CC1', [r'4a\. .*? tabledata .*? 1100 \s* 1100 \s* 0001 .*? 5a\.'], text, points=3)
    test5a = exact_answer('5a. ABC9', [r'5a\. .*? tabledata .*? 1010 \s* 1011 \s* 1100 \s* 1001 \s* .*? example'], text, points=3)
    test6a = exact_answer('6a. 0010', [r'6a\. .*? tabledata .*? 2 .*? 7a\.'], text, points=3)
    test7a = exact_answer('7a. 1110', [r'7a\. .*? tabledata .*? e .*? 8a\.'], text, points=3)
    test8a = exact_answer('8a. 0111 1010', [r'8a\. .*? tabledata .*? 7 \s* a .*? 9a\.'], text, points=3)
    test9a = exact_answer('9a. 1110 0111', [r'9a\. .*? tabledata .*?  e \s* 7 .*? 10a\.'], text, points=3)
    test10a = exact_answer('10a. 010101011110', [r'10a\. .*? tabledata .*? 5 \s* 5 \s* e .*?  11a\.'], text,
                           points=3)
    test11a = exact_answer('11a. 101101111111', [r'11a\. .*? tabledata .*? b \s* 7 \s* f .*? check \s your \s work'], text, points=3)
    tests.extend([test1a, test2a, test3a, test4a, test5a, test6a, test7a, test8a, test9a, test10a, test11a, ])
    return tests

