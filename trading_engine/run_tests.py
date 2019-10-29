import importlib
import sys
from config_manager import config_manager
from tests import test_data_engine, test_portfolio_manager

class run_tests:

	def __init__( self ):
		self.config = config_manager.read_config( './config/test.config.te' )

	def run( self ):
		test_data_engine.test_data_engine( self.config ).run()
		test_portfolio_manager.test_portfolio_manager( self.config ).run()

if __name__ == '__main__':
	test_runner = run_tests()
	test_runner.run()