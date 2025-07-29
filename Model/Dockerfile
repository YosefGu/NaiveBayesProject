# שלב בסיס
FROM python:3.12-slim

# הגדרת משתנה סביבתי (מונע בעיות ב־Python)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# צור תקייה לפרויקט
WORKDIR /app

# העתקת קובץ תלויות
COPY requirements.txt .

# התקנת תלויות
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# העתק את כל הקבצים מהפרויקט
COPY . .

# חשיפת פורט
EXPOSE 8001

# הפעלת שרת uvicorn
CMD ["uvicorn", "Api.main:app", "--host", "0.0.0.0", "--port", "8001"]

