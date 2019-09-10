def docs_feedback_hex_minilab(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)
    test1a = exact_answer('question 1a', [r'1a .+? tabledata \s* 5.+ tabledata \s*? 3 [^a-z] '], text, points=2)
    test1b = exact_answer('question 1b', [r'1b .+? tabledata \s* c .+ tabledata \s*?  12 [^a-z]'], text, points=2)
    test1c = exact_answer('question 1c', [r'1c .+? tabledata \s* a4 .+ tabledata \s*? 164 [^a-z]'], text, points=2)
    test1d = exact_answer('question 1d', [r'1d .+? tabledata \s* 2f .+ tabledata \s*? 47 [^a-z]'], text, points=2)
    test2a = exact_answer('question 2a', [r'2a. .+? tabledata \s* 1f .+ tabledata \s* 31'], text, points=2)
    test2b = exact_answer('question 2b', [r'2b. .+? tabledata \s* 8 .+ tabledata \s* 8'], text, points=2)
    test2c = exact_answer('question 2c', [r'2c. .+? tabledata \s* 51 .+ tabledata \s* 81'], text, points=2)
    test2d = exact_answer('question 2d', [r'2d. .+? tabledata \s* FF .+ tabledata \s* 255'], text, points=2)
    tests.extend([test1a, test1b, test1c, test1d, test2a, test2b, test2c, test2d, ])
    return tests
