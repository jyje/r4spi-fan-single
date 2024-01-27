FROM python:3.12.1-slim

COPY . /repo
WORKDIR /repo/src

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    build-essential

RUN pip install --no-cache -r requirements.txt
RUN rm -rf /var/lib/apt/lists/*

CMD ["python", "main.py"]


# docker run \
#     --entrypoint sh \
#     --privileged \
#     -it \
#     r4spi-fan-single

# docker run \
#     --privileged \
#     r4spi-fan-single
