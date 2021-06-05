# Dockerfile for P2Pool Server

FROM ubuntu:20.04

LABEL maintainer David Parrish <daveparrish@tutanota.com>
LABEL description="Dockerized P2Pool"

WORKDIR /p2pool
ENV P2POOL_HOME /p2pool/p2pool
ENV P2POOL_REPO https://github.com/jtoomim/p2pool.git


# Using installation instructions for Linux
# https://github.com/jtoomim/p2pool/blob/155022fc942ec45778a95622766a9b11d923e76e/README.md
# hadolint ignore=DL3003
RUN apt-get update \
  && apt-get -y --no-install-recommends install ca-certificates=20* pypy=7.* pypy-dev=7.* pypy-setuptools=44.* gcc=4:9.* build-essential=12.* git=1:2.* wget=1.* \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && mkdir $P2POOL_HOME \
  && bash -c "wget https://bootstrap.pypa.io/ez_setup.py -O - | pypy" \
  && rm setuptools-*.zip \
  && wget https://pypi.python.org/packages/source/z/zope.interface/zope.interface-4.1.3.tar.gz#md5=9ae3d24c0c7415deb249dd1a132f0f79 \
  && tar zxf zope.interface-4.1.3.tar.gz \
  && cd /p2pool/zope.interface-4.1.3 \
  && pypy setup.py install \
  && cd /p2pool \
  && rm -r zope.interface-4.1.3* \
  && wget https://pypi.python.org/packages/source/T/Twisted/Twisted-15.4.0.tar.bz2 \
  && tar jxf Twisted-15.4.0.tar.bz2 \
  && cd /p2pool/Twisted-15.4.0 \
  && pypy setup.py install \
  && cd /p2pool \
  && rm -r Twisted-15.4.0*

COPY . $P2POOL_HOME

WORKDIR $P2POOL_HOME
ENTRYPOINT ["pypy", "run_p2pool.py"]
