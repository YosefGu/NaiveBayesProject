# שלב בסיס
FROM python:3.12-slim

# צור תקייה לפרויקט
WORKDIR /app

# הגדרת משתנה סביבתי (מונע בעיות ב־Python)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# התקנת תלות בסיסית
RUN apt-get update && apt-get install -y build-essential

# התקנת תלויות
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install fastapi uvicorn requests

# העתק את כל הקבצים מהפרויקט
COPY . /app


# חשיפת פורט
EXPOSE 8000

# הפעלת שרת uvicorn
CMD ["uvicorn", "Api.main:app", "--host", "0.0.0.0", "--port", "8000"]
