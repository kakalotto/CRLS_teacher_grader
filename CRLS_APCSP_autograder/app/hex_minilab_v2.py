def docs_feedback_hex_minilab_v2(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)
    test1a = exact_answer('question 1a', [r'1a\. .*? tabledata .*? 7 .*? tabledata'], text, points=2)
    test1b = exact_answer('question 1b', [r'1b\. .*? tabledata .*? 13 .*? tabledata'], text, points=2)
    test1c = exact_answer('question 1c', [r'1c\. .*? tabledata .*? 166 .*? tabledata'], text, points=2)
    test1d = exact_answer('question 1d', [r'1d\. .*? tabledata .*? 46 .*? tabledata'], text, points=2)
    test2a = exact_answer('question 2a', [r'2a\. .*? tabledata .*? 1e .*? tabledata '], text, points=2)
    test2b = exact_answer('question 2b', [r'2b\. .*? tabledata .*? 7 .*? tabledata'], text, points=2)
    test2c = exact_answer('question 2c', [r'2c\. .*? tabledata .*? 41 .*? tabledata'], text, points=2)
    test2d = exact_answer('question 2d', [r'2d\. .*? tabledata .*? ff .*? tabledata'], text, points=2)

    tests.extend([test1a, test1b, test1c, test1d, test2a, test2b, test2c, test2d, ])
    return tests
