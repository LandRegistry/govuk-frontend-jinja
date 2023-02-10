FROM python:3.10

WORKDIR /src

RUN apt-get update
RUN apt-get install -y wait-for-it
RUN curl -L https://github.com/surevine/govuk-frontend-diff/releases/download/v1.1.2/govuk-frontend-diff-linux --output govuk-frontend-diff && \
    chmod +x ./govuk-frontend-diff

ADD requirements-test-3.10.txt .
RUN pip3 install -r requirements-test-3.10.txt

ADD tests/utils tests/utils
ADD setup.cfg .
ADD govuk_frontend_jinja govuk_frontend_jinja

CMD /src/tests/utils/test-entrypoint.sh
