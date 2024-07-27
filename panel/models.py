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

    # TODO: Throw exceptions if the process was not successful
    def save(self, *args, **kwargs):
        logger = logging.getLogger(__name__)

        if self._state.adding:
            try:
                ssh = SSHClient()
                # ssh.load_system_host_keys()
                ssh.set_missing_host_key_policy(MissingHostKeyPolicy())

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
                        logger.error(traceback.format_exc())

                _, output, error = ssh.exec_command(
                    f"setup email add {self.user} {self.password}"
                )

                for line in output:
                    logger.info(line)
                for line in error:
                    logger.error(line)
            except:
                logger.error(traceback.format_exc())

        return super().save(*args, **kwargs)
