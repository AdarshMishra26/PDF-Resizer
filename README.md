PDF Size Modifier
===============

A simple web application that allows you to adjust the size of a PDF file by a specified percentage. This project is built using Flask, PyPDF2, and Bootstrap.

Requirements
------------

* Python 3.x
* Flask
* PyPDF2

Installation
------------

1. Clone the repository:
```bash
git clone https://github.com/your-username/pdf-size-modifier.git
```
2. Change to the project directory:
```bash
cd pdf-size-modifier
```
3. Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
```
4. Activate the virtual environment:
```bash
source venv/bin/activate (Unix)
venv\Scripts\activate (Windows)
```
5. Install the required packages:
```bash
pip install -r requirements.txt
```
Usage
-----

1. Run the Flask application:
```bash
python app.py
```
2. Open your web browser and navigate to `http://127.0.0.1:5000/`.
3. Choose a PDF file and enter the desired adjustment percentage.
4. Click "Upload & Adjust" to download the modified PDF file.

File Structure
--------------

* `app.py`: Main Flask application file.
* `templates/`: Contains the HTML templates.
	+ `index.html`: Main HTML file with the upload form.
* `static/`: Contains the CSS and JavaScript files.
	+ `styles.css`: Custom CSS styles.

Contributing
------------

Contributions are welcome! If you find any issues or want to add new features, please submit a pull request.

License
-------

This project is licensed under the [MIT License](LICENSE).

Author
------

Adarsh Mishra