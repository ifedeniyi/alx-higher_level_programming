#include "lists.h"

/**
 * is_palindrome - checks if linked list is a palindrome
 *
 * @head: pointer to pointer to linked list
 * Return: (1) if palindrome, (0) otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int arr_length = 0;
	int *list_values;
	int i = 0;
	int j;

	while (current != NULL)
	{
		arr_length++;
		current = current->next;
	}

	list_values = (int *)malloc(sizeof(int) * arr_length);

	current = *head;
	while (current != NULL)
	{
		list_values[i] = current->n;
		current = current->next;
		i++;
	}

	current = *head;
	for (j = arr_length - 1; j >= 0; j--)
	{
		if (list_values[j] != current->n)
		{
			free(list_values);
			return (0);
		}

		current = current->next;
	}
	free(list_values);
	return (1);
}
