# שלב בסיס
FROM python:3.12-slim

# הגדרת משתנה סביבתי (מונע בעיות ב־Python)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# התקנת תלות בסיסית
RUN apt-get update && apt-get install -y build-essential

# צור תקייה לפרויקט
WORKDIR /app

# העתק את כל הקבצים מהפרויקט
COPY . .

# התקנת תלויות
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# הפעלת שרת uvicorn
CMD ["uvicorn", "Api.main:app", "--host", "0.0.0.0", "--port", "8000"]

