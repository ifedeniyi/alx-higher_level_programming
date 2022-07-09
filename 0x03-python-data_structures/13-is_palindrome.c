#include "lists.h"
#include <stdbool.h>

int check_palindrome(listint_t **left_ptr, listint_t *right_ptr);

/**
 * is_palindrome - checks if linked list is a palindrome
 *
 * @head: pointer to pointer to linked list
 * Return: (1) if palindrome, (0) otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *left = *head;
	listint_t *right = *head;

	return (check_palindrome(&left, right));
}

/**
 * check_palindrome - Recursively check if list is a palindrome
 *
 * @left_ptr: double pointer to linked list head
 * @right_ptr: pointer to linked list head
 * Return: (true) if palindrome, (false) otherwise
 */
int check_palindrome(listint_t **left_ptr, listint_t *right_ptr)
{
	bool is_palin = true;

	if (right_ptr == NULL)
	{
		return (true);
	}

	is_palin = check_palindrome(left_ptr, right_ptr->next);

	if (!is_palin)
	{
		return (false);
	}

	if (right_ptr->n != (*left_ptr)->n)
	{
		return (false);
	}

	*left_ptr = (*left_ptr)->next;
	return (true);
}
