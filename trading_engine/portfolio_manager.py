from config_manager import config_manager

class portfolio_manager:

	def __init__( self, config ):
		self.portfolio_file_name = config.get('portfolio.file')
		self.portfolio = config_manager.read_config( self.portfolio_file_name )

	def buy( self, symbol, quantity ):
		assert( quantity > 0 );
		# we bought, so add the quantity in our portfolio
		self.portfolio[ symbol ] = self.portfolio[ symbol ] + quantity;

	def sell( self, symbol, quantity ):
		assert( quantity > 0 );
		# we sold, so we remove the quantity in our portfolio
		self.portfolio[ symbol ] = self.portfolio[ symbol ] - quantity;

	def reverse_position( self, symbol ):
		existing_pos = self.portfolio[symbol]
		self.portfolio[symbol] = - existing_pos;
		return existing_pos;

	def get_position( self, symbol ):
		return self.portfolio[symbol];

	def set_position( self, symbol, position ):
		self.portfolio[symbol] = position;

	def dump_portfolio( self ):
		config_manager.write_config( self.portfolio_file_name, self.portfolio );