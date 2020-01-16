FROM python:3.7-alpine
COPY . /usr/src/app/WorldOfGames
WORKDIR /usr/src/app/WorldOfGames
RUN pip install --no-cache-dir -r /usr/src/app/WorldOfGames/requirements.txt

CMD [ "python", "MainScores.py" ] 
