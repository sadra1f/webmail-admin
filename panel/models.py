import logging
import traceback

from django.conf import settings
from django.db import models
from paramiko import MissingHostKeyPolicy, SSHClient


class EmailAccount(models.Model):
    user = models.CharField(max_length=200, help_text="The E-Mail address")
    password = models.CharField(max_length=200)

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def delete(self, *args, **kwargs):
        logger = logging.getLogger(__name__)

        ssh = SSHClient()
        ssh.set_missing_host_key_policy(MissingHostKeyPolicy())
        # ssh.load_system_host_keys()

        for _ in range(5):
            try:
                ssh.connect(
                    hostname=settings.POSTFIX_SSH_HOST,
                    port=(
                        int(settings.POSTFIX_SSH_PORT)
                        if settings.POSTFIX_SSH_PORT.isdigit()
                        else 22
                    ),
                    username=settings.POSTFIX_SSH_USER,
                    password=settings.POSTFIX_SSH_PASSWORD,
                )
                break
            except:
                # TODO: Throw exception
                logger.error(traceback.format_exc())

        try:
            _, output, error = ssh.exec_command("setup email list")
            users = [line.strip().split()[1] for line in output if line.strip()]

            if self.user in users and len(list(error)) == 0:
                ssh.exec_command(f"setup email del {self.user}")

            return super().delete(*args, **kwargs)
        except:
            # TODO: Throw exception
            logger.error(traceback.format_exc())

    def save(self, *args, **kwargs):
        logger = logging.getLogger(__name__)

        ssh = SSHClient()
        ssh.set_missing_host_key_policy(MissingHostKeyPolicy())
        # ssh.load_system_host_keys()

        for _ in range(5):
            try:
                ssh.connect(
                    hostname=settings.POSTFIX_SSH_HOST,
                    port=(
                        int(settings.POSTFIX_SSH_PORT)
                        if settings.POSTFIX_SSH_PORT.isdigit()
                        else 22
                    ),
                    username=settings.POSTFIX_SSH_USER,
                    password=settings.POSTFIX_SSH_PASSWORD,
                )
                break
            except:
                # TODO: Throw exception
                logger.error(traceback.format_exc())

        try:
            _, output, error = ssh.exec_command("setup email list")
            users = [line.strip().split()[1] for line in output if line.strip()]

            output = []
            error = []

            if self._state.adding and len(list(error)) == 0:
                if self.user not in users:
                    _, output, error = ssh.exec_command(
                        f"setup email add {self.user} {self.password}"
                    )
                else:
                    _, output, error = ssh.exec_command(
                        f"setup email update {self.user} {self.password}"
                    )
            elif self.user in users and len(list(error)) == 0:
                _, output, error = ssh.exec_command(
                    f"setup email update {self.user} {self.password}"
                )
            else:
                # TODO: Throw exception
                logger.error("User not found.")

            for line in output:
                logger.info(line)
            for line in error:
                logger.error(line)

            return super().save(*args, **kwargs)
        except:
            # TODO: Throw exception
            logger.error(traceback.format_exc())
