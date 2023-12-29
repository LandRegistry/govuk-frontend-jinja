FROM python:3.11

WORKDIR /src

RUN apt-get update
RUN apt-get install -y wait-for-it
RUN curl -L https://github.com/matthew-shaw/govuk-frontend-diff/releases/download/v2.0.0/govuk-frontend-diff-linux --output govuk-frontend-diff && \
    chmod +x ./govuk-frontend-diff

ADD requirements-test-3.11.txt .
RUN pip3 install -r requirements-test-3.11.txt

ADD tests/utils tests/utils
ADD setup.cfg .
ADD govuk_frontend_jinja govuk_frontend_jinja

CMD /src/tests/utils/test-entrypoint.sh
