# שלב בסיס
FROM python:3.12-slim

# צור תקייה לפרויקט
WORKDIR /app

# הגדרת משתנה סביבתי (מונע בעיות ב־Python)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# העתקת קובץ תלויות
COPY requirements.txt .

# התקנת תלויות
RUN pip install -r requirements.txt

# העתק את כל הקבצים מהפרויקט
COPY . /app

# חשיפת פורט
EXPOSE 8002

# הפעלת שרת uvicorn
CMD ["uvicorn", "Api.main:app", "--host", "0.0.0.0", "--port", "8002"]
