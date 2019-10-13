def docs_feedback_cybersecurity_and_crime(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()

    text = get_text(link)
    test1a = keyword_and_length('1a. 3 examples of cybercrime', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+) 2a\.', min_length=10, points=1)
    test2a = keyword_and_length('2a. What is a virus', [r'[a-zA-Z]+'], text,
                                search_string=r'2a\. .+? tabledata (.+) 3a\.', min_length=7, points=1)
    test3a = keyword_and_length('3a. What is DDOS?', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) 4a\.', min_length=10, points=1)
    test4a = keyword_and_length('4a. What is phishing?', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+?) 5a\.', min_length=10, points=1)
    test5a = keyword_and_length('5a. Pick one, write about how to defend against it?', [r'[a-zA-Z]+'], text,
                                search_string=r'5a\. .+? tabledata (.+?) $', min_length=10, points=1)
    tests.extend([test1a, test2a, test3a, test4a, test5a,])
    return tests
