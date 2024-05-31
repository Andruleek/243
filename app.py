from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample contacts list
contacts = [
    {'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com', 'phone': '123-456-7890', 'birthday': '1990-01-01'},
    {'first_name': 'Jane', 'last_name': 'Doe', 'email': 'jane@example.com', 'phone': '098-765-4321', 'birthday': '1992-02-02'},
    # Add more contacts here
]

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/contacts')
def index():
    search_query = request.args.get('search', '').lower()
    filtered_contacts = [contact for contact in contacts if 
                         search_query in contact['first_name'].lower() or 
                         search_query in contact['last_name'].lower() or 
                         search_query in contact['email'].lower()]
    return render_template('index.html', contacts=filtered_contacts)

@app.route('/create_contact', methods=['GET', 'POST'])
def create_contact():
    if request.method == 'POST':
        new_contact = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'birthday': request.form['birthday']
        }
        contacts.append(new_contact)
        return redirect(url_for('index'))
    return render_template('create_contact.html')

@app.route('/delete_contact/<int:index>', methods=['POST'])
def delete_contact(index):
    if 0 <= index < len(contacts):
        del contacts[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
