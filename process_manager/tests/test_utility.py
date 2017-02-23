from utility import *
import os

def test_file_types_are_correctly_searched():	
	HOME_PATH = os.path.dirname(os.path.abspath(__file__))
	assert find_scripts(HOME_PATH+"/fake_input") == ['p1.py','p2.py','p3.sh']
	assert find_scripts(HOME_PATH+"/fake_input", types=['*.xls']) == []
	


def test_invalid_program():
	assert run_program('test.xls') == False

