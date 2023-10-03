from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todo = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':  
        c = len(todo)
        title = request.form.get('title')
        description = request.form.get('description')
        todo.append({'id': c, 'title': title, 'description': description})
        c+=1
    return render_template('index.html', todo=todo)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    global todo
    if 0 <= id < len(todo):
        del todo[id-1]
    a=0
    for i in todo:
        i['id']=a
        a+=1
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
