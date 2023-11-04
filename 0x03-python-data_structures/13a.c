#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *idx_node(listint_t **head, int tcount)
{
	int i = 0;
	listint_t *Lnode = *head;

	while (i++ < tcount - 1)
	{
		Lnode = Lnode->next;
	}
	return (Lnode);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to head node.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *Bnode = *head, *tmp = *head;
	int count = 0,  tcount, i = 0;
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (tmp != NULL)
	{
		tmp = tmp->next;
		count++;
	}

	tcount = count;

	while (i++ < count/2)
	{
		tmp = idx_node(head, tcount--);

		if (tmp->n != Bnode->n)
			return (0);
		Bnode = Bnode->next;
	}
	return (1);
}
