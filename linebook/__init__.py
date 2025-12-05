try:
	import pymysql
	pymysql.install_as_MySQLdb()
except Exception:
	# PyMySQL no está instalado; mysqlclient puede usarse en su lugar
	pass
