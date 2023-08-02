from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play_default():
    return render_template('index.html', num_boxes=3, box_color='blue')

@app.route('/play/<int:num_boxes>')
def play_with_boxes(num_boxes):
    return render_template('index.html', num_boxes=num_boxes, box_color='blue')

@app.route('/play/<int:num_boxes>/<string:box_color>')
def play_with_boxes_and_color(num_boxes, box_color):
    return render_template('index.html', num_boxes=num_boxes, box_color=box_color)

if __name__ == '__main__':
    app.run(debug=True)

