import pytest

from ticket.strings.StringUtils import StringUtils


@pytest.mark.unit
def centred_text_test001():
    string_utils = StringUtils()
    text = 'hello'
    char_amount = 6
    results = string_utils.centred_text(text, char_amount)
    assert ' hello ' == results


@pytest.mark.unit
def centred_text_test002():
    # prep
    string_utils = StringUtils()
    text = 'hello'
    char_amount = 4
    # run
    results = string_utils.centred_text(text, char_amount)
    # results
    assert 'hello' == results


@pytest.mark.unit
def centred_text_test003():
    # prep
    string_utils = StringUtils()
    text = None
    char_amount = 4
    # run
    results = string_utils.centred_text(text, char_amount)
    # results
    assert (results is None)


@pytest.mark.unit
def centred_text_test004():
    # prep
    string_utils = StringUtils()
    text = 'hello'
    char_amount = 7

    # run
    results = string_utils.centred_text(text, char_amount)

    # results
    assert '  hello ' == results


@pytest.mark.unit
def centred_text_test005():
    # prep
    string_utils = StringUtils()
    text = 'hello'
    char_amount = 8

    # run
    results = string_utils.centred_text(text, char_amount)

    # results
    assert '  hello  ' == results


@pytest.mark.unit
def cut_text_test_001():
    # prep
    string_utils = StringUtils()
    text = '  hello  '
    max_char = 7

    # run
    results = string_utils.cut_text(text, max_char)

    # results
    assert '  hello ' == results


@pytest.mark.unit
def cut_text_test_002():
    # prep
    string_utils = StringUtils()
    text = None
    max_char = 4

    # run
    results = string_utils.cut_text(text, max_char)

    # results
    assert (results is None)


@pytest.mark.unit
def cut_text_test_003():
    # prep
    string_utils = StringUtils()
    text = 'hello'
    max_char = 3

    # run
    results = string_utils.cut_text(text, max_char)

    # results
    assert ('hell' == results)


@pytest.mark.unit
def cut_text_test_004():
    # prep
    string_utils = StringUtils()
    text = '  hello  '
    max_char = 10

    # run
    results = string_utils.cut_text(text, max_char)

    # results
    assert ('  hello    ' == results)


@pytest.mark.unit
def justify_text_test_001():
    # prep
    string_utils = StringUtils()
    text = 'hello'
    char_amount = 7

    # run
    results = string_utils.justify_text(text, char_amount)

    # results
    assert ('   hello' == results)


@pytest.mark.unit
def justify_text_test_002():
    # prep
    string_utils = StringUtils()
    text = 'hellohello'
    char_amount = 8

    # run
    results = string_utils.justify_text(text, char_amount)

    # results
    assert (text == results)


@pytest.mark.unit
def justify_text_test_003():
    # prep
    string_utils = StringUtils()
    text = 'hellohello'
    char_amount = 7

    # run
    try:
        string_utils.justify_text(text, char_amount)
        assert False
    except Exception as e:
        assert ('Error' in str(e))


@pytest.mark.unit
def justify_text_test_004():
    # prep
    string_utils = StringUtils()
    text = None
    char_amount = 4

    # run
    results = string_utils.justify_text(text, char_amount)

    # results
    assert (results is None)


@pytest.mark.unit
def normalize_text_test_001():
    # prep
    string_utils = StringUtils()
    text = 'hello'
    char_amount = 7

    # run
    results = string_utils.normalize_text(text, char_amount)

    # results
    assert ('hello   ' == results)


@pytest.mark.unit
def normalize_text_test_002():
    # prep
    string_utils = StringUtils()
    text = 'hellohello'
    char_amount = 8

    # run
    results = string_utils.normalize_text(text, char_amount)

    # results
    assert (text == results)


@pytest.mark.unit
def normalize_text_test_003():
    # prep
    string_utils = StringUtils()
    text = 'hellohello'
    char_amount = 7

    # run
    try:
        string_utils.normalize_text(text, char_amount)
        assert False
    except Exception as e:
        assert ('Error' in str(e))


@pytest.mark.unit
def normalize_text_test_004():
    # prep
    string_utils = StringUtils()
    text = None
    char_amount = 4

    # run
    results = string_utils.normalize_text(text, char_amount)

    # results
    assert (results is None)
