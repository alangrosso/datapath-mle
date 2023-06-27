# 1. Imagen
FROM python:3.10.12

# Step 2. Copy local code to the container image
WORKDIR /app
COPY requirements.txt .
COPY model.joblib .
COPY scaler.joblib .
COPY utils /app/utils
COPY main.py .

# Step 3. Install production dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Run the python script
ENTRYPOINT [ "python", "main.py"]