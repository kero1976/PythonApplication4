import DirModule
import logging



def test_file_names_passing():

    files = DirModule.file_names('テストデータ\\テスト1')
    assert files == ['テストデータ\テスト1\ABC\TextFile1.txt','テストデータ\テスト1\ABC\TextFile2.txt','テストデータ\テスト1\DEF\XYZ\TextFile3.txt']

def test_file_ext_sarch_passing():

    files = DirModule.file_ext_sarch('テストデータ\\テスト2', "CSV")
    assert files == ['テストデータ\テスト2\ABC\TextFile1.csv','テストデータ\テスト2\DEF\XYZ\TextFile3.csv']

def test_file_name_sarch_passing():

    files = DirModule.file_name_sarch('テストデータ\\テスト2', "3")
    assert files == ['テストデータ\テスト2\DEF\XYZ\TextFile3.csv']