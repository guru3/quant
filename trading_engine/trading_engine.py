import data_engine as dataE
import portfolio_manager as portfolioM

class trading_engine:

	def __init__( self ):
		self.__init_constants()
		self.config = self.__get_config()
		self.portfolio_manager = portfolioM.portfolio_manager( self.config );
		
	def __del__( self ):
		print('Exiting...')
	
	def __init_constants( self ):
		self.config_file_path = 'config/config.te'

	def __get_config( self ):
		config_file = open( self.config_file_path, 'r' )
		config = {}
		for line in config_file.read().splitlines():
			if line.startswith('#'):
				continue;
			key, value = line.split('=')
			config[key] = value
		return config;

	def main( self ):
		print('Welcome to the trading engine!')

		#TODO - read the command line arguments
		
		self.exit();

if __name__ == "__main__":
    te = trading_engine()
    te.main()