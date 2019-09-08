def docs_feedback_hardware_esd_formfactors_cards(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)
    test1a = exact_answer('question 1a', [r'1a .+? tabledata \s* .+? electr .+ static .* discharg .+ 1b'], text, points=5)
    test1b = keyword_and_length('question 1b', [r'[a-zA-Z]+'], text,
                                search_string=r'1b. .+? tabledata (.+) 1c.', min_length=7, points=1)
    test1c1 = exact_answer('question 1c-1', [r'1c. .+? tabledata .+ touch .+ side .+ 2.'], text, points=4)
    test1c2 = exact_answer('question 1c-2', [r'1c. .+? tabledata .+ (wrist|strap|brac) .+ 2.'], text, points=3)
    test1c3 = exact_answer('question 1c-3', [r'1c. .+? tabledata .+ (mat|rug) .+ 2.'], text, points=3)
    test2a = exact_answer('question 2a', [r'2a. .+? tabledata .+ small .+ form .+ factor .+ 2b.',
                                          r'2a. .+? tabledata .+ micro .+ 2b.',
                                          r'2a. .+? tabledata .+ tower.+ 2b.',
                                          r'2a. .+? tabledata .+ rack.+ 2b.'], text, points=3, required=2)
    test2b = exact_answer('question 2b', [r'2b. .+? tabledata .+ [a-zA-Z] .+ pci'], text, points=1)
    test3a = exact_answer('question 3a', [r'3a. .+? tabledata .+ inlineobject .+ 3b'], text, points=1)
    test3b = exact_answer('question 3b', [r'3b. .+? tabledata .+ [a-zA-Z] .+ pci'], text, points=1)
    test4a = keyword_and_length('question 4a', [r'[a-zA-Z]+'], text,
                                search_string=r'4a. .+? tabledata (.+) 4b', min_length=7, points=1)
    test4b = exact_answer('question 4b', [r'4b. .+? tabledata .+ (1|16) .+ 4c'], text, points=5)
    test4c = keyword_and_length('question 4c', [r'[a-zA-Z]+'], text,
                                search_string=r'4c. .+? tabledata (.+) how', min_length=15, points=1)
    tests.extend([test1a, test1b, test1c1, test1c2, test1c3, test2a, test2b, test3a, test3b, test4a, test4b, test4c])
    return tests

