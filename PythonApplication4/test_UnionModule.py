import DirModule
import UnionMmodule

def test_union_keyword_passing():

    files = DirModule.file_name_sarch('テストデータ\\テスト4', 'Text')
    lines = UnionMmodule.union_keyword(files)
    assert len(lines) == 22

