#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: head node
 * Return: the new head
 */

void reverse_listint(listint_t **head)
{
	listint_t *new = *head, *prev = NULL, *next;

	while (new)
	{
		next = new->next;
		new->next = prev;
		prev = new;
		new = next;
	}
	*head = prev;
	
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to head node.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *half = NULL;
	
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			half = slow->next;
			break;
		}
		if (!fast->next)
		{
			half = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&half);

	while (half && temp)
	{
		if (temp->n == half->n)
		{
			half = half->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	return (1);
}
