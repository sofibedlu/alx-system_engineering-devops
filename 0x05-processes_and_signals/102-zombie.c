#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - create infinite loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - create five zombie process
 * Return: 0 for success
 */
int main(void)
{
	int i, status = 0;
	pid_t pid, wpid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid < 0)
		{
			perror("can't fork");
			exit(EXIT_FAILURE);
		}
		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", (int) getpid());
			exit(0);
		}
	}
	infinite_while();
	while ((wpid = wait(&status)) > 0);
	return (0);
}
