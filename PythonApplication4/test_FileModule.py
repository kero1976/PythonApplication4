import KeywordModule

def test_file_read_passing():

    lines = KeywordModule.read_keyword('テストデータ\\テスト3\\キーワード.txt')
    assert len(lines) == 5