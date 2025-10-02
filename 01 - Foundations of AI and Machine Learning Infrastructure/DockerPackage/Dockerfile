FROM        python:3.13.3-slim
WORKDIR     /appdir
COPY        .   /appdir/
RUN         pip install --no-cache-dir -r requirements.txt
EXPOSE      80
CMD         python serve_model.py
