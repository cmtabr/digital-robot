extends Node2D

func _process(delta):
	$HTTPRequest.request("https://api-flask-digital-robot.onrender.com/data", [], false, HTTPClient.METHOD_GET)

func _on_request_error(error):
	print("Erro na solicitação: ", error)

func _on_HTTPRequest_request_completed(result, response_code, _headers, body):
	if result == HTTPRequest.RESULT_SUCCESS:
		var json_instance = JSON.new()
		var json_string = body.get_string_from_utf8()
		var json_data = json_instance.parse(json_string)
		var id = json_data["id"]
		var x = json_data["x"]
		var y = json_data["y"]
		var z = json_data["z"]
		$Sprite.position.x = x
		$Sprite.position.y = y
		proportion(z)

	else:
		print("Erro na solicitação: ", response_code)

func proportion(z):
	$Sprite.scale.x = z/100
	$Sprite.scale.y = z/100
