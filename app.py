from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

def read_csv(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)
    
@app.route('/')
def index():
    jobs = read_csv('jobs.csv')
    print("Jobs: ", jobs)
    bids = read_csv('bids.csv')
    print("Bids: ", bids)
    return render_template('index.html', jobs=jobs, bids=bids)


@app.route('/submit_bid', methods=['POST'])
def submit_bid():
    client_name = request.form.get('client_name')
    contact_info = request.form.get('contact_info')
    email_address = request.form.get('email_address')
    address = request.form.get('address')
    date_of_bid = request.form.get('date_of_bid')
    material_estimate = request.form.get('material_estimate')
    labor_estimate = request.form.get('labor_estimate')
    estimated_timeframe = request.form.get('estimated_timeframe')
    estimated_number_of_workers = request.form.get('estimated_number_of_workers')
    grand_total_of_bid = request.form.get('grand_total_of_bid')
    status = request.form.get('status')

    

    # Write to bids.csv
    with open('bids.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow({client_name, contact_info, email_address, address, date_of_bid, material_estimate, labor_estimate, estimated_timeframe, estimated_number_of_workers, grand_total_of_bid, status})

    return redirect('/')


@app.route('/submit_job', methods=['POST'])
def submit_job():
    client_name = request.form.get('client_name')
    contact_info = request.form.get('contact_info')
    location = request.form.get('location')
    job_details = request.form.get('job_details')
    start_date = request.form.get('start_date')
    estimated_enddate = request.form.get('estimated_enddate')
    onsite_workers = request.form.get('onsite_workers')
    progress = request.form.get('progress')

    print(client_name, contact_info, location, job_details, start_date, estimated_enddate, onsite_workers, progress)

    # Write to jobs.csv
    with open('jobs.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow({client_name, contact_info, location, job_details, start_date, estimated_enddate, onsite_workers, progress})

    return redirect('/')

@app.route('/view_jobs')
def view_jobs():
    jobs = read_csv('jobs.csv')
    return render_template('view_jobs.html', jobs=jobs)

@app.route('/view_bids')
def view_bids():
    bids = read_csv('bids.csv')
    return render_template('view_bids.html', bids=bids)

if __name__ == '__main__':
    app.run(debug=True)
