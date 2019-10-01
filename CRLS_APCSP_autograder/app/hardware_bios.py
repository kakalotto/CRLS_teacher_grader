def docs_feedback_hardware_bios(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()

    text = get_text(link)
    test1a = exact_answer('1a. BIOS version?', [r'1a\. .+? tabledata .*? A0 .+? 1b',], text, points=5)
    test1b = exact_answer('1b. BIOS year?', [r'1b\. .+? tabledata .*? 2 .+? 1c',], text, points=5)
    test1c = exact_answer('1c. How often?', [r'1c\. .+? tabledata .*? only .+? 1d',], text, points=5)
    test1d = keyword_and_length('1d. Explain how often?', [r'[a-ZA-Z]'], text,
                                 search_string=r'to \s 1c. .+? tabledata (.+?) oot', min_length=7, points=1)
    tests.extend([test1a, test1b, test1c, test1d,])
    return tests
