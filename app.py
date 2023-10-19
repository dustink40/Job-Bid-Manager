from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

def read_csv(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return list(reader)
    
@app.route('/')
def index():
    paid = read_csv('paid.csv')
    print("Paid: ", paid)
    paid_out = read_csv('paid_out.csv')
    return render_template('index.html', paid=paid, paid_out=paid_out)


@app.route('/submit_paid_out', methods=['POST'])
def submit_paid_out():
    bill_name = request.form.get('bill_name')
    total_amount = request.form.get('total_amount')
    amount_due = request.form.get('amount_due')
    due_date = request.form.get('due_date')
    payment_method = request.form.get('payment_method')

        # Write to bids.csv
    with open('paid_out.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([bill_name, total_amount, amount_due, due_date, payment_method])

    return redirect('/')


@app.route('/submit_paid', methods=['POST'])
def submit_paid():
    client_name = request.form.get('client_name')
    contact_info = request.form.get('contact_info')
    email = request.form.get('email')
    address = request.form.get('address')
    payment_date = request.form.get('payment_date')
    amount_paid = request.form.get('amount_paid')
    work_performed = request.form.get('work_performed')    

    # Write to jobs.csv
    with open('paid.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([client_name, contact_info, email, address, payment_date, amount_paid, work_performed])

    return redirect('/')

@app.route('/view_paid')
def view_paid():
    paid = read_csv('paid.csv')
    return render_template('view_paid.html', paid=paid)

@app.route('/view_paid_out')
def view_paid_out():
    paid_out = read_csv('paid_out.csv')
    return render_template('view_paid_out.html', paid_out=paid_out)

if __name__ == '__main__':
    app.run(debug=True)
