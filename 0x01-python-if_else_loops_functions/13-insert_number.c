#include "lists.h"

/**
 * insert_node - inserts a new node into a sorted singly linked list
 *
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head;
	listint_t *prevnode = *head;
	listint_t *newnode = malloc(sizeof(listint_t));

	if (!newnode)
		return (NULL);

	newnode->n = number;
	newnode->next = NULL;

	if (ptr == NULL)
	{
		*head = newnode;
		return (newnode);
	}

	while (ptr)
	{
		if (ptr->n > number)
		{
			newnode->next = ptr;

			if (prevnode == *head)
				*head = newnode;
			else
				prevnode->next = newnode;

			return (newnode);
		}
		prevnode = ptr;
		ptr = ptr->next;
	}
	prevnode->next = newnode;
	return (newnode);
}
