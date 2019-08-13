import wave_editor
import mock
import filecmp
import os

##############################################################
#                       IMPORTANT!!!                         #
# Fill next line with the first function called in your code!#
##############################################################

FIRST_CALL_FANC = wave_editor.main


def test_revers_1():
    inputs = ['1', 'for_test_1.wav', "1", "1", "test.wav", ]
    input_generator = (i for i in inputs)
    with mock.patch('wave_editor.input', lambda prompt: next(input_generator)):
        try:
            FIRST_CALL_FANC()
        except StopIteration:
            assert True

    assert filecmp.cmp("test.wav", "for_test_1_rev.wav")


def test_revers_2():
    inputs = ['1', 'batman_theme_x.wav', "1", "1", "test.wav", ]
    input_generator = (i for i in inputs)
    with mock.patch('wave_editor.input', lambda prompt: next(input_generator)):
        try:
            FIRST_CALL_FANC()
        except StopIteration:
            assert True
    assert filecmp.cmp("test.wav", "batman_theme_x_1.wav")



def test_faster_1():
    inputs = ['1', 'for_test_1.wav', "2", "1", "test.wav"]
    input_generator = (i for i in inputs)
    with mock.patch('wave_editor.input', lambda prompt: next(input_generator)):
        try:
            FIRST_CALL_FANC()
        except StopIteration:
            True
    assert filecmp.cmp("test.wav", "for_test_1_faster.wav")


def test_faster_2():
    inputs = ['1', 'bugs_whats_up_doc.wav', "2", "1", "test.wav"]
    input_generator = (i for i in inputs)
    with mock.patch('wave_editor.input', lambda prompt: next(input_generator)):
        try:
            FIRST_CALL_FANC()
        except StopIteration:
            True
    assert filecmp.cmp("test.wav", "bugs_whats_up_doc_2.wav")


def test_slower_1():
    inputs = ['1', 'for_test_1.wav', "3", "1", "test.wav"]
    input_generator = (i for i in inputs)
    with mock.patch('wave_editor.input', lambda prompt: next(input_generator)):
        try:
            FIRST_CALL_FANC()
        except StopIteration:
            True
    assert filecmp.cmp("test.wav", "for_test_1_slower.wav")


def test_slower_2():
    inputs = ['1', 'seinfeld.wav', "3", "1", "test.wav"]
    input_generator = (i for i in inputs)
    with mock.patch('wave_editor.input', lambda prompt: next(input_generator)):
        try:
            FIRST_CALL_FANC()
        except StopIteration:
            assert True
    assert filecmp.cmp("test.wav", "seinfeld_3.wav")


def test_vol_up_1():
    inputs = ['1', 'for_test_1.wav', "4", "1", "test.wav"]
    input_generator = (i for i in inputs)
    with mock.patch('wave_editor.input', lambda prompt: next(input_generator)):
        try:
            FIRST_CALL_FANC()
        except StopIteration:
            assert True
    assert filecmp.cmp("test.wav", "for_test_1_vol_up.wav")


def test_vol_up__2():
    inputs = ['1', 'seinfeld.wav', "4", "1", "test.wav"]
    input_generator = (i for i in inputs)
    with mock.patch('wave_editor.input', lambda prompt: next(input_generator)):
        try:
            FIRST_CALL_FANC()
        except StopIteration:
            assert True
    assert filecmp.cmp("test.wav", "seinfeld_4.wav")


def test_vol_down_1():
    inputs = ['1', 'for_test_1.wav', "5", "1", "test.wav"]
    input_generator = (i for i in inputs)
    with mock.patch('wave_editor.input', lambda prompt: next(input_generator)):
        try:
            FIRST_CALL_FANC()
        except StopIteration:
            assert True
    assert filecmp.cmp("test.wav", "for_test_1_vol_down.wav")


def test_vol_down_2():
    inputs = ['1', 'this_boys_life_supper.wav', "5", "1", "test.wav"]
    input_generator = (i for i in inputs)
    with mock.patch('wave_editor.input', lambda prompt: next(input_generator)):
        try:
            FIRST_CALL_FANC()
        except StopIteration:
            assert True
    assert filecmp.cmp("test.wav", "this_boys_life_supper_5.wav")


def test_dim_1():
    inputs = ['1', 'for_test_1.wav', "6", "1", "test.wav"]
    input_generator = (i for i in inputs)
    with mock.patch('wave_editor.input', lambda prompt: next(input_generator)):
        try:
            FIRST_CALL_FANC()
        except StopIteration:
            assert True
    assert filecmp.cmp("test.wav", "for_test_1_dim.wav")


def test_dim_2():
    inputs = ['1', 'this_boys_life_supper.wav', "6", "1", "test.wav"]
    input_generator = (i for i in inputs)
    with mock.patch('wave_editor.input', lambda prompt: next(input_generator)):
        try:
            FIRST_CALL_FANC()
        except StopIteration:
            assert True
    assert filecmp.cmp("test.wav", "this_boys_life_supper_6.wav")


def test_unait_1():
    inputs = ['2', 'for_test_1.wav for_test_2.wav', "1", "test.wav"]
    input_generator = (i for i in inputs)
    with mock.patch('wave_editor.input', lambda prompt: next(input_generator)):
        try:
            FIRST_CALL_FANC()
        except StopIteration:
            assert True
    assert filecmp.cmp("test.wav", "for_test_1_2.wav")


def test_unait_2():
    inputs = ['2', 'batman_theme_x.wav bugs_whats_up_doc.wav', "1", "test.wav"]
    input_generator = (i for i in inputs)
    with mock.patch('wave_editor.input', lambda prompt: next(input_generator)):
        try:
            FIRST_CALL_FANC()
        except StopIteration:
            assert True
    assert filecmp.cmp("test.wav", "unit2.wav")


def test_unait_3():
    inputs = ['2', 'seinfeld.wav disco_dancing.wav', "1", "test.wav"]
    input_generator = (i for i in inputs)
    with mock.patch('wave_editor.input', lambda prompt: next(input_generator)):
        try:
            FIRST_CALL_FANC()
        except StopIteration:
            assert True
    assert filecmp.cmp("test.wav", "unit3.wav")


def test_compos_1():
    inputs = ['3', 'sample1.txt', "1", "test.wav"]
    input_generator = (i for i in inputs)
    with mock.patch('wave_editor.input', lambda prompt: next(input_generator)):
        try:
            FIRST_CALL_FANC()
        except StopIteration:
            assert True
    assert filecmp.cmp("test.wav", "sample1.wav")


def test_compos_2():
    inputs = ['3', 'sample2.txt', "1", "test.wav"]
    input_generator = (i for i in inputs)
    with mock.patch('wave_editor.input', lambda prompt: next(input_generator)):
        try:
            FIRST_CALL_FANC()
        except StopIteration:
            assert True
    assert filecmp.cmp("test.wav", "sample2.wav")


def test_compos_3():
    inputs = ['3', 'copos3.txt', "1", "test.wav"]
    input_generator = (i for i in inputs)
    with mock.patch('wave_editor.input', lambda prompt: next(input_generator)):
        try:
            FIRST_CALL_FANC()
        except StopIteration:
            assert True
    assert filecmp.cmp("test.wav", "copos3.wav")


def test_remove_garbage():
    os.remove("test.wav")


