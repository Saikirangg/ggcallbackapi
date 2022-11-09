import psycopg2
from app import app
from flask import flash, request
# from db_config import mysql
from flask import jsonify
# from flask import flash, request
# from werkzeug import generate_password_hash, check_password_hash
		
@app.route('/add', methods=['POST'])
def add_user():
	try:
		_json = request.json
		varient_type = ''
		varient_id = ''
		sku = ''
		varient_name = ''
		price_amount = ''
		cost_price_amount = ''
		quantity  = ''
		quantity_allocated = ''
		is_published = ''

		for i in _json:
			for j in i['variants']:
				varient_type = j['type']
				varient_id = j['id']
				sku = j['sku']
				varient_name = j['name']
				price_amount = j['price_amount']
				cost_price_amount = j['cost_price_amount']
				quantity = j['quantity']
				quantity_allocated = j['quantity_allocated']
				is_published = i['is_published']
				print(varient_type)
				print(varient_id)
				print(sku)
				print(varient_name)
				print(price_amount)
				print(cost_price_amount)
				print(quantity)
				print(quantity_allocated)
				print(is_published)
		
				conn = psycopg2.connect(
					host="database-crm.cazl4vulkacd.ap-south-1.rds.amazonaws.com",
					database="database_crm",
					user="database_gg_crm",
					password="Crmpostgres123"
				)
				# create a cursor
				cur = conn.cursor()
				# cur.execute("select * from inventory")
				# print(cur.fetchall())
				# insert_query = "insert into inventory (varient_type, varient_id, sku, varient_name, price_amount, cost_price_amount, quantity, quantity_allocated, is_published) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (varient_type, varient_id, sku, varient_name, price_amount, cost_price_amount, quantity, quantity_allocated, is_published)"
				cur.execute("update inventory set varient_type = %s, varient_id = %s, sku = %s, varient_name = %s, price_amount = %s, cost_price_amount = %s, quantity = %s, quantity_allocated = %s, is_published = %s where varient_id = %s", (varient_type, varient_id, sku, varient_name, price_amount, cost_price_amount, quantity, quantity_allocated, is_published, varient_id))
            			cur.execute("insert into inventory (varient_type, varient_id, sku, varient_name, price_amount, cost_price_amount, quantity, quantity_allocated, is_published) select %s, %s, %s, %s, %s, %s, %s, %s, %s where not exists (select 1 from inventory where varient_id = %s)", (varient_type, varient_id, sku, varient_name, price_amount, cost_price_amount, quantity, quantity_allocated, is_published, varient_id))
	
# 				#cur.execute("INSERT INTO inventory (varient_type, varient_id, sku, varient_name, price_amount, cost_price_amount, quantity, quantity_allocated, is_published) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (varient_type, varient_id, sku, varient_name, price_amount, cost_price_amount, quantity, quantity_allocated, is_published))
				# cur.execute(insert_query)
				conn.commit()
				# cur.execute("select * from product")
				cur.execute("select * from inventory")
				print(cur.fetchall())

		# get the data from the dict
		resp = jsonify('Data added successfully!')
		resp.status_code = 200
		return resp

		# _name = _json['name']
		# _email = _json['email']
		# _password = _json['pwd']
		# # validate the received values
		# if _name and _email and _password and request.method == 'POST':
		# 	#do not save password as a plain text
		# 	_hashed_password = generate_password_hash(_password)
		# 	# save edits
		# 	sql = "INSERT INTO tbl_user(user_name, user_email, user_password) VALUES(%s, %s, %s)"
		# 	data = (_name, _email, _hashed_password,)
		# 	conn = mysql.connect()
		# 	cursor = conn.cursor()
		# 	cursor.execute(sql, data)
		# 	conn.commit()
		# 	resp = jsonify('User added successfully!')
		# 	resp.status_code = 200
		# 	return resp
		# else:
		# 	return not_found()
	except Exception as e:
		print(e)
	finally:
		print("done")


		
# @app.route('/users')
# def users():
# 	try:
# 		conn = mysql.connect()
# 		cursor = conn.cursor(pymysql.cursors.DictCursor)
# 		cursor.execute("SELECT * FROM tbl_user")
# 		rows = cursor.fetchall()
# 		resp = jsonify(rows)
# 		resp.status_code = 200
# 		return resp
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close() 
# 		conn.close()
		
# @app.route('/user/<int:id>')
# def user(id):
# 	try:
# 		conn = mysql.connect()
# 		cursor = conn.cursor(pymysql.cursors.DictCursor)
# 		cursor.execute("SELECT * FROM tbl_user WHERE user_id=%s", id)
# 		row = cursor.fetchone()
# 		resp = jsonify(row)
# 		resp.status_code = 200
# 		return resp
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close() 
# 		conn.close()
# @app.route('/update', methods=['POST'])
# def update_user():
# 	try:
# 		_json = request.json
# 		_id = _json['id']
# 		_name = _json['name']
# 		_email = _json['email']
# 		_password = _json['pwd']		
# 		# validate the received values
# 		if _name and _email and _password and _id and request.method == 'POST':
# 			#do not save password as a plain text
# 			_hashed_password = generate_password_hash(_password)
# 			# save edits
# 			sql = "UPDATE tbl_user SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
# 			data = (_name, _email, _hashed_password, _id,)
# 			conn = mysql.connect()
# 			cursor = conn.cursor()
# 			cursor.execute(sql, data)
# 			conn.commit()
# 			resp = jsonify('User updated successfully!')
# 			resp.status_code = 200
# 			return resp
# 		else:
# 			return not_found()
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close() 
# 		conn.close()
		
# @app.route('/delete/<int:id>')
# def delete_user(id):
# 	try:
# 		conn = mysql.connect()
# 		cursor = conn.cursor()
# 		cursor.execute("DELETE FROM tbl_user WHERE user_id=%s", (id,))
# 		conn.commit()
# 		resp = jsonify('User deleted successfully!')
# 		resp.status_code = 200
# 		return resp
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close() 
# 		conn.close()
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp
		
if __name__ == "__main__":
    app.run()
