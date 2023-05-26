from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def helloWorld():
    return render_template('index.html')


@app.route('/<string:page_name>/<name>')
def html_page(page_name, name=None):
    return render_template((str(page_name).__add__('.html')), name=name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict();
        write_to_csv(data)
        # return redirect('/thankyou/{name}/{messege}'
        #                 .format(name=date.get('name') , messege = date.get('email')))\
        return redirect('/thank_you/{name}'.format(name=data.get('name')))
    return 'سلام این خیلی باحاله'


@app.route('/thankyou/<name>/<messege>')
def thank_you(name, messege):
    return render_template('thank_you.html', name=name, messege=messege)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        message = data["message"]
        file = database.write(f'\n{email},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        # email = data["email"]
        # message = data["message"]
        # csv_writer = csv.writer(database2, delimiter=',')
        # csv_writer.writerow([email, message])
        csv_writer = csv.DictWriter(database2, fieldnames=data.keys(), delimiter=',')

        if read_csv() == 0:
            csv_writer.writeheader()
        csv_writer.writerow(data)


def read_csv():
    # line_number = 0
    with open('database.csv', mode='r', newline='') as database3:
        #     csv_reader = csv.reader(database3)
        #     for row in csv_reader:
        #         line_number +=1
        #
        # return line_number
        csv_reader = csv.reader(database3)
        list_of_rows = list(csv_reader)

    return len(list_of_rows)
