
class config_manager():

	@staticmethod
	def read_config( file_path ):
		file_reader = open( file_path, 'r' )
		config = {}
		for line in file_reader.read().splitlines():
			if ( not line ) or line.startswith('#'):
				continue
			key, value = line.split('=')
			config[ key ] = value
		file_reader.close();
		return config;

	@staticmethod
	def write_config( file_path, config ):
		file_writer = open( file_path, 'w' )
		for key in config.keys():
			file_writer.writeline(key,'=',config[key])
		file_writer.close();

