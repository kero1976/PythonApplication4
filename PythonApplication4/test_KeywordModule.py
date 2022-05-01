import KeywordModule

def test_file_read_passing():

    lines = KeywordModule.read_keyword('テストデータ\\テスト3\\キーワード.txt')
    assert len(lines) == 5


def test_file_read_passing2():

    lines = KeywordModule.read_keyword('テストデータ\\テスト3\\キーワード2.txt')
    assert len(lines) == 5
