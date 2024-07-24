FROM mailserver/docker-mailserver:14.0

RUN apt update \
    && apt install -y openssh-server \
    && rm -rf /var/lib/apt/lists/*

RUN ssh-keygen -A \
    && mkdir -p /root/.ssh \
    && chmod 0700 /root/.ssh \
    && mkdir -p /var/run/sshd \
    && chmod 0755 /var/run/sshd \
    && ln -s /etc/ssh/ssh_host_ed25519_key.pub /root/.ssh/authorized_key

COPY chpasswd-supervisor.conf /etc/supervisor/conf.d/chpasswd-supervisor.conf
COPY sshd-supervisor.conf /etc/supervisor/conf.d/sshd-supervisor.conf
COPY sshd.conf /etc/ssh/sshd_config.d/sshd.conf

WORKDIR /

EXPOSE 25 587 143 465 993 110 995 4190 22

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
