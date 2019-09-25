def docs_feedback_python_2050(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)

    test1a = exact_answer('1a ', [r'1a\. .+? tabledata \s* [a-zA-Z] .+? tabledata .+? 1b\.'], text, points=1)
    test2a = exact_answer('2a ', [r'2a\. .+? tabledata \s* [a-zA-Z] .+? tabledata .+? 2b\.'], text, points=1)
    test3a = exact_answer('3a ', [r'3a\. .+? tabledata \s* [a-zA-Z] .+? tabledata .+? 3b\.'], text, points=1)
    test4a = exact_answer('4a ', [r'4a\. .+? tabledata .+? [a-zA-Z] .+? tabledata .+? 4b\.'], text, points=1)
    test1b = exact_answer('1b ', [r'1b\. .+? tabledata \s* a \s* d \s* .+? tabledata .+? 2a\.'], text, points=1)
    test2b = exact_answer('2b ', [r'2b\. .+? tabledata \s* c .+? tabledata .+? 3a\.'], text, points=1)
    test3b = exact_answer('3b ', [r'3b\. .+? tabledata \s* e .+? tabledata .+? 4a\.'], text, points=1)
    test4b = exact_answer('4b ', [r'4b\. .+? tabledata .+? a .+? b.+? c .+? haha .+? e .+? check'], text, points=1)

    tests.extend([test1a, test1b, test2a, test2b, test3a, test3b, test4a, test4b])
    return tests

