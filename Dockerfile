FROM artifactory.ciena.com/blueplanet/base-image-devops-toolkit:20190716-py3.7

WORKDIR /bp2/src/

ARG pypi='https://artifactory.ciena.com/api/pypi/blueplanet-ubuntu-bionic-pypi/simple'

COPY .devops-toolkit /bp2/.devops-toolkit
COPY requirements.txt /bp2/src/
RUN pip install --find-links /bp2/.devops-toolkit -i $pypi -r requirements.txt

COPY . /bp2/src/
RUN pip install --find-links /bp2/.devops-toolkit -i $pypi -e .

RUN mkdir -p /bp2/log

ENV RASDK_SETTINGS_MODULE=arjun_ra.settings \
    SBIS=kafka,statsd,bpocore \
    BP2HOOK=http://{ip}:8888/bp2-hook
RUN ssh-keygen -t rsa -f /root/.ssh/id_rsa -q -N "" && \
    git config --global user.email "arjun_ra@ciena.com" && \
    git config --global user.name "arjun_ra"

CMD ["arjun_ra", "--logfile", "/bp2/log/arjun_ra.log", "--kafka"]
