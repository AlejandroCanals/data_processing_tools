# Projects: django_text_reader and sales_report_generator

## django_text_reader

### Description

The "django_text_reader" project is a web application developed with Django that allows users to upload and process text files for analysis and visualization.  

This mini-project has allowed me to further improve my skills with Python and Django, and also implement Docker, which is something I recently learned.

### Key Features

  - **File Upload**: Enables users to upload text files.
  - **Processing**: Analyzes and processes the uploaded text files to extract relevant information.
  - **Visualization**: Displays results or statistics derived from the processing.

### Technologies Used

  - Python
  - Django
  - HTML 5

Building the Docker Image

    Clone the repository from GitHub:
    
    git clone <repository_url>
    
    cd django_text_reader

Build the Docker image:

    docker build -t django-text-reader .

Running the Docker Container

    docker run -p 8000:8000 django-text-reader


## sales_report_generator
### Description

The "sales_report_generator" project is a command-line utility (CLI) that generates PDF reports based on sales data stored in a JSON file.
### Key Features

  - **Data Processing**: Reads and sorts sales data from a JSON file.
  - **Report Generation**: Creates PDF reports displaying the sorted data.
  - **User Interaction**: Allows the user to specify the generated PDF file name.

### Technologies Used

  - Python
  - ReportLab (for PDF generation)
  - JSON (for storing sales data)

### Installation and Usage

Clone the repository from GitHub:

    git clone <repository_url>
    
    cd sales_report_generator

Install the necessary dependencies:

    pip install -r requirements.txt

Run the script to generate a PDF report:

    python generate_report.py

Follow the instructions in the console to specify the PDF file name.
