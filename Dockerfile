
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Create a dedicated non-root application user
RUN addgroup --system app && adduser --system --ingroup app app

# Copy application files with correct ownership
COPY --chown=app:app . .

# Run application as non-root user
USER app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
