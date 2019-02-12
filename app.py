from flask import Flask, render_template, request
import PlanechaseMap


app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

myPlanechaseMap = PlanechaseMap.Map()
# myPlanechaseMap.moveup()
# myPlanechaseMap.moveleft()
# myPlanechaseMap.movedown()
# myPlanechaseMap.movedown()
# myPlanechaseMap.moveright()
# myPlanechaseMap.moveright()
# myPlanechaseMap.moveup()
# myPlanechaseMap.moveup()
# myPlanechaseMap.moveleft()
# myPlanechaseMap.movedown()


# prevent cached responses
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def home():
	myPlanechaseMap.generate_map_image()
	return render_template("index.html", image_width = myPlanechaseMap.image_width, image_height = myPlanechaseMap.image_height)

@app.route('/movemap', methods=['POST'])
def movemap():

	f = request.form.to_dict()
	direction = f['id']
	print (direction)

	if direction == 'up':
		myPlanechaseMap.moveup()
	elif direction == 'left':
		myPlanechaseMap.moveleft()
	elif direction == 'right':
		myPlanechaseMap.moveright()
	elif direction == 'down':
		myPlanechaseMap.movedown()
	else:
		pass

	myPlanechaseMap.generate_map_image()

	return "nothing"

if __name__ == "__main__":
	app.run(debug=True)