#Select Base iamge for run container

from python:3.9

# Environment settings

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Select Working Dir on Container

workdir /code

# Copy dependency list
copy requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

#Copy code to working dir
copy . /code/

# Expose port
expose 8000


#Run the code

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

