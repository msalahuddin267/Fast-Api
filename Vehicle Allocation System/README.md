Prerequisites:
    - Python 3.9 or higher
    - MongoDB installed locally

Setup Instructions:
    1. Create a Virtual Environment
        - run this command to your terminal: virtualenv venv
        - activate command for virtual environment: ./venv/Scripts/activate
    2. Install Dependencies
        - run this command to your terminal: pip install -r requirements.txt

    3. Set up Environment Variables
        - create .env file
        - Paste this line: MONGODB_URI="mongodb://localhost:27017/vehicle_allocation"

    4. Run the Application
        - For run this command to your terminal: uvicorn app.main:app --reload
        - Project run at: http://127.0.0.1:8000
        - For Swagger documentation: http://127.0.0.1:8000/docs

    5. API Endpoints
        - Allocate a Vehicle: POST /vehicles/allocate
        - Update an Allocation: PUT /vehicles/update/{allocation_id}
        - Delete an Allocation: DELETE /vehicles/delete/{allocation_id}
        - Get Allocations History: GET /reports/allocations-report

    