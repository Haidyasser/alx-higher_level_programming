#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int len = 0, i = 0;
	int *array;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (current != NULL)
	{
		len++;
		current = current->next;
	}

	int array[len];

	current = *head;
	while (current != NULL)
	{
		array[i] = current->n;
		current = current->next;
		i++;
	}

	for (i = 0; i < len / 2; i++)
	{
		if (array[i] != array[len - i - 1])
		{
			return (0);
		}
	}
	return (1);
}
