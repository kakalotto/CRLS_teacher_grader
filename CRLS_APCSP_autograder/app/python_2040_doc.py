def docs_feedback_python_2040(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)

    test1a = exact_answer('1a ', [r'1a\. .+? tabledata \s* pretty \s good \s grade .+? tabledata .+? 2a\.'], text, points=2)
    test2a = exact_answer('2a ', [r'2a\. .+? tabledata \s*  .+? tabledata .+? 3a\.'], text, points=3)
    test3a = exact_answer('3a ', [r'3a\. .+? tabledata \s* .+? Chec'], text, points=3)

    tests.extend([test1a, test2a, test3a])
    return tests
