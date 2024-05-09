from flask import Flask, render_template, request, send_file, flash
from PyPDF2 import PdfReader, PdfWriter
import io

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Get uploaded file
        uploaded_file = request.files['file']

        if uploaded_file.filename == '':
            flash('No file selected!')
            return render_template('index.html')

        if uploaded_file.mimetype != 'application/pdf':
            flash('Invalid file type! Please upload a PDF.')
            return render_template('index.html')

        try:
            # Read PDF file
            pdf_reader = PdfReader(uploaded_file)
            pdf_writer = PdfWriter()

            # Get adjustment percentage from the form
            adjustment_percentage = int(request.form['adjustment'])
            if 0 <= adjustment_percentage <= 100:
                # Calculate the adjustment factor
                adjustment_factor = 1 - (adjustment_percentage / 100.0)

                # Iterate through each page of the PDF and adjust its size
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    # Adjusting size uniformly
                    page.scale(adjustment_factor, adjustment_factor)
                    pdf_writer.add_page(page)

                # Create a buffer to hold the PDF content
                output_pdf = io.BytesIO()
                # Write the modified PDF content to the buffer
                pdf_writer.write(output_pdf)
                # Move to the beginning of the buffer
                output_pdf.seek(0)

                # Set the filename for download
                filename = uploaded_file.filename.split('.')[0] + '_adjusted.pdf'

                # Return the modified PDF file for download
                return send_file(output_pdf, as_attachment=True, download_name=filename,
                                 mimetype='application/pdf')
            else:
                flash('Adjustment percentage should be between 0 and 100.')
                return render_template('index.html')

        except Exception as e:
            flash(f'Error processing the file: {str(e)}')
            return render_template('index.html')

    # Render the upload form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
